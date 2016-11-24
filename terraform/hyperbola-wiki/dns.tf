variable "prod_zone_id" {}

variable "local_zone_id" {}

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
  default     = "hyperbola2"
}

# Cloudflare DNS

resource "cloudflare_record" "wiki" {
  domain  = "hyperbo.la"
  name    = "wiki"
  value   = "${aws_elb.elb.dns_name}"
  type    = "CNAME"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "wiki-local" {
  domain  = "hyperbo.la"
  name    = "wiki.local"
  value   = "${lookup(var.ipv4_addresses, "wiki-local-1")}"
  type    = "A"
  ttl     = 1
  proxied = false
}

# Route 53 DNS
resource "aws_route53_record" "wiki" {
  zone_id = "${var.prod_zone_id}"
  name    = "wiki"
  type    = "A"

  alias {
    name                   = "${aws_elb.elb.dns_name}"
    zone_id                = "${aws_elb.elb.zone_id}"
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "wiki-local" {
  zone_id = "${var.local_zone_id}"
  name    = "wiki"
  type    = "A"

  ttl     = 300
  records = ["${lookup(var.ipv4_addresses, "wiki-local-1")}"]
}
