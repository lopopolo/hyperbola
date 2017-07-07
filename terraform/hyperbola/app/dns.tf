variable "ipv4_addresses" {
  description = "hyperbola inventory ipv4 addresses"
  type        = "map"
}

variable "ipv6_addresses" {
  description = "hyperbola inventory ipv6 addresses"
  type        = "map"
}

variable "host" {
  description = "host the wiki runs on"
  type        = "string"
  default     = "hyperbola3"
}

resource "cloudflare_record" "hyperbo_la_A" {
  domain  = "hyperbo.la"
  name    = "hyperbo.la"
  value   = "${lookup(var.ipv4_addresses, var.host)}"
  type    = "A"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "www_hyperbo_la_A" {
  domain  = "hyperbo.la"
  name    = "www"
  value   = "${lookup(var.ipv4_addresses, var.host)}"
  type    = "A"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "staging_hyperbo_la_A" {
  domain  = "hyperbo.la"
  name    = "staging"
  value   = "${lookup(var.ipv4_addresses, var.host)}"
  type    = "A"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "hyperbo_la_AAAA" {
  domain  = "hyperbo.la"
  name    = "hyperbo.la"
  value   = "${lookup(var.ipv6_addresses, var.host)}"
  type    = "AAAA"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "www_hyperbo_la_AAAA" {
  domain  = "hyperbo.la"
  name    = "www"
  value   = "${lookup(var.ipv6_addresses, var.host)}"
  type    = "AAAA"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "staging_hyperbo_la_AAAA" {
  domain  = "hyperbo.la"
  name    = "staging"
  value   = "${lookup(var.ipv6_addresses, var.host)}"
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
  records = ["${lookup(var.ipv4_addresses, var.host)}"]
}
