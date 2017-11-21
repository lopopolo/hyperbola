terraform {
  required_version = "> 0.9.7"

  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/wr-prod-northwest/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

resource "aws_s3_bucket" "website" {
  bucket = "www.burnfastburnbright.com"
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}

resource "aws_s3_bucket_object" "index" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "index.html"
  source       = "${path.root}/site/index.html"
  etag         = "${md5(file("${path.root}/site/index.html"))}"
  content_type = "text/html"
}

resource "aws_s3_bucket_object" "error" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "error.html"
  source       = "${path.root}/site/index.html"
  etag         = "${md5(file("${path.root}/site/index.html"))}"
  content_type = "text/html"
}

resource "aws_s3_bucket_object" "image" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "WR-124.jpg"
  source       = "${path.root}/site/WR-124.jpg"
  etag         = "${md5(file("${path.root}/site/WR-124.jpg"))}"
  content_type = "image/jpeg"
}

provider "aws" {
  region = "us-east-1"
  alias  = "cloudfront-acm-region"
}

data "aws_acm_certificate" "website" {
  provider = "aws.cloudfront-acm-region"
  domain   = "www.burnfastburnbright.com"
  statuses = ["ISSUED"]
}

resource "aws_cloudfront_distribution" "website" {
  origin {
    domain_name = "${aws_s3_bucket.website.bucket_domain_name}"
    origin_id   = "s3-website"
  }

  enabled             = true
  is_ipv6_enabled     = true
  comment             = "CloudFront for www.burnfastburnbright.com"
  default_root_object = "index.html"

  aliases = ["www.burnfastburnbright.com"]

  default_cache_behavior {
    allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "s3-website"

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
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
    Environment = "wr-prod"
  }

  viewer_certificate {
    acm_certificate_arn      = "${data.aws_acm_certificate.website.arn}"
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2018"
  }
}

resource "aws_s3_bucket" "website-no-www" {
  bucket = "burnfastburnbright.com"
  acl    = "public-read"

  website {
    redirect_all_requests_to = "https://www.burnfastburnbright.com"
  }
}

data "aws_acm_certificate" "website-no-www" {
  provider = "aws.cloudfront-acm-region"
  domain   = "burnfastburnbright.com"
  statuses = ["ISSUED"]
}

resource "aws_cloudfront_distribution" "website-no-www" {
  origin {
    domain_name = "${aws_s3_bucket.website-no-www.bucket_domain_name}"
    origin_id   = "s3-website"
  }

  enabled             = true
  is_ipv6_enabled     = true
  comment             = "CloudFront for burnfastburnbright.com"
  default_root_object = "index.html"

  aliases = ["burnfastburnbright.com"]

  default_cache_behavior {
    allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "s3-website"

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
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
    Environment = "wr-prod"
  }

  viewer_certificate {
    acm_certificate_arn      = "${data.aws_acm_certificate.website-no-www.arn}"
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2018"
  }
}
