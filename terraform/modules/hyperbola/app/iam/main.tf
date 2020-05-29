variable "env" {}

variable "bucket_arns" {
  type = list
}

data "aws_iam_policy_document" "this" {
  statement {
    sid = "AllowAppBucketPermissions"

    actions = [
      "s3:ListBucket",
      "s3:GetBucketLocation",
    ]

    resources = formatlist("%s", var.bucket_arns)
  }

  statement {
    sid = "AllowAppBucketContentPermissions"

    actions = [
      "s3:*Object*",
    ]

    resources = formatlist("%s/*", var.bucket_arns)
  }

  statement {
    sid = "AllowSecretsAccess"

    actions = [
      "ssm:GetParametersByPath",
    ]

    resources = [
      "arn:aws:ssm:*:*:parameter/app/${var.env}/*",
    ]
  }
}

output "document" {
  value = "${data.aws_iam_policy_document.this.json}"
}
