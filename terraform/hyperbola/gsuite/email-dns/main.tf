variable "zone_id" {}
variable "zone_name" {}
variable "google_site_verifcation_keys" {} # csv
variable "dkim" {}

# G Suite MX record values: https://support.google.com/a/answer/174125?hl=en
# G Suite TXT record values: https://support.google.com/a/answer/2716802?hl=en

resource "aws_route53_record" "mx-records" {
  zone_id = "${var.zone_id}"
  name    = "${var.zone_name}"
  type    = "MX"
  ttl     = "300"

  records = [
    "1 ASPMX.L.GOOGLE.COM.",
    "5 ALT1.ASPMX.L.GOOGLE.COM.",
    "5 ALT2.ASPMX.L.GOOGLE.COM.",
    "10 ALT3.ASPMX.L.GOOGLE.COM.",
    "10 ALT4.ASPMX.L.GOOGLE.COM.",
  ]
}

resource "aws_route53_record" "root-txt-records" {
  zone_id = "${var.zone_id}"
  name    = "${var.zone_name}"
  type    = "TXT"
  ttl     = "300"

  records = "${concat(list("v=spf1 include:_spf.google.com ~all"), formatlist("google-site-verification=%s", split(",", var.google_site_verifcation_keys)))}"
}

resource "aws_route53_record" "dkim-txt-record" {
  zone_id = "${var.zone_id}"
  name    = "google._domainkey"
  type    = "TXT"
  ttl     = "300"

  records = [
    "v=DKIM1; k=rsa;\" \"${replace(var.dkim, "/(.{254})/", "$1\" \"")}",
  ]
}
