-- ============================================================
-- CompanyCard — Supabase schema & security (run once)
-- Paste this whole file into: Supabase Dashboard → SQL Editor → Run
-- ============================================================
-- Model:
--   companies : one row per customer account (tenant)
--   profiles  : one row per user (linked to Supabase Auth), role = admin | employee
--   cards     : business cards; owner_id = the employee, company_id = tenant
--   invites   : admin-generated invite tokens for employees
--
-- Security (Row Level Security — enforced by the database itself):
--   * A user only ever sees rows of their OWN company (full tenant isolation)
--   * employee: sees/edits only their own card & profile
--   * admin  : sees all profiles/cards of their company, manages invites
--   * anonymous visitors: can read a card ONLY if it is published (public card page / QR)
-- ============================================================

-- ---------- Tables ----------
create table if not exists public.companies (
  id         uuid primary key default gen_random_uuid(),
  name       text not null,
  created_at timestamptz not null default now()
);

create table if not exists public.profiles (
  id         uuid primary key references auth.users(id) on delete cascade,
  company_id uuid not null references public.companies(id) on delete cascade,
  role       text not null check (role in ('admin','employee')) default 'employee',
  full_name  text,
  email      text,
  created_at timestamptz not null default now()
);

create table if not exists public.cards (
  id          uuid primary key default gen_random_uuid(),
  company_id  uuid not null references public.companies(id) on delete cascade,
  owner_id    uuid not null references auth.users(id) on delete cascade,
  slug        text unique,                 -- public URL slug (QR / share link)
  is_public   boolean not null default true,
  data        jsonb not null default '{}'::jsonb,   -- the card content
  updated_at  timestamptz not null default now(),
  created_at  timestamptz not null default now()
);
create index if not exists cards_company_idx on public.cards(company_id);
create index if not exists cards_owner_idx   on public.cards(owner_id);

create table if not exists public.invites (
  id         uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  token      uuid not null unique default gen_random_uuid(),
  email      text,
  role       text not null check (role in ('admin','employee')) default 'employee',
  created_by uuid not null references auth.users(id) on delete cascade,
  accepted_by uuid references auth.users(id),
  accepted_at timestamptz,
  expires_at timestamptz not null default now() + interval '14 days',
  created_at timestamptz not null default now()
);

-- ---------- Helper functions (used inside policies) ----------
create or replace function public.my_company() returns uuid
language sql stable security definer set search_path = public as
$$ select company_id from public.profiles where id = auth.uid() $$;

create or replace function public.my_role() returns text
language sql stable security definer set search_path = public as
$$ select role from public.profiles where id = auth.uid() $$;

-- ---------- Row Level Security ----------
alter table public.companies enable row level security;
alter table public.profiles  enable row level security;
alter table public.cards     enable row level security;
alter table public.invites   enable row level security;

-- companies: members can read their own company; admin can rename it
drop policy if exists companies_select on public.companies;
create policy companies_select on public.companies
  for select using (id = public.my_company());
drop policy if exists companies_update on public.companies;
create policy companies_update on public.companies
  for update using (id = public.my_company() and public.my_role() = 'admin');

-- profiles: user sees own profile; admin sees all profiles of own company
drop policy if exists profiles_select on public.profiles;
create policy profiles_select on public.profiles
  for select using (
    id = auth.uid()
    or (company_id = public.my_company() and public.my_role() = 'admin')
  );
drop policy if exists profiles_update_self on public.profiles;
create policy profiles_update_self on public.profiles
  for update using (id = auth.uid());
-- admin can update employees of own company (e.g. change role)
drop policy if exists profiles_update_admin on public.profiles;
create policy profiles_update_admin on public.profiles
  for update using (company_id = public.my_company() and public.my_role() = 'admin');
-- admin can remove an employee profile from own company
drop policy if exists profiles_delete_admin on public.profiles;
create policy profiles_delete_admin on public.profiles
  for delete using (
    company_id = public.my_company() and public.my_role() = 'admin' and id <> auth.uid()
  );

-- cards:
--   owner: full control of own cards
--   admin: read/update/delete every card of own company
--   anon : read only published cards (public card page / QR scan)
drop policy if exists cards_owner_all on public.cards;
create policy cards_owner_all on public.cards
  for all using (owner_id = auth.uid())
  with check (owner_id = auth.uid() and company_id = public.my_company());
drop policy if exists cards_admin_select on public.cards;
create policy cards_admin_select on public.cards
  for select using (company_id = public.my_company() and public.my_role() = 'admin');
drop policy if exists cards_admin_update on public.cards;
create policy cards_admin_update on public.cards
  for update using (company_id = public.my_company() and public.my_role() = 'admin');
drop policy if exists cards_admin_delete on public.cards;
create policy cards_admin_delete on public.cards
  for delete using (company_id = public.my_company() and public.my_role() = 'admin');
drop policy if exists cards_public_read on public.cards;
create policy cards_public_read on public.cards
  for select using (is_public = true);

-- invites: only admins of the company manage them
drop policy if exists invites_admin_all on public.invites;
create policy invites_admin_all on public.invites
  for all using (company_id = public.my_company() and public.my_role() = 'admin')
  with check (company_id = public.my_company() and public.my_role() = 'admin');

-- ---------- Signup trigger ----------
-- Runs when a new auth user is created.
--   metadata.company_name  → founder signup: create company, user becomes admin
--   metadata.invite_token  → employee signup: join the inviting company
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
declare
  v_company  uuid;
  v_role     text := 'employee';
  v_token    uuid;
  v_invite   public.invites%rowtype;
begin
  if new.raw_user_meta_data ? 'invite_token' then
    v_token := (new.raw_user_meta_data->>'invite_token')::uuid;
    select * into v_invite from public.invites
      where token = v_token and accepted_at is null and expires_at > now();
    if v_invite.id is null then
      raise exception 'Invite link is invalid or has expired';
    end if;
    v_company := v_invite.company_id;
    v_role    := v_invite.role;
    update public.invites
      set accepted_by = new.id, accepted_at = now() where id = v_invite.id;
  elsif new.raw_user_meta_data ? 'company_name' then
    insert into public.companies (name)
      values (coalesce(nullif(trim(new.raw_user_meta_data->>'company_name'), ''), 'My company'))
      returning id into v_company;
    v_role := 'admin';
  else
    raise exception 'Signup requires a company name or an invite';
  end if;

  insert into public.profiles (id, company_id, role, full_name, email)
  values (new.id, v_company, v_role,
          new.raw_user_meta_data->>'full_name', new.email);
  return new;
end $$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- ---------- Invite lookup for the signup page (anonymous, by token only) ----------
create or replace function public.invite_info(p_token uuid)
returns table (company_name text, email text, role text)
language sql stable security definer set search_path = public as $$
  select c.name, i.email, i.role
  from public.invites i join public.companies c on c.id = i.company_id
  where i.token = p_token and i.accepted_at is null and i.expires_at > now()
$$;

-- keep updated_at fresh
create or replace function public.touch_updated_at()
returns trigger language plpgsql as
$$ begin new.updated_at := now(); return new; end $$;
drop trigger if exists cards_touch on public.cards;
create trigger cards_touch before update on public.cards
  for each row execute function public.touch_updated_at();
