variable "env" {}
variable "bucket" {}

data "aws_route53_zone" "hyperbolausercontent" {
  name         = "hyperbolausercontent.net."
  private_zone = false
}

resource "aws_route53_record" "bucket" {
  zone_id = "${data.aws_route53_zone.hyperbolausercontent.zone_id}"
  name    = "${var.bucket}"
  type    = "CNAME"
  ttl     = "300"
  records = ["${aws_s3_bucket.bucket.website_endpoint}"]
}

resource "aws_s3_bucket" "bucket" {
  bucket = "${var.bucket}.hyperbolausercontent.net"
  acl    = "public-read"

  website {
    index_document = "index.html"
  }

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

output "bucket-cname" {
  value = "${aws_route53_record.bucket.fqdn}"
}
