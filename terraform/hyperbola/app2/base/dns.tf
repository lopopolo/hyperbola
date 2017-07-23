data "aws_route53_zone" "hyperbolausercontent" {
  name         = "hyperbolausercontent.net."
  private_zone = false
}

resource "aws_route53_record" "cdn-A" {
  zone_id = "${data.aws_route53_zone.hyperbolausercontent.zone_id}"
  name    = "${var.bucket}"
  type    = "A"

  alias {
    name                   = "${aws_cloudfront_distribution.cdn.domain_name}"
    zone_id                = "${aws_cloudfront_distribution.cdn.hosted_zone_id}"
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "cdn-AAAA" {
  zone_id = "${data.aws_route53_zone.hyperbolausercontent.zone_id}"
  name    = "${var.bucket}"
  type    = "AAAA"

  alias {
    name                   = "${aws_cloudfront_distribution.cdn.domain_name}"
    zone_id                = "${aws_cloudfront_distribution.cdn.hosted_zone_id}"
    evaluate_target_health = false
  }
}
