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
    "Resource": ["${aws_s3_bucket.media.arn}",
                 "${aws_s3_bucket.media.arn}/*",
                 "${data.terraform_remote_state.global.backup_bucket_arn}",
                 "${data.terraform_remote_state.global.backup_bucket_arn}/*"]
    }
  ]
}
EOF
}
