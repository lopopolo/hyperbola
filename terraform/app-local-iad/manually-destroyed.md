## S3 Media Bucket

### Forget

```shell
/usr/local/opt/terraform@0.12/bin/terraform state rm module.base.aws_s3_bucket.media
```

### Resource

```
# module.base.aws_s3_bucket.media will be destroyed
- resource "aws_s3_bucket" "media" {
    - acl                         = "private" -> null
    - arn                         = "arn:aws:s3:::local.hyperbolausercontent.net" -> null
    - bucket                      = "local.hyperbolausercontent.net" -> null
    - bucket_domain_name          = "local.hyperbolausercontent.net.s3.amazonaws.com" -> null
    - bucket_regional_domain_name = "local.hyperbolausercontent.net.s3.amazonaws.com" -> null
    - force_destroy               = false -> null
    - hosted_zone_id              = "Z3AQBSTGFYJSTF" -> null
    - id                          = "local.hyperbolausercontent.net" -> null
    - region                      = "us-east-1" -> null
    - request_payer               = "BucketOwner" -> null
    - tags                        = {
        - "Environment" = "local"
        - "Name"        = "hyperbola-app media files for local"
      } -> null

    - versioning {
        - enabled    = true -> null
        - mfa_delete = false -> null
      }
  }
```

### Remember

```console
$ /usr/local/opt/terraform@0.12/bin/terraform import module.base.aws_s3_bucket.media local.hyperbolausercontent.net
module.base.aws_s3_bucket.media: Importing from ID "local.hyperbolausercontent.net"...
module.base.aws_s3_bucket.media: Import prepared!
  Prepared aws_s3_bucket for import
module.base.aws_s3_bucket.media: Refreshing state... [id=local.hyperbolausercontent.net]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.

Releasing state lock. This may take a few moments...
```

## S3 Backup Bucket

### Forget

```shell
/usr/local/opt/terraform@0.12/bin/terraform state rm module.base.aws_s3_bucket.backup
```

### Resource

```
# module.base.aws_s3_bucket.backup will be destroyed
- resource "aws_s3_bucket" "backup" {
    - acl                         = "private" -> null
    - arn                         = "arn:aws:s3:::hyperbola-app-backup-local" -> null
    - bucket                      = "hyperbola-app-backup-local" -> null
    - bucket_domain_name          = "hyperbola-app-backup-local.s3.amazonaws.com" -> null
    - bucket_regional_domain_name = "hyperbola-app-backup-local.s3.amazonaws.com" -> null
    - force_destroy               = false -> null
    - hosted_zone_id              = "Z3AQBSTGFYJSTF" -> null
    - id                          = "hyperbola-app-backup-local" -> null
    - region                      = "us-east-1" -> null
    - request_payer               = "BucketOwner" -> null
    - tags                        = {
        - "Environment" = "local"
      } -> null

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }
```

### Remember

```console
$ /usr/local/opt/terraform@0.12/bin/terraform import module.base.aws_s3_bucket.backup hyperbola-app-backup-local
module.base.aws_s3_bucket.backup: Importing from ID "hyperbola-app-backup-local"...
module.base.aws_s3_bucket.backup: Import prepared!
  Prepared aws_s3_bucket for import
module.base.aws_s3_bucket.backup: Refreshing state... [id=hyperbola-app-backup-local]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.

Releasing state lock. This may take a few moments...
```

## `terraform destroy`

### Take 1

