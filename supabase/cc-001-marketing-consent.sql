-- ============================================================
-- CompanyCard — cc-001: consent-gated marketing email (2026-09-29)
-- ------------------------------------------------------------
-- Additive and idempotent. Applied to production project ohobtgbyrlczfdztzvqi
-- through the Management API as postgres, after a full dry run inside one
-- implicit transaction that was rolled back. Never touches schema mb.
--
-- What it adds
--   public.profiles        + marketing_opt_in (default false), marketing_opt_in_at,
--                            marketing_opt_in_source, marketing_consent_text_version,
--                            marketing_unsubscribed_at
--   public.marketing_consent_texts  the exact wording behind each version id
--   public.marketing_consent_log    append-only record of every opt-in / opt-out
--                                   (kept after an account is deleted: no FK)
--   public.coupon_emails            one row per (user, campaign) actually sent
--   priv.mail_keys                  HMAC secret for unsubscribe links (locked schema)
--   public.set_marketing_opt_in(bool)          signed-in user, Settings toggle
--   public.marketing_unsubscribe(uuid, text)   anon, the /unsubscribe page
--   trigger on auth.users           reads the signup checkbox from user metadata
--   trigger on public.profiles      marketing columns change only through the
--                                   functions above, never by a direct REST update
--
-- Rules the mailer must follow (not enforced here):
--   * send only to profiles with marketing_opt_in = true, to auth.users.email
--     (verified), never to profiles.email;
--   * the unsubscribe link is https://company-card.com/unsubscribe?u=<id>&t=<hex>
--     where <hex> = lowercase hex HMAC-SHA256(key = priv.mail_keys secret,
--     message = the user id as lowercase hyphenated text);
--   * insert into public.coupon_emails before/after each send so no user gets a
--     campaign twice.
--
-- The secret itself is NOT in this file. It was generated with
-- `openssl rand -hex 32`, inserted once with
--   insert into priv.mail_keys (product, secret) values ('companycard', '<hex>');
-- and kept locally at ~/.config/ceo/mail-hmac-companycard (chmod 600).
-- ============================================================

-- ---------- consent columns on the CompanyCard profile table ----------
alter table public.profiles add column if not exists marketing_opt_in boolean not null default false;
alter table public.profiles add column if not exists marketing_opt_in_at timestamptz;
alter table public.profiles add column if not exists marketing_opt_in_source text;
alter table public.profiles add column if not exists marketing_consent_text_version text;
alter table public.profiles add column if not exists marketing_unsubscribed_at timestamptz;

-- ---------- the exact wording behind each version id ----------
create table if not exists public.marketing_consent_texts (
  version    text primary key,
  body       text not null,
  created_at timestamptz not null default now()
);
insert into public.marketing_consent_texts (version, body) values
  ('cc-2026-09-29', 'Send me CompanyCard tips and occasional offers by email. Unsubscribe anytime.')
on conflict (version) do nothing;

-- ---------- append-only consent record ----------
create table if not exists public.marketing_consent_log (
  id           bigserial primary key,
  user_id      uuid not null,
  email        text,
  event        text not null check (event in ('opt_in','opt_out')),
  source       text not null,
  text_version text,
  created_at   timestamptz not null default now()
);
create index if not exists marketing_consent_log_user_idx on public.marketing_consent_log(user_id);

-- ---------- sends ----------
create table if not exists public.coupon_emails (
  user_id     uuid not null,
  campaign    text not null,
  sent_at     timestamptz not null default now(),
  provider_id text,
  primary key (user_id, campaign)
);

-- ---------- HMAC secret (locked schema; priv has no anon/authenticated usage) ----------
create schema if not exists priv;
create table if not exists priv.mail_keys (
  product    text primary key,
  secret     text not null check (length(secret) >= 32),
  created_at timestamptz not null default now()
);

