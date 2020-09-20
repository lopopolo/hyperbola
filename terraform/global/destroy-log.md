## `terraform destroy`

### Plan

```console
$ /usr/local/opt/terraform@0.12/bin/terraform plan -destroy -no-color
Refreshing Terraform state in-memory prior to plan...
The refreshed state will be used to calculate this plan, but will not be
persisted to local or remote state storage.

aws_route53_zone.hyperbolausercontent: Refreshing state... [id=Z25GE9A9NRUR2N]
aws_route53_zone.hyperboladc: Refreshing state... [id=Z15RBHRN263T6P]
data.aws_iam_policy_document.admin: Refreshing state...
module.hyperbolausercontent_email_dns.aws_route53_record.txt: Refreshing state... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_TXT]
module.hyperbolausercontent_email_dns.aws_route53_record.dkim: Refreshing state... [id=Z25GE9A9NRUR2N_google._domainkey_TXT]
module.hyperbolausercontent_email_dns.aws_route53_record.mx: Refreshing state... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_MX]
module.hyperboladc_email_dns.aws_route53_record.dkim: Refreshing state... [id=Z15RBHRN263T6P_google._domainkey_TXT]
module.hyperboladc_email_dns.aws_route53_record.txt: Refreshing state... [id=Z15RBHRN263T6P_hyperboladc.net_TXT]
module.hyperboladc_email_dns.aws_route53_record.mx: Refreshing state... [id=Z15RBHRN263T6P_hyperboladc.net_MX]

------------------------------------------------------------------------

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_route53_zone.hyperboladc will be destroyed
  - resource "aws_route53_zone" "hyperboladc" {
      - comment       = "HostedZone created by Route53 Registrar" -> null
      - force_destroy = false -> null
      - id            = "Z15RBHRN263T6P" -> null
      - name          = "hyperboladc.net." -> null
      - name_servers  = [
          - "ns-1089.awsdns-08.org",
          - "ns-1773.awsdns-29.co.uk",
          - "ns-199.awsdns-24.com",
          - "ns-564.awsdns-06.net",
        ] -> null
      - tags          = {} -> null
      - zone_id       = "Z15RBHRN263T6P" -> null
    }

  # aws_route53_zone.hyperbolausercontent will be destroyed
  - resource "aws_route53_zone" "hyperbolausercontent" {
      - comment       = "HostedZone created by Route53 Registrar" -> null
      - force_destroy = false -> null
      - id            = "Z25GE9A9NRUR2N" -> null
      - name          = "hyperbolausercontent.net." -> null
      - name_servers  = [
          - "ns-1019.awsdns-63.net",
          - "ns-1159.awsdns-16.org",
          - "ns-1778.awsdns-30.co.uk",
          - "ns-187.awsdns-23.com",
        ] -> null
      - tags          = {} -> null
      - zone_id       = "Z25GE9A9NRUR2N" -> null
    }

  # module.hyperboladc_email_dns.aws_route53_record.dkim will be destroyed
  - resource "aws_route53_record" "dkim" {
      - allow_overwrite = true -> null
      - fqdn            = "google._domainkey.hyperboladc.net" -> null
      - id              = "Z15RBHRN263T6P_google._domainkey_TXT" -> null
      - name            = "google._domainkey" -> null
      - records         = [
          - "v=DKIM1; k=rsa;\" \"p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgw9GWNAV7pI++w0j2kBrSkZbU9+v0cULWem5c1n2AavdmSp+JP0WNXww3bi72pxI2Vrq0iTlmSVxERCLMhnHx1jHEg+iz/JsngVF9ShSYHfs0oz89hVGzA9nX/pC+DH0r066BHtB5DiTcH5MHLLcMjJMjHbw6C/LnAygUMac4pGPlaj56V+TTZpr/dEm5zkzhb+i500SROmnwAy5\" \"CsCymPXE3jcoOLeCh1MkJGZgH7hxgBxusii3Z1jvtVHodRWXp7P2UYmHJTCWtTpCribewkRluRGsNao5Ssxtql+16PqNJzY/VpeW1G9Qv77KS9iBZvQpCXALAZnfU637UoNKxwIDAQAB",
        ] -> null
      - ttl             = 300 -> null
      - type            = "TXT" -> null
      - zone_id         = "Z15RBHRN263T6P" -> null
    }

  # module.hyperboladc_email_dns.aws_route53_record.mx will be destroyed
  - resource "aws_route53_record" "mx" {
      - allow_overwrite = true -> null
      - fqdn            = "hyperboladc.net" -> null
      - id              = "Z15RBHRN263T6P_hyperboladc.net_MX" -> null
      - name            = "hyperboladc.net" -> null
      - records         = [
          - "1 ASPMX.L.GOOGLE.COM.",
          - "10 ALT3.ASPMX.L.GOOGLE.COM.",
          - "10 ALT4.ASPMX.L.GOOGLE.COM.",
          - "5 ALT1.ASPMX.L.GOOGLE.COM.",
          - "5 ALT2.ASPMX.L.GOOGLE.COM.",
        ] -> null
      - ttl             = 300 -> null
      - type            = "MX" -> null
      - zone_id         = "Z15RBHRN263T6P" -> null
    }

  # module.hyperboladc_email_dns.aws_route53_record.txt will be destroyed
  - resource "aws_route53_record" "txt" {
      - allow_overwrite = true -> null
      - fqdn            = "hyperboladc.net" -> null
      - id              = "Z15RBHRN263T6P_hyperboladc.net_TXT" -> null
      - name            = "hyperboladc.net" -> null
      - records         = [
          - "google-site-verification=MBJltQtisR_DfhKzGfjs4mjMRpPK-1nRugHrza1elAA",
          - "v=spf1 include:_spf.google.com ~all",
        ] -> null
      - ttl             = 300 -> null
      - type            = "TXT" -> null
      - zone_id         = "Z15RBHRN263T6P" -> null
    }

  # module.hyperbolausercontent_email_dns.aws_route53_record.dkim will be destroyed
  - resource "aws_route53_record" "dkim" {
      - allow_overwrite = true -> null
      - fqdn            = "google._domainkey.hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_google._domainkey_TXT" -> null
      - name            = "google._domainkey" -> null
      - records         = [
          - "v=DKIM1; k=rsa;\" \"p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm4qyzPNyrtbwcK/VmQn5a1lyW9pvE3Y5caL55A2Bg72goVGjGbGHmWrNW8dJJi/JSxWUJoyglSN9s3Ms1XjbBnzC9f3N/8CyRUtgZRAGuJCkrFOSdT4rZdjMp3UMottDDNtc6ziW6YRtQFHZ4b7IDFjs7tcupaM9LIVB4BKvMM5AwA9079gKRB7+vOOnNClq6qzVtnC8ttS9rcRY\" \"S7/rAambbT4/70MfEuTXpOCoV/TlUfFsP4Jsn85SXRKYUyL2Umk6fxwjKkzb3O7PI4/nQ/cn8lH0FJiAAhlaRSFkVZHMZr/XDlqdJw41VYzUuaDf0e9mpyCHXgTlvtQht0JJ/wIDAQAB",
        ] -> null
      - ttl             = 300 -> null
      - type            = "TXT" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null
    }

  # module.hyperbolausercontent_email_dns.aws_route53_record.mx will be destroyed
  - resource "aws_route53_record" "mx" {
      - allow_overwrite = true -> null
      - fqdn            = "hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_hyperbolausercontent.net_MX" -> null
      - name            = "hyperbolausercontent.net" -> null
      - records         = [
          - "1 ASPMX.L.GOOGLE.COM.",
          - "10 ALT3.ASPMX.L.GOOGLE.COM.",
          - "10 ALT4.ASPMX.L.GOOGLE.COM.",
          - "5 ALT1.ASPMX.L.GOOGLE.COM.",
          - "5 ALT2.ASPMX.L.GOOGLE.COM.",
        ] -> null
      - ttl             = 300 -> null
      - type            = "MX" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null
    }

  # module.hyperbolausercontent_email_dns.aws_route53_record.txt will be destroyed
  - resource "aws_route53_record" "txt" {
      - allow_overwrite = true -> null
      - fqdn            = "hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_hyperbolausercontent.net_TXT" -> null
      - name            = "hyperbolausercontent.net" -> null
      - records         = [
          - "google-site-verification=BAsDzAuut0wmAAA4v5iVIiTCWFYu0gLTvkK_sRk5O8Y",
          - "v=spf1 include:_spf.google.com ~all",
        ] -> null
      - ttl             = 300 -> null
      - type            = "TXT" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null
    }

Plan: 0 to add, 0 to change, 8 to destroy.

------------------------------------------------------------------------

Note: You didn't specify an "-out" parameter to save this plan, so Terraform
can't guarantee that exactly these actions will be performed if
"terraform apply" is subsequently run.

Releasing state lock. This may take a few moments...
```

