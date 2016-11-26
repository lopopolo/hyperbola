variable "cloudflare_email" {
  default = "rjl@hyperbo.la"
}

variable "cloudflare_token" {
  default = ""
}

data template_file "cloudflare_token" {
  template = "$${token}"

  vars {
    token = "${coalesce(var.cloudflare_token, replace(file("${path.root}/../.secrets/cloudflare-api-key.txt"), "\n", ""))}"
  }
}

provider "cloudflare" {
  email = "${var.cloudflare_email}"
  token = "${data.template_file.cloudflare_token.rendered}"
}

variable "ipv4_addresses" {
  description = "IPv4 addresses of hyperbola machines"
  type        = "map"

  default = {
    hyperbola3 = "69.164.208.10"
  }
}

variable "ipv6_addresses" {
  description = "IPv6 addresses of hyperbola machines"
  type        = "map"

  default = {
    hyperbola3 = "2600:3c03::f03c:91ff:fe2c:b8c8"
  }
}

# Cloudflare DNS

resource "cloudflare_record" "hyperbola3_dc_hyperbo_la_A" {
  domain  = "hyperbo.la"
  name    = "hyperbola3.dc"
  value   = "${lookup(var.ipv4_addresses, "hyperbola3")}"
  type    = "A"
  ttl     = 1
  proxied = false
}

# Route 53 DNS

resource "aws_route53_zone" "hyperbola-zone" {
  name = "hyperbo.la"
}

resource "aws_route53_zone" "hyperbola-local-zone" {
  name = "local.hyperbo.la"

  tags {
    Environment = "localhost"
  }
}

resource "aws_route53_record" "hyperbola-local-ns" {
  zone_id = "${aws_route53_zone.hyperbola-local-zone.zone_id}"
  name    = "local.hyperbo.la"
  type    = "NS"
  ttl     = "30"

  records = [
    "${aws_route53_zone.hyperbola-local-zone.name_servers.0}",
    "${aws_route53_zone.hyperbola-local-zone.name_servers.1}",
    "${aws_route53_zone.hyperbola-local-zone.name_servers.2}",
    "${aws_route53_zone.hyperbola-local-zone.name_servers.3}",
  ]
}

output "hyperbola-zone-id" {
  value = "${aws_route53_zone.hyperbola-zone.zone_id}"
}

output "hyperbola-local-zone-id" {
  value = "${aws_route53_zone.hyperbola-local-zone.zone_id}"
}