-- Supabase's default privileges grant everything in public to anon and
-- authenticated. None of these tables is for the browser.
alter table public.marketing_consent_texts enable row level security;
alter table public.marketing_consent_log   enable row level security;
alter table public.coupon_emails           enable row level security;
alter table priv.mail_keys                 enable row level security;
revoke all on public.marketing_consent_texts from public, anon, authenticated;
revoke all on public.marketing_consent_log   from public, anon, authenticated;
revoke all on public.coupon_emails           from public, anon, authenticated;
revoke all on sequence public.marketing_consent_log_id_seq from public, anon, authenticated;
revoke all on priv.mail_keys from public, anon, authenticated, service_role;

-- ---------- guard: marketing columns are not writable by a direct REST update ----------
-- A signed-in user may update their own profile row (policy profiles_update_self)
-- and an admin may update employees' rows (profiles_update_admin). Neither may
-- touch consent: an admin must not opt an employee in, and the timestamps must
-- be server time. The SECURITY DEFINER functions below run as postgres, so
-- current_user is not anon/authenticated inside them.
create or replace function public.cc_profiles_marketing_guard()
returns trigger language plpgsql set search_path = public, pg_temp as $$
begin
  if current_user in ('anon', 'authenticated') then
    if tg_op = 'INSERT' then
      new.marketing_opt_in := false;
      new.marketing_opt_in_at := null;
      new.marketing_opt_in_source := null;
      new.marketing_consent_text_version := null;
      new.marketing_unsubscribed_at := null;
    elsif new.marketing_opt_in is distinct from old.marketing_opt_in
       or new.marketing_opt_in_at is distinct from old.marketing_opt_in_at
       or new.marketing_opt_in_source is distinct from old.marketing_opt_in_source
       or new.marketing_consent_text_version is distinct from old.marketing_consent_text_version
       or new.marketing_unsubscribed_at is distinct from old.marketing_unsubscribed_at then
      raise exception 'Email preferences change only through set_marketing_opt_in()'
        using errcode = '42501';
    end if;
  end if;
  return new;
end $$;
drop trigger if exists cc_profiles_marketing_guard on public.profiles;
create trigger cc_profiles_marketing_guard
  before insert or update on public.profiles
  for each row execute function public.cc_profiles_marketing_guard();

-- ---------- log every change of consent ----------
create or replace function public.cc_profiles_marketing_log()
returns trigger language plpgsql security definer set search_path = public, pg_temp as $$
declare
  v_src text := nullif(current_setting('cc.marketing_source', true), '');
begin
  if new.marketing_opt_in is distinct from old.marketing_opt_in
     or (new.marketing_unsubscribed_at is distinct from old.marketing_unsubscribed_at
         and new.marketing_unsubscribed_at is not null) then
    insert into public.marketing_consent_log (user_id, email, event, source, text_version)
    values (new.id,
            (select u.email from auth.users u where u.id = new.id),
            case when new.marketing_opt_in then 'opt_in' else 'opt_out' end,
            coalesce(v_src, case when new.marketing_opt_in then new.marketing_opt_in_source end, 'direct_sql'),
            case when new.marketing_opt_in then new.marketing_consent_text_version end);
  end if;
  return new;
end $$;
drop trigger if exists cc_profiles_marketing_log on public.profiles;
create trigger cc_profiles_marketing_log
  after update on public.profiles
  for each row execute function public.cc_profiles_marketing_log();

-- ---------- signup checkbox (email signup on /app/signup.html) ----------
-- auth.js sends options.data.marketing_opt_in = true and
-- marketing_consent_version = 'cc-2026-09-29' ONLY when the unchecked-by-default
-- box was ticked. Fires after on_auth_user_created (trigger names run in
-- alphabetical order), so the profile row already exists. It can never block
-- account creation.
create or replace function public.cc_marketing_signup_consent()
returns trigger language plpgsql security definer set search_path = public, pg_temp as $$
declare
  v_ver text := new.raw_user_meta_data->>'marketing_consent_version';
