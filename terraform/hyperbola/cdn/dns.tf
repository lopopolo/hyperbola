variable "ipv4_address" {}
variable "ipv6_address" {}

variable "host" {
  description = "host the wiki runs on"
  type        = "string"
  default     = "hyperbola3"
}

resource "cloudflare_record" "hyperbolacdn_com_A" {
  domain  = "hyperbolacdn.com"
  name    = "hyperbolacdn.com"
  value   = "${var.ipv4_address}"
  type    = "A"
  ttl     = 1
  proxied = true
}

resource "cloudflare_record" "www_hyperbolacdn_com_A" {
  domain  = "hyperbolacdn.com"
  name    = "www"
  value   = "${var.ipv4_address}"
  type    = "A"
  ttl     = 1
  proxied = true
}

resource "cloudflare_record" "hyperbolacdn_com_AAAA" {
  domain  = "hyperbolacdn.com"
  name    = "hyperbolacdn.com"
  value   = "${var.ipv6_address}"
  type    = "AAAA"
  ttl     = 1
  proxied = true
}

resource "cloudflare_record" "www_hyperbolacdn_com_AAAA" {
  domain  = "hyperbolacdn.com"
  name    = "www"
  value   = "${var.ipv6_address}"
  type    = "AAAA"
  ttl     = 1
  proxied = true
}