```console
/usr/local/opt/terraform@0.12/bin/terraform destroy
module.base.data.aws_acm_certificate.cdn: Refreshing state...
data.aws_route53_zone.dc: Refreshing state...
module.base.data.aws_iam_policy_document.assume: Refreshing state...
module.base.data.aws_route53_zone.hyperbolausercontent: Refreshing state...
module.base.aws_s3_bucket.media: Refreshing state... [id=local.hyperbolausercontent.net]
module.base.aws_s3_bucket.backup: Refreshing state... [id=hyperbola-app-backup-local]
data.aws_iam_policy_document.lb: Refreshing state...
module.app_policy.data.aws_iam_policy_document.this: Refreshing state...
module.base.module.app_policy.data.aws_iam_policy_document.this: Refreshing state...

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # module.base.aws_s3_bucket.backup will be destroyed
  - resource "aws_s3_bucket" "backup" {
      - arn                         = "arn:aws:s3:::hyperbola-app-backup-local" -> null
      - bucket                      = "hyperbola-app-backup-local" -> null
      - bucket_domain_name          = "hyperbola-app-backup-local.s3.amazonaws.com" -> null
      - bucket_regional_domain_name = "hyperbola-app-backup-local.s3.amazonaws.com" -> null
      - hosted_zone_id              = "Z3AQBSTGFYJSTF" -> null
      - id                          = "hyperbola-app-backup-local" -> null
      - region                      = "us-east-1" -> null
      - request_payer               = "BucketOwner" -> null
      - tags                        = {
          - "Environment" = "local"
        } -> null

      - versioning {
          - enabled    = false -> null
          - mfa_delete = false -> null
        }
    }

  # module.base.aws_s3_bucket.media will be destroyed
  - resource "aws_s3_bucket" "media" {
      - arn                         = "arn:aws:s3:::local.hyperbolausercontent.net" -> null
      - bucket                      = "local.hyperbolausercontent.net" -> null
      - bucket_domain_name          = "local.hyperbolausercontent.net.s3.amazonaws.com" -> null
      - bucket_regional_domain_name = "local.hyperbolausercontent.net.s3.amazonaws.com" -> null
      - hosted_zone_id              = "Z3AQBSTGFYJSTF" -> null
      - id                          = "local.hyperbolausercontent.net" -> null
      - region                      = "us-east-1" -> null
      - request_payer               = "BucketOwner" -> null
      - tags                        = {
          - "Environment" = "local"
          - "Name"        = "hyperbola-app media files for local"
        } -> null

      - versioning {
          - enabled    = true -> null
          - mfa_delete = false -> null
        }
    }

Plan: 0 to add, 0 to change, 2 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

module.base.aws_s3_bucket.backup: Destroying... [id=hyperbola-app-backup-local]
module.base.aws_s3_bucket.media: Destroying... [id=local.hyperbolausercontent.net]
module.base.aws_s3_bucket.backup: Destruction complete after 0s

Error: error deleting S3 Bucket (local.hyperbolausercontent.net): BucketNotEmpty: The bucket you tried to delete is not empty. You must delete all versions in the bucket.
	status code: 409, request id: DF79D1420F710629, host id: V9aFJ/HzqQ+iT4U5EHqFpHK6vNqN6iKOmuI1n6KGE3NKJeHVxJvvPXwKKegF7DsYQbZ2meggMHc=


Releasing state lock. This may take a few moments...
```

### Take 2

After deleting all versions in `local.hyperbolausercontent.net`.

```console
$ /usr/local/opt/terraform@0.12/bin/terraform destroy
module.base.data.aws_acm_certificate.cdn: Refreshing state...
data.aws_route53_zone.dc: Refreshing state...
module.base.data.aws_route53_zone.hyperbolausercontent: Refreshing state...
module.base.data.aws_iam_policy_document.assume: Refreshing state...
module.base.aws_s3_bucket.media: Refreshing state... [id=local.hyperbolausercontent.net]
data.aws_iam_policy_document.lb: Refreshing state...

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # module.base.aws_s3_bucket.media will be destroyed
  - resource "aws_s3_bucket" "media" {
      - arn                         = "arn:aws:s3:::local.hyperbolausercontent.net" -> null
      - bucket                      = "local.hyperbolausercontent.net" -> null
      - bucket_domain_name          = "local.hyperbolausercontent.net.s3.amazonaws.com" -> null
      - bucket_regional_domain_name = "local.hyperbolausercontent.net.s3.amazonaws.com" -> null
      - hosted_zone_id              = "Z3AQBSTGFYJSTF" -> null
      - id                          = "local.hyperbolausercontent.net" -> null
      - region                      = "us-east-1" -> null
      - request_payer               = "BucketOwner" -> null
      - tags                        = {
          - "Environment" = "local"
          - "Name"        = "hyperbola-app media files for local"
        } -> null

      - versioning {
          - enabled    = true -> null
          - mfa_delete = false -> null
        }
    }

Plan: 0 to add, 0 to change, 1 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

module.base.aws_s3_bucket.media: Destroying... [id=local.hyperbolausercontent.net]
module.base.aws_s3_bucket.media: Destruction complete after 1s

Destroy complete! Resources: 1 destroyed.
Releasing state lock. This may take a few moments...
```
