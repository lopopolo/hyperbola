terraform {
  required_version = "> 0.9.7"

  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/frklft-prod-northwest/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

resource "aws_s3_bucket" "website" {
  bucket = "www.frklft.tires"
  acl    = "public-read"

  website {
    index_document = "index.html"

    routing_rules = <<EOF
[{
    "Condition": {
        "HttpErrorCodeReturnedEquals": "404"
    },
    "Redirect": {
        "HttpRedirectCode": "302",
        "Protocol": "https",
        "HostName": "www.frklft.tires",
        "ReplaceKeyWith": ""
    }
}]
EOF
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

resource "aws_s3_bucket_object" "team" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "team"
  source       = "${path.root}/site/team.html"
  etag         = "${md5(file("${path.root}/site/team.html"))}"
  content_type = "text/html"
}

resource "aws_s3_bucket_object" "error" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "error.html"
  source       = "${path.root}/site/error.html"
  etag         = "${md5(file("${path.root}/site/error.html"))}"
  content_type = "text/html"
}

resource "aws_s3_bucket_object" "logo" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "logo.png"
  source       = "${path.root}/site/logo.png"
  etag         = "${md5(file("${path.root}/site/logo.png"))}"
  content_type = "image/png"
}

resource "aws_s3_bucket_object" "image" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "forklift-tires.jpg"
  source       = "${path.root}/site/forklift-tires.jpg"
  etag         = "${md5(file("${path.root}/site/forklift-tires.jpg"))}"
  content_type = "image/jpeg"
}

resource "aws_s3_bucket_object" "index-hero" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "tire-rack.png"
  source       = "${path.root}/site/tire-rack.png"
  etag         = "${md5(file("${path.root}/site/tire-rack.png"))}"
  content_type = "image/png"
}

resource "aws_s3_bucket_object" "team-hero" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "forklift-servers.jpg"
  source       = "${path.root}/site/forklift-servers.jpg"
  etag         = "${md5(file("${path.root}/site/forklift-servers.jpg"))}"
  content_type = "image/jpeg"
}

resource "aws_s3_bucket_object" "team-hero-png" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "forklift-servers.png"
  source       = "${path.root}/site/forklift-servers.png"
  etag         = "${md5(file("${path.root}/site/forklift-servers.png"))}"
  content_type = "image/png"
}

resource "aws_s3_bucket_object" "team-crane" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "team-crane.jpg"
  source       = "${path.root}/site/team-crane.jpg"
  etag         = "${md5(file("${path.root}/site/team-crane.jpg"))}"
  content_type = "image/jpeg"
}

resource "aws_s3_bucket_object" "team-forklift" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "team-forklift.jpg"
  source       = "${path.root}/site/team-forklift.jpg"
  etag         = "${md5(file("${path.root}/site/team-forklift.jpg"))}"
  content_type = "image/jpeg"
}

resource "aws_s3_bucket_object" "team-front-loader" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "team-front-loader.jpg"
  source       = "${path.root}/site/team-front-loader.jpg"
  etag         = "${md5(file("${path.root}/site/team-front-loader.jpg"))}"
  content_type = "image/jpeg"
}

resource "aws_s3_bucket_object" "team-speed-swing" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "team-speed-swing.jpg"
  source       = "${path.root}/site/team-speed-swing.jpg"
  etag         = "${md5(file("${path.root}/site/team-speed-swing.jpg"))}"
  content_type = "image/jpeg"
}

resource "aws_s3_bucket_object" "robots" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "robots.txt"
  source       = "${path.root}/site/robots.txt"
  etag         = "${md5(file("${path.root}/site/robots.txt"))}"
  content_type = "text/plain"
}

resource "aws_s3_bucket_object" "favicon" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "favicon.ico"
  source       = "${path.root}/site/favicon.ico"
  etag         = "${md5(file("${path.root}/site/favicon.ico"))}"
  content_type = "image/x-icon"
}

resource "aws_s3_bucket_object" "apple-touch-icon" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "apple-touch-icon.png"
  source       = "${path.root}/site/apple-touch-icon.png"
  etag         = "${md5(file("${path.root}/site/apple-touch-icon.png"))}"
  content_type = "image/png"
}

resource "aws_s3_bucket_object" "android-chrome-192" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "android-chrome-192x192.png"
  source       = "${path.root}/site/android-chrome-192x192.png"
  etag         = "${md5(file("${path.root}/site/android-chrome-192x192.png"))}"
  content_type = "image/png"
}

resource "aws_s3_bucket_object" "android-chrome-512" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "android-chrome-512x512.png"
  source       = "${path.root}/site/android-chrome-512x512.png"
  etag         = "${md5(file("${path.root}/site/android-chrome-512x512.png"))}"
  content_type = "image/png"
}

provider "aws" {
  region = "us-east-1"
  alias  = "cloudfront-acm-region"
}

data "aws_acm_certificate" "website" {
  provider = "aws.cloudfront-acm-region"
  domain   = "www.frklft.tires"
  statuses = ["ISSUED"]
}

resource "aws_cloudfront_distribution" "website" {
  origin {
    domain_name = "${aws_s3_bucket.website.website_endpoint}"
    origin_id   = "s3-website"

    custom_origin_config {
      origin_protocol_policy = "http-only"
      http_port              = "80"
      https_port             = "443"
      origin_ssl_protocols   = ["TLSv1"]
    }
  }

  enabled         = true
  is_ipv6_enabled = true
  comment         = "CloudFront for www.frklft.tires"

  aliases = ["www.frklft.tires"]

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
  bucket = "frklft.tires"
  acl    = "public-read"

  website {
    redirect_all_requests_to = "https://www.frklft.tires"
  }
}

data "aws_acm_certificate" "website-no-www" {
  provider = "aws.cloudfront-acm-region"
  domain   = "www.frklft.tires"
  statuses = ["ISSUED"]
}

resource "aws_cloudfront_distribution" "website-no-www" {
  origin {
    domain_name = "${aws_s3_bucket.website-no-www.website_endpoint}"
    origin_id   = "s3-website"

    custom_origin_config {
      origin_protocol_policy = "http-only"
      http_port              = "80"
      https_port             = "443"
      origin_ssl_protocols   = ["TLSv1"]
    }
  }

  enabled         = true
  is_ipv6_enabled = true
  comment         = "CloudFront for frklft.tires"

  aliases = ["frklft.tires"]

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

    viewer_protocol_policy = "allow-all"
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
