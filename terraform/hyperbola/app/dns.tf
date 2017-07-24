variable "ipv4_address" {}
variable "ipv6_address" {}

variable "host" {
  description = "host the wiki runs on"
  type        = "string"
  default     = "hyperbola3"
}

resource "cloudflare_record" "hyperbo_la" {
  domain  = "hyperbo.la"
  name    = "hyperbo.la"
  value   = "applb-00ba465879944ffeffaef3492c-1690299172.us-west-2.elb.amazonaws.com"
  type    = "CNAME"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "www_hyperbo_la" {
  domain  = "hyperbo.la"
  name    = "www"
  value   = "applb-00ba465879944ffeffaef3492c-1690299172.us-west-2.elb.amazonaws.com"
  type    = "CNAME"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "staging_hyperbo_la_A" {
  domain  = "hyperbo.la"
  name    = "staging"
  value   = "${var.ipv4_address}"
  type    = "A"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "staging_hyperbo_la_AAAA" {
  domain  = "hyperbo.la"
  name    = "staging"
  value   = "${var.ipv6_address}"
  type    = "AAAA"
  ttl     = 1
  proxied = false
}

data "aws_route53_zone" "linode-dc" {
  name         = "linode.hyperboladc.net."
  private_zone = false
}

resource "aws_route53_record" "dc-linode" {
  zone_id = "${data.aws_route53_zone.linode-dc.zone_id}"
  name    = "${var.host}"
  type    = "A"
  ttl     = "300"
  records = ["${var.ipv4_address}"]
}
