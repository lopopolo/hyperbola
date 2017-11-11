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

output "hyperbola-zone-id" {
  value = "${aws_route53_zone.hyperbola-zone.zone_id}"
}

output "hyperbolausercontent-zone-id" {
  value = "${aws_route53_zone.hyperbolausercontent-net-public.zone_id}"
}

output "hyperboladc-zone-id" {
  value = "${aws_route53_zone.hyperboladc-net-public.zone_id}"
}
