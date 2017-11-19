resource "aws_route53_zone" "burnfastburnbright-com" {
  name    = "burnfastburnbright.com."
  comment = "HostedZone created by Route53 Registrar"
}

resource "aws_route53_record" "website" {
  name    = "www"
  zone_id = "${aws_route53_zone.burnfastburnbright-com.zone_id}"
  type    = "A"

  alias {
    name                   = "${aws_s3_bucket.website.website_domain}"
    zone_id                = "${aws_s3_bucket.website.hosted_zone_id}"
    evaluate_target_health = true
  }
}
