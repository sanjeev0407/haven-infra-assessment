#!/usr/bin/env python3
"""Fail if any taggable resource in a Terraform plan JSON lacks landlord_account_id.

Usage: python scripts/cost_tag_check.py fixtures/plan.json
Output is deterministic: sorted by resource address, no timestamps.
"""
import json
import sys

REQUIRED_TAG = "landlord_account_id"
IGNORED_ACTIONS = ({"delete"}, {"no-op"})  # resources being removed / untouched


def _tags(after):
    # tags_all includes provider default_tags; fall back to tags
    for key in ("tags_all", "tags"):
        if after.get(key):
            return after[key]
    return {}


def check_plan(plan: dict) -> list[dict]:
    violations = []
    for rc in plan.get("resource_changes", []):
        change = rc.get("change", {})
        if set(change.get("actions", [])) in IGNORED_ACTIONS:
            continue
        after = change.get("after") or {}
        if "tags" not in after and "tags_all" not in after:
            continue  # resource type is not taggable: generic, no hardcoded types
        if change.get("after_unknown", {}).get("tags_all") is True:
            continue  # unknown at plan time; cannot judge
        value = _tags(after).get(REQUIRED_TAG)
        if value is None or str(value).strip() == "":
            violations.append({
                "address": rc["address"],  # idempotency key
                "type": rc.get("type"),
                "reason": f"missing or empty tag '{REQUIRED_TAG}'",
            })
    return sorted(violations, key=lambda v: v["address"])


def main(argv):
    with open(argv[1]) as f:
        plan = json.load(f)
    violations = check_plan(plan)
    print(json.dumps({"required_tag": REQUIRED_TAG,
                      "violations": violations,
                      "result": "FAIL" if violations else "PASS"}, indent=2))
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