### Destroy

```console
$ /usr/local/opt/terraform@0.12/bin/terraform destroy
aws_route53_zone.hyperboladc: Refreshing state... [id=Z15RBHRN263T6P]
aws_route53_zone.hyperbolausercontent: Refreshing state... [id=Z25GE9A9NRUR2N]
data.aws_iam_policy_document.admin: Refreshing state...
module.hyperbolausercontent_email_dns.aws_route53_record.mx: Refreshing state... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_MX]
module.hyperbolausercontent_email_dns.aws_route53_record.txt: Refreshing state... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_TXT]
module.hyperbolausercontent_email_dns.aws_route53_record.dkim: Refreshing state... [id=Z25GE9A9NRUR2N_google._domainkey_TXT]
module.hyperboladc_email_dns.aws_route53_record.txt: Refreshing state... [id=Z15RBHRN263T6P_hyperboladc.net_TXT]
module.hyperboladc_email_dns.aws_route53_record.dkim: Refreshing state... [id=Z15RBHRN263T6P_google._domainkey_TXT]
module.hyperboladc_email_dns.aws_route53_record.mx: Refreshing state... [id=Z15RBHRN263T6P_hyperboladc.net_MX]

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_route53_zone.hyperboladc will be destroyed
  - resource "aws_route53_zone" "hyperboladc" {
      - comment       = "HostedZone created by Route53 Registrar" -> null
      - force_destroy = false -> null
      - id            = "Z15RBHRN263T6P" -> null
      - name          = "hyperboladc.net." -> null
      - name_servers  = [
          - "ns-1089.awsdns-08.org",
          - "ns-1773.awsdns-29.co.uk",
          - "ns-199.awsdns-24.com",
          - "ns-564.awsdns-06.net",
        ] -> null
      - tags          = {} -> null
      - zone_id       = "Z15RBHRN263T6P" -> null
    }

  # aws_route53_zone.hyperbolausercontent will be destroyed
  - resource "aws_route53_zone" "hyperbolausercontent" {
      - comment       = "HostedZone created by Route53 Registrar" -> null
      - force_destroy = false -> null
      - id            = "Z25GE9A9NRUR2N" -> null
      - name          = "hyperbolausercontent.net." -> null
      - name_servers  = [
          - "ns-1019.awsdns-63.net",
          - "ns-1159.awsdns-16.org",
          - "ns-1778.awsdns-30.co.uk",
          - "ns-187.awsdns-23.com",
        ] -> null
      - tags          = {} -> null
      - zone_id       = "Z25GE9A9NRUR2N" -> null
    }

  # module.hyperboladc_email_dns.aws_route53_record.dkim will be destroyed
  - resource "aws_route53_record" "dkim" {
      - allow_overwrite = true -> null
      - fqdn            = "google._domainkey.hyperboladc.net" -> null
      - id              = "Z15RBHRN263T6P_google._domainkey_TXT" -> null
      - name            = "google._domainkey" -> null
      - records         = [
          - "v=DKIM1; k=rsa;\" \"p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgw9GWNAV7pI++w0j2kBrSkZbU9+v0cULWem5c1n2AavdmSp+JP0WNXww3bi72pxI2Vrq0iTlmSVxERCLMhnHx1jHEg+iz/JsngVF9ShSYHfs0oz89hVGzA9nX/pC+DH0r066BHtB5DiTcH5MHLLcMjJMjHbw6C/LnAygUMac4pGPlaj56V+TTZpr/dEm5zkzhb+i500SROmnwAy5\" \"CsCymPXE3jcoOLeCh1MkJGZgH7hxgBxusii3Z1jvtVHodRWXp7P2UYmHJTCWtTpCribewkRluRGsNao5Ssxtql+16PqNJzY/VpeW1G9Qv77KS9iBZvQpCXALAZnfU637UoNKxwIDAQAB",
        ] -> null
      - ttl             = 300 -> null
      - type            = "TXT" -> null
      - zone_id         = "Z15RBHRN263T6P" -> null
    }

  # module.hyperboladc_email_dns.aws_route53_record.mx will be destroyed
  - resource "aws_route53_record" "mx" {
      - allow_overwrite = true -> null
      - fqdn            = "hyperboladc.net" -> null
      - id              = "Z15RBHRN263T6P_hyperboladc.net_MX" -> null
      - name            = "hyperboladc.net" -> null
      - records         = [
          - "1 ASPMX.L.GOOGLE.COM.",
          - "10 ALT3.ASPMX.L.GOOGLE.COM.",
          - "10 ALT4.ASPMX.L.GOOGLE.COM.",
          - "5 ALT1.ASPMX.L.GOOGLE.COM.",
          - "5 ALT2.ASPMX.L.GOOGLE.COM.",
        ] -> null
      - ttl             = 300 -> null
      - type            = "MX" -> null
      - zone_id         = "Z15RBHRN263T6P" -> null
    }

  # module.hyperboladc_email_dns.aws_route53_record.txt will be destroyed
  - resource "aws_route53_record" "txt" {
      - allow_overwrite = true -> null
      - fqdn            = "hyperboladc.net" -> null
      - id              = "Z15RBHRN263T6P_hyperboladc.net_TXT" -> null
      - name            = "hyperboladc.net" -> null
      - records         = [
          - "google-site-verification=MBJltQtisR_DfhKzGfjs4mjMRpPK-1nRugHrza1elAA",
          - "v=spf1 include:_spf.google.com ~all",
        ] -> null
      - ttl             = 300 -> null
      - type            = "TXT" -> null
      - zone_id         = "Z15RBHRN263T6P" -> null
    }

  # module.hyperbolausercontent_email_dns.aws_route53_record.dkim will be destroyed
  - resource "aws_route53_record" "dkim" {
      - allow_overwrite = true -> null
      - fqdn            = "google._domainkey.hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_google._domainkey_TXT" -> null
      - name            = "google._domainkey" -> null
      - records         = [
          - "v=DKIM1; k=rsa;\" \"p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm4qyzPNyrtbwcK/VmQn5a1lyW9pvE3Y5caL55A2Bg72goVGjGbGHmWrNW8dJJi/JSxWUJoyglSN9s3Ms1XjbBnzC9f3N/8CyRUtgZRAGuJCkrFOSdT4rZdjMp3UMottDDNtc6ziW6YRtQFHZ4b7IDFjs7tcupaM9LIVB4BKvMM5AwA9079gKRB7+vOOnNClq6qzVtnC8ttS9rcRY\" \"S7/rAambbT4/70MfEuTXpOCoV/TlUfFsP4Jsn85SXRKYUyL2Umk6fxwjKkzb3O7PI4/nQ/cn8lH0FJiAAhlaRSFkVZHMZr/XDlqdJw41VYzUuaDf0e9mpyCHXgTlvtQht0JJ/wIDAQAB",
        ] -> null
      - ttl             = 300 -> null
      - type            = "TXT" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null
    }

  # module.hyperbolausercontent_email_dns.aws_route53_record.mx will be destroyed
  - resource "aws_route53_record" "mx" {
      - allow_overwrite = true -> null
      - fqdn            = "hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_hyperbolausercontent.net_MX" -> null
      - name            = "hyperbolausercontent.net" -> null
      - records         = [
          - "1 ASPMX.L.GOOGLE.COM.",
          - "10 ALT3.ASPMX.L.GOOGLE.COM.",
          - "10 ALT4.ASPMX.L.GOOGLE.COM.",
          - "5 ALT1.ASPMX.L.GOOGLE.COM.",
          - "5 ALT2.ASPMX.L.GOOGLE.COM.",
        ] -> null
      - ttl             = 300 -> null
      - type            = "MX" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null
    }

  # module.hyperbolausercontent_email_dns.aws_route53_record.txt will be destroyed
  - resource "aws_route53_record" "txt" {
      - allow_overwrite = true -> null
      - fqdn            = "hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_hyperbolausercontent.net_TXT" -> null
      - name            = "hyperbolausercontent.net" -> null
      - records         = [
          - "google-site-verification=BAsDzAuut0wmAAA4v5iVIiTCWFYu0gLTvkK_sRk5O8Y",
          - "v=spf1 include:_spf.google.com ~all",
        ] -> null
      - ttl             = 300 -> null
      - type            = "TXT" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null
    }

Plan: 0 to add, 0 to change, 8 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

module.hyperboladc_email_dns.aws_route53_record.txt: Destroying... [id=Z15RBHRN263T6P_hyperboladc.net_TXT]
module.hyperbolausercontent_email_dns.aws_route53_record.dkim: Destroying... [id=Z25GE9A9NRUR2N_google._domainkey_TXT]
module.hyperbolausercontent_email_dns.aws_route53_record.mx: Destroying... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_MX]
module.hyperboladc_email_dns.aws_route53_record.mx: Destroying... [id=Z15RBHRN263T6P_hyperboladc.net_MX]
module.hyperboladc_email_dns.aws_route53_record.dkim: Destroying... [id=Z15RBHRN263T6P_google._domainkey_TXT]
module.hyperbolausercontent_email_dns.aws_route53_record.txt: Destroying... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_TXT]
module.hyperbolausercontent_email_dns.aws_route53_record.dkim: Still destroying... [id=Z25GE9A9NRUR2N_google._domainkey_TXT, 10s elapsed]
module.hyperboladc_email_dns.aws_route53_record.mx: Still destroying... [id=Z15RBHRN263T6P_hyperboladc.net_MX, 10s elapsed]
module.hyperboladc_email_dns.aws_route53_record.txt: Still destroying... [id=Z15RBHRN263T6P_hyperboladc.net_TXT, 10s elapsed]
module.hyperbolausercontent_email_dns.aws_route53_record.mx: Still destroying... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_MX, 10s elapsed]
module.hyperboladc_email_dns.aws_route53_record.dkim: Still destroying... [id=Z15RBHRN263T6P_google._domainkey_TXT, 10s elapsed]
module.hyperbolausercontent_email_dns.aws_route53_record.txt: Still destroying... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_TXT, 10s elapsed]
module.hyperbolausercontent_email_dns.aws_route53_record.txt: Still destroying... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_TXT, 20s elapsed]
module.hyperboladc_email_dns.aws_route53_record.dkim: Still destroying... [id=Z15RBHRN263T6P_google._domainkey_TXT, 20s elapsed]
module.hyperbolausercontent_email_dns.aws_route53_record.dkim: Still destroying... [id=Z25GE9A9NRUR2N_google._domainkey_TXT, 20s elapsed]
module.hyperbolausercontent_email_dns.aws_route53_record.mx: Still destroying... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_MX, 20s elapsed]
module.hyperboladc_email_dns.aws_route53_record.txt: Still destroying... [id=Z15RBHRN263T6P_hyperboladc.net_TXT, 20s elapsed]
module.hyperboladc_email_dns.aws_route53_record.mx: Still destroying... [id=Z15RBHRN263T6P_hyperboladc.net_MX, 20s elapsed]
module.hyperbolausercontent_email_dns.aws_route53_record.txt: Still destroying... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_TXT, 30s elapsed]
module.hyperboladc_email_dns.aws_route53_record.txt: Still destroying... [id=Z15RBHRN263T6P_hyperboladc.net_TXT, 30s elapsed]
module.hyperbolausercontent_email_dns.aws_route53_record.mx: Still destroying... [id=Z25GE9A9NRUR2N_hyperbolausercontent.net_MX, 30s elapsed]
module.hyperbolausercontent_email_dns.aws_route53_record.dkim: Still destroying... [id=Z25GE9A9NRUR2N_google._domainkey_TXT, 30s elapsed]
module.hyperboladc_email_dns.aws_route53_record.mx: Still destroying... [id=Z15RBHRN263T6P_hyperboladc.net_MX, 30s elapsed]
module.hyperboladc_email_dns.aws_route53_record.dkim: Still destroying... [id=Z15RBHRN263T6P_google._domainkey_TXT, 30s elapsed]
module.hyperbolausercontent_email_dns.aws_route53_record.dkim: Destruction complete after 32s
module.hyperbolausercontent_email_dns.aws_route53_record.txt: Destruction complete after 32s
module.hyperbolausercontent_email_dns.aws_route53_record.mx: Destruction complete after 32s
aws_route53_zone.hyperbolausercontent: Destroying... [id=Z25GE9A9NRUR2N]
module.hyperboladc_email_dns.aws_route53_record.dkim: Destruction complete after 32s
module.hyperboladc_email_dns.aws_route53_record.txt: Destruction complete after 32s
aws_route53_zone.hyperbolausercontent: Destruction complete after 0s
module.hyperboladc_email_dns.aws_route53_record.mx: Destruction complete after 38s
aws_route53_zone.hyperboladc: Destroying... [id=Z15RBHRN263T6P]
aws_route53_zone.hyperboladc: Destruction complete after 1s

Destroy complete! Resources: 8 destroyed.
Releasing state lock. This may take a few moments...
```
