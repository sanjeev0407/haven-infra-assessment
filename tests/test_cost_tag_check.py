from scripts.cost_tag_check import check_plan


def rc(addr, tags, actions=("create",), key="tags"):
    return {
        "address": addr,
        "type": "x",
        "change": {"actions": list(actions), "after": {key: tags}},
    }


def test_missing_tag_fails_and_tenant_id_does_not_count():
    plan = {"resource_changes": [rc("aws_s3_bucket.a", {"tenant_id": "t1"})]}
    assert [v["address"] for v in check_plan(plan)] == ["aws_s3_bucket.a"]


def test_present_tag_passes():
    plan = {"resource_changes": [rc("x.y", {"landlord_account_id": "L1"})]}
    assert check_plan(plan) == []


def test_empty_tag_value_fails():
    plan = {"resource_changes": [rc("x.y", {"landlord_account_id": "  "})]}
    assert len(check_plan(plan)) == 1


def test_generic_across_types():
    plan = {"resource_changes": [rc("aws_sqs_queue.q", {}), rc("aws_dynamodb_table.t", {})]}
    assert len(check_plan(plan)) == 2


def test_deleted_resources_are_skipped():
    plan = {"resource_changes": [rc("x.gone", {}, actions=("delete",))]}
    assert check_plan(plan) == []


def test_idempotent():
    plan = {"resource_changes": [rc("b.z", {}), rc("a.y", {})]}
    first = check_plan(plan)
    assert first == check_plan(plan)
    assert [v["address"] for v in first] == ["a.y", "b.z"]  # sorted by address
