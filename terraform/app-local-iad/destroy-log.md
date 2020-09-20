## `terraform destroy`

```console
$ /usr/local/opt/terraform@0.12/bin/terraform destroy
module.base.data.aws_acm_certificate.cdn: Refreshing state...
module.iam_r53.aws_iam_group.group: Refreshing state... [id=local-route53]
module.iam_r53.aws_iam_user.user[0]: Refreshing state... [id=local-lb]
module.base.data.aws_route53_zone.hyperbolausercontent: Refreshing state...
module.secrets.aws_ssm_parameter.database_password: Refreshing state... [id=/app/local/DB_PASSWORD]
module.iam_vagrant.aws_iam_group.group: Refreshing state... [id=local-app-s3]
data.aws_route53_zone.dc: Refreshing state...
module.base.data.aws_iam_policy_document.assume: Refreshing state...
module.secrets.aws_ssm_parameter.secret_key: Refreshing state... [id=/app/local/SECRET_KEY]
module.iam_vagrant.aws_iam_user.user[0]: Refreshing state... [id=local-app]
module.base.aws_iam_role.app: Refreshing state... [id=app-role-00285de333c0953e987c9dabac]
module.iam_vagrant.aws_iam_group_membership.membership: Refreshing state... [id=local-app-s3]
module.iam_vagrant.aws_iam_access_key.key[0]: Refreshing state... [id=AKIAJQJF3OYS6FIDIKJA]
module.base.aws_iam_instance_profile.app: Refreshing state... [id=app-profile-00285de333c0953e987c9dabad]
module.base.aws_iam_role_policy.app: Refreshing state... [id=app-role-00285de333c0953e987c9dabac:app-policy-00285de333c0953e987c9dabae]
module.iam_r53.aws_iam_access_key.key[0]: Refreshing state... [id=AKIAINBWRVVPFO6QTMIA]
module.iam_r53.aws_iam_group_membership.membership: Refreshing state... [id=local-route53]
module.iam_vagrant.aws_iam_group_policy.policy: Refreshing state... [id=local-app-s3:local-app-s3]
module.base.aws_cloudfront_distribution.cdn: Refreshing state... [id=E1SBU01V6U4TA3]
aws_route53_record.app-local: Refreshing state... [id=Z15RBHRN263T6P_app-local_A]
aws_route53_record.lb-local: Refreshing state... [id=Z15RBHRN263T6P_lb-local_A]
data.aws_iam_policy_document.lb: Refreshing state...
module.iam_r53.aws_iam_group_policy.policy: Refreshing state... [id=local-route53:local-route53]
module.base.aws_route53_record.cdn-A: Refreshing state... [id=Z25GE9A9NRUR2N_local_A]
module.base.aws_route53_record.cdn-AAAA: Refreshing state... [id=Z25GE9A9NRUR2N_local_AAAA]
aws_route53_record.local: Refreshing state... [id=Z15RBHRN263T6P_local_CNAME]

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_route53_record.app-local will be destroyed
  - resource "aws_route53_record" "app-local" {
      - allow_overwrite = true -> null
      - fqdn            = "app-local.hyperboladc.net" -> null
      - id              = "Z15RBHRN263T6P_app-local_A" -> null
      - name            = "app-local" -> null
      - records         = [
          - "192.168.10.20",
        ] -> null
      - ttl             = 300 -> null
      - type            = "A" -> null
      - zone_id         = "Z15RBHRN263T6P" -> null
    }

  # aws_route53_record.lb-local will be destroyed
  - resource "aws_route53_record" "lb-local" {
      - allow_overwrite = true -> null
      - fqdn            = "lb-local.hyperboladc.net" -> null
      - id              = "Z15RBHRN263T6P_lb-local_A" -> null
      - name            = "lb-local" -> null
      - records         = [
          - "192.168.10.40",
        ] -> null
      - ttl             = 300 -> null
      - type            = "A" -> null
      - zone_id         = "Z15RBHRN263T6P" -> null
    }

  # aws_route53_record.local will be destroyed
  - resource "aws_route53_record" "local" {
      - allow_overwrite = true -> null
      - fqdn            = "local.hyperboladc.net" -> null
      - id              = "Z15RBHRN263T6P_local_CNAME" -> null
      - name            = "local" -> null
      - records         = [
          - "lb-local.hyperboladc.net",
        ] -> null
      - ttl             = 300 -> null
      - type            = "CNAME" -> null
      - zone_id         = "Z15RBHRN263T6P" -> null
    }

  # module.base.aws_cloudfront_distribution.cdn will be destroyed
  - resource "aws_cloudfront_distribution" "cdn" {
      - active_trusted_signers         = {
          - "enabled" = "false"
          - "items.#" = "0"
        } -> null
      - aliases                        = [
          - "local.hyperbolausercontent.net",
        ] -> null
      - arn                            = "arn:aws:cloudfront::473124112471:distribution/E1SBU01V6U4TA3" -> null
      - caller_reference               = "2017-07-05T11:30:55.041868358-07:00" -> null
      - comment                        = "CloudFront for hyperbola-app cdn - local" -> null
      - domain_name                    = "d18eoc1x0zcy0f.cloudfront.net" -> null
      - enabled                        = true -> null
      - etag                           = "ERKI3LI3R9RPS" -> null
      - hosted_zone_id                 = "Z2FDTNDATAQYW2" -> null
      - http_version                   = "http2" -> null
      - id                             = "E1SBU01V6U4TA3" -> null
      - in_progress_validation_batches = 0 -> null
      - is_ipv6_enabled                = true -> null
      - last_modified_time             = "2017-11-19 03:53:51.344 +0000 UTC" -> null
      - price_class                    = "PriceClass_100" -> null
      - retain_on_delete               = false -> null
      - status                         = "Deployed" -> null
      - tags                           = {
          - "Environment" = "local"
        } -> null
      - wait_for_deployment            = true -> null

      - default_cache_behavior {
          - allowed_methods        = [
              - "DELETE",
              - "GET",
              - "HEAD",
              - "OPTIONS",
              - "PATCH",
              - "POST",
              - "PUT",
            ] -> null
          - cached_methods         = [
              - "GET",
              - "HEAD",
            ] -> null
          - compress               = false -> null
          - default_ttl            = 3600 -> null
          - max_ttl                = 86400 -> null
          - min_ttl                = 0 -> null
          - smooth_streaming       = false -> null
          - target_origin_id       = "s3-media" -> null
          - trusted_signers        = [] -> null
          - viewer_protocol_policy = "https-only" -> null

          - forwarded_values {
              - headers                 = [] -> null
              - query_string            = false -> null
              - query_string_cache_keys = [] -> null

              - cookies {
                  - forward           = "none" -> null
                  - whitelisted_names = [] -> null
                }
            }
        }

      - origin {
          - domain_name = "local.hyperbolausercontent.net.s3.amazonaws.com" -> null
          - origin_id   = "s3-media" -> null
        }

      - restrictions {
          - geo_restriction {
              - locations        = [] -> null
              - restriction_type = "none" -> null
            }
        }

      - viewer_certificate {
          - acm_certificate_arn            = "arn:aws:acm:us-east-1:473124112471:certificate/ec75af41-df70-41d7-9766-01c71c80f0d3" -> null
          - cloudfront_default_certificate = false -> null
          - minimum_protocol_version       = "TLSv1.2_2018" -> null
          - ssl_support_method             = "sni-only" -> null
        }
    }

  # module.base.aws_iam_instance_profile.app will be destroyed
  - resource "aws_iam_instance_profile" "app" {
      - arn         = "arn:aws:iam::473124112471:instance-profile/app-profile-00285de333c0953e987c9dabad" -> null
      - create_date = "2017-07-25T05:53:32Z" -> null
      - id          = "app-profile-00285de333c0953e987c9dabad" -> null
      - name        = "app-profile-00285de333c0953e987c9dabad" -> null
      - name_prefix = "app-profile-" -> null
      - path        = "/" -> null
      - role        = "app-role-00285de333c0953e987c9dabac" -> null
      - roles       = [
          - "app-role-00285de333c0953e987c9dabac",
        ] -> null
      - unique_id   = "AIPAIBUFEHKT6WADHMTKC" -> null
    }

  # module.base.aws_iam_role.app will be destroyed
  - resource "aws_iam_role" "app" {
      - arn                   = "arn:aws:iam::473124112471:role/app-role-00285de333c0953e987c9dabac" -> null
      - assume_role_policy    = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = "sts:AssumeRole"
                      - Effect    = "Allow"
                      - Principal = {
                          - Service = "ec2.amazonaws.com"
                        }
                      - Sid       = "AppAssumeRole"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - create_date           = "2017-07-25T05:53:31Z" -> null
      - force_detach_policies = false -> null
      - id                    = "app-role-00285de333c0953e987c9dabac" -> null
      - max_session_duration  = 3600 -> null
      - name                  = "app-role-00285de333c0953e987c9dabac" -> null
      - name_prefix           = "app-role-" -> null
      - path                  = "/" -> null
      - tags                  = {} -> null
      - unique_id             = "AROAISJCZJG36HAUMFKYY" -> null
    }

  # module.base.aws_iam_role_policy.app will be destroyed
  - resource "aws_iam_role_policy" "app" {
      - id          = "app-role-00285de333c0953e987c9dabac:app-policy-00285de333c0953e987c9dabae" -> null
      - name        = "app-policy-00285de333c0953e987c9dabae" -> null
      - name_prefix = "app-policy-" -> null
      - policy      = jsonencode(
            {
              - Statement = [
                  - {
                      - Action   = [
                          - "s3:ListBucket",
                          - "s3:GetBucketLocation",
                        ]
                      - Effect   = "Allow"
                      - Resource = [
                          - "arn:aws:s3:::local.hyperbolausercontent.net",
                          - "arn:aws:s3:::hyperbola-app-backup-local",
                        ]
                      - Sid      = "AllowAppBucketPermissions"
                    },
                  - {
                      - Action   = "s3:*Object*"
                      - Effect   = "Allow"
                      - Resource = [
                          - "arn:aws:s3:::local.hyperbolausercontent.net/*",
                          - "arn:aws:s3:::hyperbola-app-backup-local/*",
                        ]
                      - Sid      = "AllowAppBucketContentPermissions"
                    },
                  - {
                      - Action   = [
                          - "ssm:GetParametersByPath",
                        ]
                      - Effect   = "Allow"
                      - Resource = [
                          - "arn:aws:ssm:*:*:parameter/app/local/*",
                        ]
                      - Sid      = "AllowSecretsAccess"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - role        = "app-role-00285de333c0953e987c9dabac" -> null
    }

  # module.base.aws_route53_record.cdn-A will be destroyed
  - resource "aws_route53_record" "cdn-A" {
      - allow_overwrite = true -> null
      - fqdn            = "local.hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_local_A" -> null
      - name            = "local" -> null
      - records         = [] -> null
      - ttl             = 0 -> null
      - type            = "A" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null

      - alias {
          - evaluate_target_health = false -> null
          - name                   = "d18eoc1x0zcy0f.cloudfront.net" -> null
          - zone_id                = "Z2FDTNDATAQYW2" -> null
        }
    }

  # module.base.aws_route53_record.cdn-AAAA will be destroyed
  - resource "aws_route53_record" "cdn-AAAA" {
      - allow_overwrite = true -> null
      - fqdn            = "local.hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_local_AAAA" -> null
      - name            = "local" -> null
      - records         = [] -> null
      - ttl             = 0 -> null
      - type            = "AAAA" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null

      - alias {
          - evaluate_target_health = false -> null
          - name                   = "d18eoc1x0zcy0f.cloudfront.net" -> null
          - zone_id                = "Z2FDTNDATAQYW2" -> null
        }
    }

  # module.iam_r53.aws_iam_access_key.key[0] will be destroyed
  - resource "aws_iam_access_key" "key" {
      - id                = "AKIAINBWRVVPFO6QTMIA" -> null
      - secret            = (sensitive value)
      - ses_smtp_password = (sensitive value)
      - status            = "Active" -> null
      - user              = "local-lb" -> null
    }

  # module.iam_r53.aws_iam_group.group will be destroyed
  - resource "aws_iam_group" "group" {
      - arn       = "arn:aws:iam::473124112471:group/local-route53" -> null
      - id        = "local-route53" -> null
      - name      = "local-route53" -> null
      - path      = "/" -> null
      - unique_id = "AGPAJL5IMULDV6EMJWVSY" -> null
    }

  # module.iam_r53.aws_iam_group_membership.membership will be destroyed
  - resource "aws_iam_group_membership" "membership" {
      - group = "local-route53" -> null
      - id    = "local-route53" -> null
      - name  = "local-route53" -> null
      - users = [
          - "local-lb",
        ] -> null
    }

  # module.iam_r53.aws_iam_group_policy.policy will be destroyed
  - resource "aws_iam_group_policy" "policy" {
      - group  = "local-route53" -> null
      - id     = "local-route53:local-route53" -> null
      - name   = "local-route53" -> null
      - policy = jsonencode(
            {
              - Statement = [
                  - {
                      - Action   = [
                          - "route53:ListHostedZones",
                          - "route53:GetChange",
                        ]
                      - Effect   = "Allow"
                      - Resource = "*"
                      - Sid      = "AllowGlobalRecordSetsPermissions"
                    },
                  - {
                      - Action   = [
                          - "route53:ListResourceRecordSets",
                          - "route53:ChangeResourceRecordSets",
                        ]
                      - Effect   = "Allow"
                      - Resource = "arn:aws:route53:::hostedzone/Z15RBHRN263T6P"
                      - Sid      = "AllowChangePermissions"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
    }

  # module.iam_r53.aws_iam_user.user[0] will be destroyed
  - resource "aws_iam_user" "user" {
      - arn           = "arn:aws:iam::473124112471:user/local-lb" -> null
      - force_destroy = false -> null
      - id            = "local-lb" -> null
      - name          = "local-lb" -> null
      - path          = "/" -> null
      - tags          = {} -> null
      - unique_id     = "AIDAITASK5BHQVEY76I7Q" -> null
    }

  # module.iam_vagrant.aws_iam_access_key.key[0] will be destroyed
  - resource "aws_iam_access_key" "key" {
      - id                = "AKIAJQJF3OYS6FIDIKJA" -> null
      - secret            = (sensitive value)
      - ses_smtp_password = (sensitive value)
      - status            = "Active" -> null
      - user              = "local-app" -> null
    }

  # module.iam_vagrant.aws_iam_group.group will be destroyed
  - resource "aws_iam_group" "group" {
      - arn       = "arn:aws:iam::473124112471:group/local-app-s3" -> null
      - id        = "local-app-s3" -> null
      - name      = "local-app-s3" -> null
      - path      = "/" -> null
      - unique_id = "AGPAJEFCVIDXGIJ4PYFN6" -> null
    }

  # module.iam_vagrant.aws_iam_group_membership.membership will be destroyed
  - resource "aws_iam_group_membership" "membership" {
      - group = "local-app-s3" -> null
      - id    = "local-app-s3" -> null
      - name  = "local-app-s3" -> null
      - users = [
          - "local-app",
        ] -> null
    }

  # module.iam_vagrant.aws_iam_group_policy.policy will be destroyed
  - resource "aws_iam_group_policy" "policy" {
      - group  = "local-app-s3" -> null
      - id     = "local-app-s3:local-app-s3" -> null
      - name   = "local-app-s3" -> null
      - policy = jsonencode(
            {
              - Statement = [
                  - {
                      - Action   = [
                          - "s3:ListBucket",
                          - "s3:GetBucketLocation",
                        ]
                      - Effect   = "Allow"
                      - Resource = [
                          - "arn:aws:s3:::local.hyperbolausercontent.net",
                          - "arn:aws:s3:::hyperbola-app-backup-local",
                        ]
                      - Sid      = "AllowAppBucketPermissions"
                    },
                  - {
                      - Action   = "s3:*Object*"
                      - Effect   = "Allow"
                      - Resource = [
                          - "arn:aws:s3:::local.hyperbolausercontent.net/*",
                          - "arn:aws:s3:::hyperbola-app-backup-local/*",
                        ]
                      - Sid      = "AllowAppBucketContentPermissions"
                    },
                  - {
                      - Action   = "ssm:GetParametersByPath"
                      - Effect   = "Allow"
                      - Resource = "arn:aws:ssm:*:*:parameter/app/local/*"
                      - Sid      = "AllowSecretsAccess"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
    }

  # module.iam_vagrant.aws_iam_user.user[0] will be destroyed
  - resource "aws_iam_user" "user" {
      - arn           = "arn:aws:iam::473124112471:user/local-app" -> null
      - force_destroy = false -> null
      - id            = "local-app" -> null
      - name          = "local-app" -> null
      - path          = "/" -> null
      - tags          = {} -> null
      - unique_id     = "AIDAITNBLJ4CVFCKJ23NS" -> null
    }

  # module.secrets.aws_ssm_parameter.database_password will be destroyed
  - resource "aws_ssm_parameter" "database_password" {
      - arn         = "arn:aws:ssm:us-east-1:473124112471:parameter/app/local/DB_PASSWORD" -> null
      - description = "App database password" -> null
      - id          = "/app/local/DB_PASSWORD" -> null
      - key_id      = "alias/aws/ssm" -> null
      - name        = "/app/local/DB_PASSWORD" -> null
      - tags        = {
          - "Environment" = "local"
          - "Project"     = "app"
        } -> null
      - tier        = "Standard" -> null
      - type        = "SecureString" -> null
      - value       = (sensitive value)
      - version     = 2 -> null
    }

  # module.secrets.aws_ssm_parameter.secret_key will be destroyed
  - resource "aws_ssm_parameter" "secret_key" {
      - arn         = "arn:aws:ssm:us-east-1:473124112471:parameter/app/local/SECRET_KEY" -> null
      - description = "Django secret key" -> null
      - id          = "/app/local/SECRET_KEY" -> null
      - key_id      = "alias/aws/ssm" -> null
      - name        = "/app/local/SECRET_KEY" -> null
      - tags        = {
          - "Environment" = "local"
          - "Project"     = "app"
        } -> null
      - tier        = "Standard" -> null
      - type        = "SecureString" -> null
      - value       = (sensitive value)
      - version     = 1 -> null
    }

Plan: 0 to add, 0 to change, 21 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

module.iam_vagrant.aws_iam_group_policy.policy: Destroying... [id=local-app-s3:local-app-s3]
module.secrets.aws_ssm_parameter.secret_key: Destroying... [id=/app/local/SECRET_KEY]
module.secrets.aws_ssm_parameter.database_password: Destroying... [id=/app/local/DB_PASSWORD]
module.iam_vagrant.aws_iam_group_membership.membership: Destroying... [id=local-app-s3]
module.base.aws_iam_role_policy.app: Destroying... [id=app-role-00285de333c0953e987c9dabac:app-policy-00285de333c0953e987c9dabae]
aws_route53_record.local: Destroying... [id=Z15RBHRN263T6P_local_CNAME]
module.iam_r53.aws_iam_group_membership.membership: Destroying... [id=local-route53]
aws_route53_record.app-local: Destroying... [id=Z15RBHRN263T6P_app-local_A]
module.iam_r53.aws_iam_group_policy.policy: Destroying... [id=local-route53:local-route53]
module.base.aws_route53_record.cdn-A: Destroying... [id=Z25GE9A9NRUR2N_local_A]
module.secrets.aws_ssm_parameter.database_password: Destruction complete after 0s
module.base.aws_iam_instance_profile.app: Destroying... [id=app-profile-00285de333c0953e987c9dabad]
module.secrets.aws_ssm_parameter.secret_key: Destruction complete after 0s
module.iam_r53.aws_iam_group_policy.policy: Destruction complete after 0s
module.iam_vagrant.aws_iam_access_key.key[0]: Destroying... [id=AKIAJQJF3OYS6FIDIKJA]
module.base.aws_route53_record.cdn-AAAA: Destroying... [id=Z25GE9A9NRUR2N_local_AAAA]
module.iam_vagrant.aws_iam_group_policy.policy: Destruction complete after 0s
module.iam_r53.aws_iam_access_key.key[0]: Destroying... [id=AKIAINBWRVVPFO6QTMIA]
module.iam_vagrant.aws_iam_group_membership.membership: Destruction complete after 0s
module.iam_vagrant.aws_iam_group.group: Destroying... [id=local-app-s3]
module.iam_r53.aws_iam_group_membership.membership: Destruction complete after 0s
module.iam_r53.aws_iam_group.group: Destroying... [id=local-route53]
module.iam_vagrant.aws_iam_access_key.key[0]: Destruction complete after 0s
module.iam_vagrant.aws_iam_user.user[0]: Destroying... [id=local-app]
module.iam_vagrant.aws_iam_group.group: Destruction complete after 0s
module.iam_r53.aws_iam_access_key.key[0]: Destruction complete after 0s
module.iam_r53.aws_iam_user.user[0]: Destroying... [id=local-lb]
module.iam_r53.aws_iam_group.group: Destruction complete after 0s
module.base.aws_iam_role_policy.app: Destruction complete after 0s
module.base.aws_iam_instance_profile.app: Destruction complete after 1s
module.base.aws_iam_role.app: Destroying... [id=app-role-00285de333c0953e987c9dabac]
module.iam_r53.aws_iam_user.user[0]: Destruction complete after 1s
module.iam_vagrant.aws_iam_user.user[0]: Destruction complete after 1s
module.base.aws_iam_role.app: Destruction complete after 0s
aws_route53_record.app-local: Still destroying... [id=Z15RBHRN263T6P_app-local_A, 10s elapsed]
aws_route53_record.local: Still destroying... [id=Z15RBHRN263T6P_local_CNAME, 10s elapsed]
module.base.aws_route53_record.cdn-A: Still destroying... [id=Z25GE9A9NRUR2N_local_A, 10s elapsed]
module.base.aws_route53_record.cdn-AAAA: Still destroying... [id=Z25GE9A9NRUR2N_local_AAAA, 10s elapsed]
aws_route53_record.local: Still destroying... [id=Z15RBHRN263T6P_local_CNAME, 20s elapsed]
aws_route53_record.app-local: Still destroying... [id=Z15RBHRN263T6P_app-local_A, 20s elapsed]
module.base.aws_route53_record.cdn-A: Still destroying... [id=Z25GE9A9NRUR2N_local_A, 20s elapsed]
module.base.aws_route53_record.cdn-AAAA: Still destroying... [id=Z25GE9A9NRUR2N_local_AAAA, 20s elapsed]
module.base.aws_route53_record.cdn-A: Still destroying... [id=Z25GE9A9NRUR2N_local_A, 30s elapsed]
aws_route53_record.app-local: Still destroying... [id=Z15RBHRN263T6P_app-local_A, 30s elapsed]
aws_route53_record.local: Still destroying... [id=Z15RBHRN263T6P_local_CNAME, 30s elapsed]
module.base.aws_route53_record.cdn-AAAA: Still destroying... [id=Z25GE9A9NRUR2N_local_AAAA, 30s elapsed]
module.base.aws_route53_record.cdn-A: Destruction complete after 32s
aws_route53_record.local: Destruction complete after 32s
aws_route53_record.lb-local: Destroying... [id=Z15RBHRN263T6P_lb-local_A]
aws_route53_record.app-local: Destruction complete after 32s
module.base.aws_route53_record.cdn-AAAA: Destruction complete after 32s
module.base.aws_cloudfront_distribution.cdn: Destroying... [id=E1SBU01V6U4TA3]
aws_route53_record.lb-local: Still destroying... [id=Z15RBHRN263T6P_lb-local_A, 10s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 10s elapsed]
aws_route53_record.lb-local: Still destroying... [id=Z15RBHRN263T6P_lb-local_A, 20s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 20s elapsed]
aws_route53_record.lb-local: Still destroying... [id=Z15RBHRN263T6P_lb-local_A, 30s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 30s elapsed]
aws_route53_record.lb-local: Destruction complete after 37s
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 40s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 50s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 1m0s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 1m10s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 1m20s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 1m30s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 1m40s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 1m50s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 2m0s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 2m10s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 2m20s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 2m30s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 2m40s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 2m50s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 3m0s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 3m10s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 3m20s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 3m30s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E1SBU01V6U4TA3, 3m40s elapsed]
module.base.aws_cloudfront_distribution.cdn: Destruction complete after 3m43s

Destroy complete! Resources: 21 destroyed.
Releasing state lock. This may take a few moments...
```
