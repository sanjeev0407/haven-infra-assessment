from types import SimpleNamespace as NS

import pytest

from app.access_control import AccessDenied, can_view_screening_report, require_view_screening_report

# Two landlord accounts, one property and one tenant each.
# Tenant ids are deliberately identical across accounts to prove that
# tenant_id is not what grants access.
properties = {
    "p1": NS(id="p1", landlord_account_id="LA-1"),
    "p2": NS(id="p2", landlord_account_id="LA-2"),
}
tenants = {
    "t1": NS(id="t1", property_id="p1"),
    "t2": NS(id="t2", property_id="p2"),
}
report_a = NS(id="r1", tenant_id="t1")  # belongs to LA-1
report_b = NS(id="r2", tenant_id="t2")  # belongs to LA-2
manager_a = NS(id="m1", landlord_account_id="LA-1")


def test_same_account_allowed():
    assert can_view_screening_report(manager_a, report_a, tenants, properties)


def test_cross_account_denied():
    assert not can_view_screening_report(manager_a, report_b, tenants, properties)


def test_require_raises_on_cross_account():
    with pytest.raises(AccessDenied):
        require_view_screening_report(manager_a, report_b, tenants, properties)


def test_dangling_reference_fails_closed():
    orphan = NS(id="r9", tenant_id="missing")
    assert not can_view_screening_report(manager_a, orphan, tenants, properties)


def test_manager_without_account_denied():
    nobody = NS(id="m9", landlord_account_id=None)
    assert not can_view_screening_report(nobody, report_a, tenants, properties)
