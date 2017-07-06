variable "env" {}
variable "bucket" {}

data "aws_route53_zone" "hyperbolausercontent" {
  name         = "hyperbolausercontent.net."
  private_zone = false
}

resource "aws_route53_record" "cdn" {
  zone_id = "${data.aws_route53_zone.hyperbolausercontent.zone_id}"
  name    = "${var.bucket}"
  type    = "A"

  alias {
    name                   = "${aws_cloudfront_distribution.cdn.domain_name}"
    zone_id                = "${aws_cloudfront_distribution.cdn.hosted_zone_id}"
    evaluate_target_health = false
  }
}

data "aws_acm_certificate" "cdn" {
  domain   = "*.hyperbolausercontent.net"
  statuses = ["ISSUED"]
}

resource "aws_cloudfront_distribution" "cdn" {
  origin {
    domain_name = "${aws_s3_bucket.bucket.bucket_domain_name}"
    origin_id   = "s3-media"
  }

  enabled         = true
  is_ipv6_enabled = true
  comment         = "CloudFront for hyperbola-app cdn - ${var.env}"

  aliases = ["${var.bucket}.hyperbolausercontent.net"]

  default_cache_behavior {
    allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "s3-media"

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "https-only"
    min_ttl                = 0
    default_ttl            = 3600
    max_ttl                = 86400
  }

  price_class = "PriceClass_100"

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  tags {
    Environment = "${var.env}"
  }

  viewer_certificate {
    acm_certificate_arn      = "${data.aws_acm_certificate.cdn.arn}"
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1"
  }
}

resource "aws_s3_bucket" "bucket" {
  bucket = "${var.bucket}.hyperbolausercontent.net"
  acl    = "public-read"

  versioning {
    enabled = true
  }

  tags {
    Name        = "hyperbola-app media files for ${var.env}"
    Environment = "${var.env}"
  }
}

resource "aws_iam_instance_profile" "app" {
  name = "hyperbola-app-${var.env}"
  role = "${aws_iam_role.app.name}"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_iam_role" "app" {
  name = "hyperbola-app-${var.env}"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "app" {
  name = "hyperbola-app-${var.env}"
  role = "${aws_iam_role.app.id}"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement":[{
    "Effect": "Allow",
    "Action": "s3:*",
    "Resource": ["${aws_s3_bucket.bucket.arn}",
                 "${aws_s3_bucket.bucket.arn}/*"]
    }
  ]
}
EOF
}
