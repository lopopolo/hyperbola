resource "aws_route53_zone" "burnfastburnbright-com" {
  name    = "burnfastburnbright.com."
  comment = "HostedZone created by Route53 Registrar"
}

resource "aws_route53_record" "website" {
  name    = "www"
  zone_id = "${aws_route53_zone.burnfastburnbright-com.zone_id}"
  type    = "A"

  alias {
    name                   = "${aws_cloudfront_distribution.website.domain_name}"
    zone_id                = "${aws_cloudfront_distribution.website.hosted_zone_id}"
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "website-AAAA" {
  name    = "www"
  zone_id = "${aws_route53_zone.burnfastburnbright-com.zone_id}"
  type    = "AAAA"

  alias {
    name                   = "${aws_cloudfront_distribution.website.domain_name}"
    zone_id                = "${aws_cloudfront_distribution.website.hosted_zone_id}"
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "website-no-www" {
  name    = "burnfastburnbright.com"
  zone_id = "${aws_route53_zone.burnfastburnbright-com.zone_id}"
  type    = "A"

  alias {
    name                   = "${aws_cloudfront_distribution.website-no-www.domain_name}"
    zone_id                = "${aws_cloudfront_distribution.website-no-www.hosted_zone_id}"
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "website-no-www-AAAA" {
  name    = "burnfastburnbright.com"
  zone_id = "${aws_route53_zone.burnfastburnbright-com.zone_id}"
  type    = "AAAA"

  alias {
    name                   = "${aws_cloudfront_distribution.website-no-www.domain_name}"
    zone_id                = "${aws_cloudfront_distribution.website-no-www.hosted_zone_id}"
    evaluate_target_health = false
  }
}
