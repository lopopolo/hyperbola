variable "cloudflare_email" {
  default = "rjl@hyperbo.la"
}

variable "cloudflare_token" {}

provider "cloudflare" {
  email = "${var.cloudflare_email}"
  token = "${var.cloudflare_token}"
}

variable "ipv4_addresses" {
  description = "IPv4 addresses of hyperbola machines"
  type        = "map"

  default = {
    hyperbola2   = "45.33.89.210"
    hyperbola3   = "69.164.208.10"
    wiki-local-1 = "192.168.10.10"
  }
}

variable "ipv6_addresses" {
  description = "IPv6 addresses of hyperbola machines"

  default = {
    hyperbola2 = "2600:3c03::f03c:91ff:fe0a:ec23"
    hyperbola3 = "2600:3c03::f03c:91ff:fe2c:b8c8"
  }
}

resource "cloudflare_record" "hyperbola1_dc_hyperbo_la_A" {
  domain  = "hyperbo.la"
  name    = "hyperbola1.dc"
  value   = "173.255.236.117"
  type    = "A"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "hyperbola2_dc_hyperbo_la_A" {
  domain  = "hyperbo.la"
  name    = "hyperbola2.dc"
  value   = "${lookup(var.ipv4_addresses, "hyperbola2")}"
  type    = "A"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "hyperbola3_dc_hyperbo_la_A" {
  domain  = "hyperbo.la"
  name    = "hyperbola3.dc"
  value   = "${lookup(var.ipv4_addresses, "hyperbola3")}"
  type    = "A"
  ttl     = 1
  proxied = false
}
