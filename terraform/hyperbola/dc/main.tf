variable "dc" {}

data "aws_route53_zone" "dc" {
  name         = "hyperboladc.net."
  private_zone = false
}

resource "aws_route53_zone" "dc" {
  name = "${var.dc}.hyperboladc.net."

  tags {
    Environment = "${var.dc}"
  }
}

resource "aws_route53_record" "dc-ns" {
  zone_id = "${data.aws_route53_zone.dc.zone_id}"
  name    = "${var.dc}.hyperboladc.net."
  type    = "NS"
  ttl     = "30"

  records = ["${aws_route53_zone.dc.name_servers}"]
}

output "zone-id" {
  value = "${aws_route53_zone.dc.zone_id}"
}
