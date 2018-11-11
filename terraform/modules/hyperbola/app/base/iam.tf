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
      "Sid": "AppAssumeRole",
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      }
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
  "Statement": [
    {
      "Sid" : "AllowAppBucketPermissions",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetBucketLocation"
      ],
      "Resource": [
        "${aws_s3_bucket.media.arn}",
        "${aws_s3_bucket.backup.arn}"
      ]
    },
    {
      "Sid" : "AllowAppBucketContentPermissions",
      "Effect": "Allow",
      "Action": "s3:*Object*",
      "Resource": [
        "${aws_s3_bucket.media.arn}/*",
        "${aws_s3_bucket.backup.arn}/*"
      ]
    },
    {
      "Sid" : "AllowSecretsAccess",
      "Effect": "Allow",
      "Action": [
        "ssm:GetParametersByPath"
      ],
      "Resource": [
        "arn:aws:ssm:*:*:parameter/app/${var.env}/*"
      ]
     }
  ]
}
EOF
}

output "app_instance_profile" {
  value = "${aws_iam_instance_profile.app.name}"
}
