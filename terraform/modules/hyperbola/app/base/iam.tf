resource "aws_iam_instance_profile" "app" {
  name_prefix = "app-profile-"
  role        = aws_iam_role.app.name

  lifecycle {
    create_before_destroy = true
  }
}

data "aws_iam_policy_document" "assume" {
  statement {
    sid = "AppAssumeRole"

    actions = [
      "sts:AssumeRole",
    ]

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "app" {
  name_prefix = "app-role-"

  assume_role_policy = data.aws_iam_policy_document.assume.json
}

module "app_policy" {
  source = "../iam"

  env = var.env

  bucket_arns = [
    aws_s3_bucket.media.arn,
    aws_s3_bucket.backup.arn,
  ]
}

resource "aws_iam_role_policy" "app" {
  name_prefix = "app-policy-"
  role        = aws_iam_role.app.id

  policy = module.app_policy.document
}

output "app_instance_profile" {
  value = aws_iam_instance_profile.app.name
}