begin
  if coalesce(new.raw_user_meta_data->>'product', '') = 'meetingbrand' then
    return new;
  end if;
  if coalesce(new.raw_user_meta_data->>'marketing_opt_in', '') = 'true'
     and exists (select 1 from public.marketing_consent_texts t where t.version = v_ver) then
    perform set_config('cc.marketing_source', 'signup_checkbox', true);
    update public.profiles
       set marketing_opt_in = true,
           marketing_opt_in_at = now(),
           marketing_opt_in_source = 'signup_checkbox',
           marketing_consent_text_version = v_ver,
           marketing_unsubscribed_at = null
     where id = new.id;
    perform set_config('cc.marketing_source', '', true);
  end if;
  return new;
exception when others then
  return new;
end $$;
drop trigger if exists on_auth_user_created_marketing on auth.users;
create trigger on_auth_user_created_marketing
  after insert on auth.users
  for each row execute function public.cc_marketing_signup_consent();

-- ---------- Settings toggle (signed-in user, own row only) ----------
create or replace function public.set_marketing_opt_in(p_opt_in boolean)
returns boolean language plpgsql security definer set search_path = public, pg_temp as $$
declare
  v_uid uuid := auth.uid();
  v_now boolean;
begin
  if v_uid is null or p_opt_in is null then
    return null;
  end if;
  perform set_config('cc.marketing_source', 'settings_toggle', true);
  if p_opt_in then
    update public.profiles
       set marketing_opt_in = true,
           marketing_opt_in_at = now(),
           marketing_opt_in_source = 'settings_toggle',
           marketing_consent_text_version = 'cc-2026-09-29',
           marketing_unsubscribed_at = null
     where id = v_uid and not marketing_opt_in;
  else
    update public.profiles
       set marketing_opt_in = false,
           marketing_unsubscribed_at = now()
     where id = v_uid and marketing_opt_in;
  end if;
  perform set_config('cc.marketing_source', '', true);
  select marketing_opt_in into v_now from public.profiles where id = v_uid;
  return v_now;
end $$;

-- ---------- one-click unsubscribe (anon, from the email link) ----------
-- Returns true only when the token is the HMAC of the user id. The result does
-- not depend on whether the user exists, and the comparison touches every byte.
create or replace function public.marketing_unsubscribe(p_user uuid, p_token text)
returns boolean language plpgsql security definer set search_path = public, pg_temp as $$
declare
  v_key  text;
  v_want bytea;
  v_got  bytea;
  v_diff integer := 0;
  i      integer;
begin
  if p_user is null or p_token is null or p_token !~ '^[0-9A-Fa-f]{64}$' then
    return false;
  end if;
  select secret into v_key from priv.mail_keys where product = 'companycard';
  if v_key is null then
    return false;
  end if;
  v_want := extensions.hmac(p_user::text, v_key, 'sha256');
  v_got  := decode(lower(p_token), 'hex');
  for i in 0..31 loop
    v_diff := v_diff | (get_byte(v_want, i) # get_byte(v_got, i));
  end loop;
  if v_diff <> 0 then
    return false;
  end if;
  perform set_config('cc.marketing_source', 'unsubscribe_link', true);
  update public.profiles
     set marketing_opt_in = false,
         marketing_unsubscribed_at = case
           when marketing_opt_in or marketing_unsubscribed_at is null then now()
           else marketing_unsubscribed_at end
   where id = p_user;
  perform set_config('cc.marketing_source', '', true);
  return true;
end $$;

-- ---------- execute grants ----------
-- Supabase grants EXECUTE on every new public function to PUBLIC, anon and
-- authenticated by default; narrow each one.
revoke all on function public.cc_profiles_marketing_guard()      from public, anon, authenticated;
revoke all on function public.cc_profiles_marketing_log()        from public, anon, authenticated;
revoke all on function public.cc_marketing_signup_consent()      from public, anon, authenticated;
revoke all on function public.set_marketing_opt_in(boolean)      from public, anon, authenticated;
revoke all on function public.marketing_unsubscribe(uuid, text)  from public, anon, authenticated;
grant execute on function public.set_marketing_opt_in(boolean)     to authenticated;
grant execute on function public.marketing_unsubscribe(uuid, text) to anon;
