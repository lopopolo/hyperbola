variable "cloudflare_email" {
  default = "rjl@hyperbo.la"
}

variable "cloudflare_token" {
  default = ""
}

provider "cloudflare" {
  email = "${var.cloudflare_email}"
  token = "${coalesce(var.cloudflare_token, trimspace(file("${path.root}/../../../.secrets/cloudflare-api-key.txt")))}"
}

# Route 53 DNS

resource "aws_route53_zone" "hyperbola-zone" {
  name = "hyperbo.la"
}

resource "aws_route53_zone" "hyperbolausercontent-net-public" {
  name    = "hyperbolausercontent.net."
  comment = "HostedZone created by Route53 Registrar"
}

resource "aws_route53_zone" "hyperboladc-net-public" {
  name    = "hyperboladc.net."
  comment = "HostedZone created by Route53 Registrar"
}

module "aws-dc" {
  source = "../../hyperbola/dc"
  dc     = "aws"
}

module "linode-dc" {
  source = "../../hyperbola/dc"
  dc     = "linode"
}

module "local-dc" {
  source = "../../hyperbola/dc"
  dc     = "local"
}

output "hyperbola-zone-id" {
  value = "${aws_route53_zone.hyperbola-zone.zone_id}"
}

output "hyperbolausercontent-zone-id" {
  value = "${aws_route53_zone.hyperbolausercontent-net-public.zone_id}"
}

output "hyperboladc-zone-id" {
  value = "${aws_route53_zone.hyperboladc-net-public.zone_id}"
}

output "aws-hyperboladc-zone-id" {
  value = "${module.aws-dc.zone-id}"
}

output "linode-hyperboladc-zone-id" {
  value = "${module.linode-dc.zone-id}"
}

output "local-hyperboladc-zone-id" {
  value = "${module.local-dc.zone-id}"
}