"""Access check: a PropertyManager may view a ScreeningReport only if the
report belongs to the manager's own LandlordAccount.

Ownership chain: ScreeningReport -> Tenant -> Property -> LandlordAccount.
We compare landlord_account_id, never tenant_id.
"""
# ADAPT the attribute/lookup names below to app/models.py and app/seed_data.py.


class AccessDenied(Exception):
    pass


def landlord_account_for_report(report, tenants, properties):
    tenant = tenants[report.tenant_id]
    prop = properties[tenant.property_id]
    return prop.landlord_account_id


def can_view_screening_report(manager, report, tenants, properties) -> bool:
    try:
        owner = landlord_account_for_report(report, tenants, properties)
    except KeyError:
        return False  # fail closed on dangling references
    return manager.landlord_account_id is not None and manager.landlord_account_id == owner


def require_view_screening_report(manager, report, tenants, properties):
    if not can_view_screening_report(manager, report, tenants, properties):
        raise AccessDenied("manager cannot view reports outside own landlord account")
