module "hyperbola-app" {
  source         = "./hyperbola-app"
  host           = "hyperbola3"
  ipv4_addresses = "${var.ipv4_addresses}"
  ipv6_addresses = "${var.ipv6_addresses}"
}

module "hyperbola-cdn" {
  source         = "./hyperbola-cdn"
  host           = "hyperbola3"
  ipv4_addresses = "${var.ipv4_addresses}"
  ipv6_addresses = "${var.ipv6_addresses}"
}

module "hyperbola-wiki" {
  source         = "./hyperbola-wiki"
  host           = "hyperbola2"
  ipv4_addresses = "${var.ipv4_addresses}"
  ipv6_addresses = "${var.ipv6_addresses}"
}
