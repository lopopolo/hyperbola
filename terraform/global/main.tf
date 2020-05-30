terraform {
  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/hyperbola-global/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

variable "name" {
  default = "hyperbola-global"
}

variable "iam_admins" {
  default = ["hyperbola-admin-2"]
}

data "aws_iam_policy_document" "admin" {
  statement {
    sid = 1

    effect = "Allow"

    actions   = ["*"]
    resources = ["*"]
  }
}

module "iam_admin" {
  source = "../modules/aws/util/iam"

  name  = "${var.name}-admin"
  users = var.iam_admins

  policy = data.aws_iam_policy_document.admin.json
}

output "config" {
  value = <<CONFIG

Admin IAM:
  Admin Users: ${join(
  "\n               ",
  formatlist("%s", module.iam_admin.users),
  )}

  Access IDs: ${join(
  "\n              ",
  formatlist("%s", module.iam_admin.access_ids),
  )}

  Secret Keys: ${join(
  "\n               ",
  formatlist("%s", module.iam_admin.secret_keys),
)}

CONFIG

}

output "iam_admin_users" {
  value = module.iam_admin.users
}

output "iam_admin_access_ids" {
  value = module.iam_admin.access_ids
}

output "iam_admin_secret_keys" {
  value = module.iam_admin.secret_keys
}
