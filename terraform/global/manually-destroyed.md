## IAM

### Forget

```console
$ /usr/local/opt/terraform@0.12/bin/terraform state rm module.iam_admin
Removed module.iam_admin.aws_iam_access_key.key[0]
Removed module.iam_admin.aws_iam_group.group
Removed module.iam_admin.aws_iam_group_membership.membership
Removed module.iam_admin.aws_iam_group_policy.policy
Removed module.iam_admin.aws_iam_user.user[0]
Successfully removed 5 resource instance(s).
Releasing state lock. This may take a few moments...
```

## IAM AWS Account

### Forget

```console
$ /usr/local/opt/terraform@0.12/bin/terraform state rm aws_iam_account_password_policy.this
Removed aws_iam_account_password_policy.this
Successfully removed 1 resource instance(s).
Releasing state lock. This may take a few moments..
$ /usr/local/opt/terraform@0.12/bin/terraform state rm aws_iam_account_alias.this
Removed aws_iam_account_alias.this
Successfully removed 1 resource instance(s).
Releasing state lock. This may take a few moments...
```

## Route53 hyperbo.la zone

### Forget

```console
/usr/local/opt/terraform@0.12/bin/terraform state rm aws_route53_zone.hyperbola
Removed aws_route53_zone.hyperbola
Successfully removed 1 resource instance(s).
Releasing state lock. This may take a few moments...
```

## Route53 hyperbo.la email

### Forget

```console
$ /usr/local/opt/terraform@0.12/bin/terraform state rm module.hyperbola_email_dns
Removed module.hyperbola_email_dns.aws_route53_record.dkim
Removed module.hyperbola_email_dns.aws_route53_record.mx
Removed module.hyperbola_email_dns.aws_route53_record.txt
Successfully removed 3 resource instance(s).
Releasing state lock. This may take a few moments...
```
