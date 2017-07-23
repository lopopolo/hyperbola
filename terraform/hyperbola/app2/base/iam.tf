resource "aws_iam_instance_profile" "app" {
  name_prefix = "app-profile-"
  role        = "${aws_iam_role.app.name}"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_iam_role" "app" {
  name_prefix = "app-role-"

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
  name_prefix = "app-policy-"
  role        = "${aws_iam_role.app.id}"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement":[{
    "Effect": "Allow",
    "Action": "s3:*",
    "Resource": ["${aws_s3_bucket.media.arn}",
                 "${aws_s3_bucket.media.arn}/*",
                 "${aws_s3_bucket.backup.arn}",
                 "${aws_s3_bucket.backup.arn}/*"]
    }
  ]
}
EOF
}

output "app_instance_profile" {
  value = "${aws_iam_instance_profile.app.name}"
}
