# Route 53 DNS

resource "aws_route53_zone" "hyperbola" {
  name = "hyperbo.la"
}

resource "aws_route53_zone" "hyperbolausercontent" {
  name    = "hyperbolausercontent.net."
  comment = "HostedZone created by Route53 Registrar"
}

resource "aws_route53_zone" "hyperboladc" {
  name    = "hyperboladc.net."
  comment = "HostedZone created by Route53 Registrar"
}

resource "aws_route53_zone" "frklftio" {
  name    = "frklft.io."
  comment = "HostedZone created by Route53 Registrar"
}

output "hyperbola_zone_id" {
  value = "${aws_route53_zone.hyperbola.zone_id}"
}

output "hyperbolausercontent_zone_id" {
  value = "${aws_route53_zone.hyperbolausercontent.zone_id}"
}

output "hyperboladc_zone_id" {
  value = "${aws_route53_zone.hyperboladc.zone_id}"
}

output "frklftio_zone_id" {
  value = "${aws_route53_zone.frklftio.zone_id}"
}
