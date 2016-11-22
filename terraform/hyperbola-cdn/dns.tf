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

resource "cloudflare_record" "hyperbolacdn_com_A" {
  domain  = "hyperbolacdn.com"
  name    = "hyperbolacdn.com"
  value   = "${lookup(var.ipv4_addresses, var.host)}"
  type    = "A"
  ttl     = 1
  proxied = true
}

resource "cloudflare_record" "www_hyperbolacdn_com_A" {
  domain  = "hyperbolacdn.com"
  name    = "www"
  value   = "${lookup(var.ipv4_addresses, var.host)}"
  type    = "A"
  ttl     = 1
  proxied = true
}

resource "cloudflare_record" "hyperbolacdn_com_AAAA" {
  domain  = "hyperbolacdn.com"
  name    = "hyperbolacdn.com"
  value   = "${lookup(var.ipv6_addresses, var.host)}"
  type    = "AAAA"
  ttl     = 1
  proxied = true
}

resource "cloudflare_record" "www_hyperbolacdn_com_AAAA" {
  domain  = "hyperbolacdn.com"
  name    = "www"
  value   = "${lookup(var.ipv6_addresses, var.host)}"
  type    = "AAAA"
  ttl     = 1
  proxied = true
}
