# Design notes

## Idempotency
The idempotency key is the resource `address` from the plan's `resource_changes`
(for example `aws_s3_bucket.media["acct-001"]`). Idempotency here means the result is a
pure function of the plan contents: violations are keyed by address, sorted by address,
contain no timestamps or run IDs, and the check mutates nothing. Re-running on an
unchanged plan produces byte-identical output and the same exit code.

## Decisions with real alternatives
- Ownership via landlord_account_id (report -> tenant -> property -> landlord),
  not tenant_id, because the README says landlord account is the billing/isolation unit.
- Fail closed on dangling references in the access check.
- Tag check reads `tags_all` then `tags`; a resource is "taggable" if the plan
  exposes those keys, so no hardcoded resource-type list. Alternative (an allowlist of types) rejected as brittle.
- Resources with `delete`/`no-op` actions are skipped; empty-string tags count as missing.
- Unknown-at-plan-time tags are skipped, not failed. Alternative: fail closed; tradeoff is noisy CI.
