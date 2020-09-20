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
