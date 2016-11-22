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

resource "cloudflare_record" "wiki_hyperbo_la_A" {
  domain  = "hyperbo.la"
  name    = "wiki"
  value   = "${lookup(var.ipv4_addresses, var.host)}"
  type    = "A"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "wiki_hyperbo_la_AAAA" {
  domain  = "hyperbo.la"
  name    = "wiki"
  value   = "${lookup(var.ipv6_addresses, var.host)}"
  type    = "AAAA"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "wiki_local_hyperbo_la_A" {
  domain  = "hyperbo.la"
  name    = "wiki.local"
  value   = "${lookup(var.ipv4_addresses, "wiki-local-1")}"
  type    = "A"
  ttl     = 1
  proxied = false
}
