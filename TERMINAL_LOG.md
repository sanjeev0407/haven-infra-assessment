# Terminal Log

## Setup
```
Python 3.12.6
Terraform v1.10.0
on windows_amd64

Your version of Terraform is out of date! The latest version
is 1.17.2. You can update by downloading from https://www.terraform.io/downloads.html
```

## Terraform plan
```

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  [32m+[0m create[0m

Terraform will perform the following actions:

[1m  # aws_s3_bucket.listing_media[0m will be created
[0m  [32m+[0m[0m resource "aws_s3_bucket" "listing_media" {
      [32m+[0m[0m acceleration_status         = (known after apply)
      [32m+[0m[0m acl                         = (known after apply)
      [32m+[0m[0m arn                         = (known after apply)
      [32m+[0m[0m bucket                      = "haven-listing-media"
      [32m+[0m[0m bucket_domain_name          = (known after apply)
      [32m+[0m[0m bucket_prefix               = (known after apply)
      [32m+[0m[0m bucket_regional_domain_name = (known after apply)
      [32m+[0m[0m force_destroy               = false
      [32m+[0m[0m hosted_zone_id              = (known after apply)
      [32m+[0m[0m id                          = (known after apply)
      [32m+[0m[0m object_lock_enabled         = (known after apply)
      [32m+[0m[0m policy                      = (known after apply)
      [32m+[0m[0m region                      = (known after apply)
      [32m+[0m[0m request_payer               = (known after apply)
      [32m+[0m[0m tags_all                    = (known after apply)
      [32m+[0m[0m website_domain              = (known after apply)
      [32m+[0m[0m website_endpoint            = (known after apply)

      [32m+[0m[0m cors_rule (known after apply)

      [32m+[0m[0m grant (known after apply)

      [32m+[0m[0m lifecycle_rule (known after apply)

      [32m+[0m[0m logging (known after apply)

      [32m+[0m[0m object_lock_configuration (known after apply)

      [32m+[0m[0m replication_configuration (known after apply)

      [32m+[0m[0m server_side_encryption_configuration (known after apply)

      [32m+[0m[0m versioning (known after apply)

      [32m+[0m[0m website (known after apply)
    }

[1m  # aws_s3_bucket_lifecycle_configuration.listing_media_archive[0m will be created
[0m  [32m+[0m[0m resource "aws_s3_bucket_lifecycle_configuration" "listing_media_archive" {
      [32m+[0m[0m bucket                                 = (known after apply)
      [32m+[0m[0m expected_bucket_owner                  = (known after apply)
      [32m+[0m[0m id                                     = (known after apply)
      [32m+[0m[0m transition_default_minimum_object_size = "all_storage_classes_128K"

      [32m+[0m[0m rule {
          [32m+[0m[0m id     = "archive-sold-listing-photos"
          [32m+[0m[0m status = "Enabled"
            [90m# (1 unchanged attribute hidden)[0m[0m

          [32m+[0m[0m transition {
              [32m+[0m[0m days          = 30
              [32m+[0m[0m storage_class = "GLACIER"
            }
        }
    }

[1mPlan:[0m 2 to add, 0 to change, 0 to destroy.
[0m[33m╷[0m[0m
[33m│[0m [0m[1m[33mWarning: [0m[0m[1mInvalid Attribute Combination[0m
[33m│[0m [0m
[33m│[0m [0m[0m  with aws_s3_bucket_lifecycle_configuration.listing_media_archive,
[33m│[0m [0m  on lifecycle.tf line 15, in resource "aws_s3_bucket_lifecycle_configuration" "listing_media_archive":
[33m│[0m [0m  15: resource "aws_s3_bucket_lifecycle_configuration" "listing_media_archive" [4m{[0m[0m
[33m│[0m [0m
[33m│[0m [0mNo attribute specified when one (and only one) of
[33m│[0m [0m[rule[0].filter,rule[0].prefix] is required
[33m│[0m [0m
[33m│[0m [0mThis will be an error in a future version of the provider
[33m│[0m [0m
[33m│[0m [0m(and one more similar warning elsewhere)
[33m╵[0m[0m
[90m
─────────────────────────────────────────────────────────────────────────────[0m

Note: You didn't use the -out option to save this plan, so Terraform can't
guarantee to take exactly these actions if you run "terraform apply" now.
```

## Access test run
```
============================= test session starts =============================
platform win32 -- Python 3.12.6, pytest-9.2.0, pluggy-1.7.0 -- C:\Users\sananaga\Downloads\assignments\haven-infra-assessment\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\sananaga\Downloads\assignments\haven-infra-assessment
collecting ... collected 5 items

tests/test_access_control.py::test_same_account_allowed PASSED           [ 20%]
tests/test_access_control.py::test_cross_account_denied PASSED           [ 40%]
tests/test_access_control.py::test_require_raises_on_cross_account PASSED [ 60%]
tests/test_access_control.py::test_dangling_reference_fails_closed PASSED [ 80%]
tests/test_access_control.py::test_manager_without_account_denied PASSED [100%]

============================== 5 passed in 0.03s ==============================
```

## Cost-tag test run
```
============================= test session starts =============================
platform win32 -- Python 3.12.6, pytest-9.2.0, pluggy-1.7.0 -- C:\Users\sananaga\Downloads\assignments\haven-infra-assessment\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\sananaga\Downloads\assignments\haven-infra-assessment
collecting ... collected 6 items

tests/test_cost_tag_check.py::test_missing_tag_fails_and_tenant_id_does_not_count PASSED [ 16%]
tests/test_cost_tag_check.py::test_present_tag_passes PASSED             [ 33%]
tests/test_cost_tag_check.py::test_empty_tag_value_fails PASSED          [ 50%]
tests/test_cost_tag_check.py::test_generic_across_types PASSED           [ 66%]
tests/test_cost_tag_check.py::test_deleted_resources_are_skipped PASSED  [ 83%]
tests/test_cost_tag_check.py::test_idempotent PASSED                     [100%]

============================== 6 passed in 0.03s ==============================
```

## Cost-tag check, run 1
```
{
  "required_tag": "landlord_account_id",
  "violations": [
    {
      "address": "aws_lambda_function.mls_feed_sync",
      "type": "aws_lambda_function",
      "reason": "missing or empty tag 'landlord_account_id'"
    },
    {
      "address": "aws_s3_bucket.listing_media",
      "type": "aws_s3_bucket",
      "reason": "missing or empty tag 'landlord_account_id'"
    }
  ],
  "result": "FAIL"
}
```

## Cost-tag check, run 2
```
{
  "required_tag": "landlord_account_id",
  "violations": [
    {
      "address": "aws_lambda_function.mls_feed_sync",
      "type": "aws_lambda_function",
      "reason": "missing or empty tag 'landlord_account_id'"
    },
    {
      "address": "aws_s3_bucket.listing_media",
      "type": "aws_s3_bucket",
      "reason": "missing or empty tag 'landlord_account_id'"
    }
  ],
  "result": "FAIL"
}
```

## Idempotency check
```
IDENTICAL
```
