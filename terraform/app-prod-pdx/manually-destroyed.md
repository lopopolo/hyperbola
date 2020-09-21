## DNS

### Forget

```shell
/usr/local/opt/terraform@0.12/bin/terraform state rm aws_route53_record.hyperbo_la_A
/usr/local/opt/terraform@0.12/bin/terraform state rm aws_route53_record.hyperbo_la_AAAA
/usr/local/opt/terraform@0.12/bin/terraform state rm aws_route53_record.www_hyperbo_la_A
/usr/local/opt/terraform@0.12/bin/terraform state rm aws_route53_record.www_hyperbo_la_AAAA
```

### Resources

The AAAA records were already destroyed when cutting over to GitHub Pages.

```
# aws_route53_record.hyperbo_la_A will be destroyed
- resource "aws_route53_record" "hyperbo_la_A" {
    - allow_overwrite = true -> null
    - fqdn            = "hyperbo.la" -> null
    - id              = "Z9AG7AEGFABVK_hyperbo.la_A" -> null
    - name            = "hyperbo.la" -> null
    - records         = [
        - "185.199.108.153",
        - "185.199.109.153",
        - "185.199.110.153",
        - "185.199.111.153",
      ] -> null
    - ttl             = 300 -> null
    - type            = "A" -> null
    - zone_id         = "Z9AG7AEGFABVK" -> null

    - alias {
        - evaluate_target_health = true -> null
        - name                   = "applb-20171106080744451200000003-922647741.us-west-2.elb.amazonaws.com" -> null
        - zone_id                = "Z1H1FL5HABSF5" -> null
      }
  }

# aws_route53_record.www_hyperbo_la_A will be destroyed
- resource "aws_route53_record" "www_hyperbo_la_A" {
    - allow_overwrite = true -> null
    - fqdn            = "www.hyperbo.la" -> null
    - id              = "Z9AG7AEGFABVK_www_A" -> null
    - name            = "www" -> null
    - records         = [
        - "185.199.108.153",
        - "185.199.109.153",
        - "185.199.110.153",
        - "185.199.111.153",
      ] -> null
    - ttl             = 300 -> null
    - type            = "A" -> null
    - zone_id         = "Z9AG7AEGFABVK" -> null

    - alias {
        - evaluate_target_health = true -> null
        - name                   = "applb-20171106080744451200000003-922647741.us-west-2.elb.amazonaws.com" -> null
        - zone_id                = "Z1H1FL5HABSF5" -> null
      }
  }
```

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
    - arn                         = "arn:aws:s3:::www.hyperbolausercontent.net" -> null
    - bucket                      = "www.hyperbolausercontent.net" -> null
    - bucket_domain_name          = "www.hyperbolausercontent.net.s3.amazonaws.com" -> null
    - bucket_regional_domain_name = "www.hyperbolausercontent.net.s3.us-west-2.amazonaws.com" -> null
    - force_destroy               = false -> null
    - hosted_zone_id              = "Z3BJ6K6RIION7M" -> null
    - id                          = "www.hyperbolausercontent.net" -> null
    - region                      = "us-west-2" -> null
    - request_payer               = "BucketOwner" -> null
    - tags                        = {
        - "Environment" = "production"
        - "Name"        = "hyperbola-app media files for production"
      } -> null

    - versioning {
        - enabled    = true -> null
        - mfa_delete = false -> null
      }
  }
```

### Result

This bucket is kept, with ownership transferred to a legacy module in `hyperbola-static`.

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
    - arn                         = "arn:aws:s3:::hyperbola-app-backup-production" -> null
    - bucket                      = "hyperbola-app-backup-production" -> null
    - bucket_domain_name          = "hyperbola-app-backup-production.s3.amazonaws.com" -> null
    - bucket_regional_domain_name = "hyperbola-app-backup-production.s3.us-west-2.amazonaws.com" -> null
    - force_destroy               = false -> null
    - hosted_zone_id              = "Z3BJ6K6RIION7M" -> null
    - id                          = "hyperbola-app-backup-production" -> null
    - region                      = "us-west-2" -> null
    - request_payer               = "BucketOwner" -> null
    - tags                        = {
        - "Environment" = "production"
      } -> null

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }
```

### Result

This bucket is kept, with ownership transferred to a legacy module in `hyperbola-static`.

## `terraform destroy`

