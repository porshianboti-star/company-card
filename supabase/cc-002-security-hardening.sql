-- ============================================================
-- CompanyCard — cc-002: two access holes found while adding cc-001 (2026-09-29)
-- ------------------------------------------------------------
-- 1. public.signup_export() is SECURITY DEFINER and returned every admin's email,
--    company name and plan to anyone holding the public (publishable) key:
--      POST /rest/v1/rpc/signup_export  -> 200 with the full list (checked 2026-09-29).
--    Nothing in the site, the app or ~/ceo/tools calls it over REST; the
--    Management API (postgres) keeps access.
--
-- 2. profiles_update_self lets a signed-in user update ANY column of their own
--    profile row, and cards_public_read exposes cards.company_id to anon. A new
--    account could therefore set its own company_id to another tenant's id and
--    role to 'admin', and read that company's people and cards. The app itself
--    only ever updates `plan` on a profile (auth.js setPlan). This guard freezes
--    id, company_id, email and created_at for browser roles, and forbids a user
--    changing their own role. An admin changing a colleague's role is unchanged.
-- Idempotent. Never touches schema mb.
-- ============================================================

revoke all on function public.signup_export() from public, anon, authenticated;

create or replace function public.cc_profiles_tenant_guard()
returns trigger language plpgsql set search_path = public, pg_temp as $$
begin
  if current_user in ('anon', 'authenticated') then
    if new.id is distinct from old.id
       or new.company_id is distinct from old.company_id
       or new.email is distinct from old.email
       or new.created_at is distinct from old.created_at then
      raise exception 'These profile fields cannot be changed' using errcode = '42501';
    end if;
    if new.role is distinct from old.role and old.id = auth.uid() then
      raise exception 'You cannot change your own role' using errcode = '42501';
    end if;
  end if;
  return new;
end $$;
revoke all on function public.cc_profiles_tenant_guard() from public, anon, authenticated;
drop trigger if exists cc_profiles_tenant_guard on public.profiles;
create trigger cc_profiles_tenant_guard
  before update on public.profiles
  for each row execute function public.cc_profiles_tenant_guard();
