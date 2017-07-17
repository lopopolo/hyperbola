variable "local_ip" {
  description = "IP assigned to a local vagrant box for testing"
}

# Cloudflare DNS

resource "cloudflare_record" "wiki" {
  domain  = "hyperbo.la"
  name    = "wiki"
  value   = "${aws_alb.alb.dns_name}"
  type    = "CNAME"
  ttl     = 1
  proxied = false
}

# Route 53 DNS
data "aws_route53_zone" "hyperbola" {
  name         = "hyperbo.la."
  private_zone = false
}

resource "aws_route53_record" "wiki-A" {
  zone_id = "${data.aws_route53_zone.hyperbola.zone_id}"
  name    = "wiki"
  type    = "A"

  alias {
    name                   = "${aws_alb.alb.dns_name}"
    zone_id                = "${aws_alb.alb.zone_id}"
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "wiki-AAAA" {
  zone_id = "${data.aws_route53_zone.hyperbola.zone_id}"
  name    = "wiki"
  type    = "AAAA"

  alias {
    name                   = "${aws_alb.alb.dns_name}"
    zone_id                = "${aws_alb.alb.zone_id}"
    evaluate_target_health = true
  }
}
