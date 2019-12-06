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
  default = "hyperbola-admin-2"
}

module "iam_admin" {
  source = "../modules/aws/util/iam"

  name  = "${var.name}-admin"
  users = var.iam_admins

  policy = <<EOF
{
  "Version"  : "2012-10-17",
  "Statement": [
    {
      "Effect"  : "Allow",
      "Action"  : "*",
      "Resource": "*"
    }
  ]
}
EOF

}

output "config" {
  value = <<CONFIG

Admin IAM:
  Admin Users: ${join(
  "\n               ",
  formatlist("%s", split(",", module.iam_admin.users)),
  )}

  Access IDs: ${join(
  "\n              ",
  formatlist("%s", split(",", module.iam_admin.access_ids)),
  )}

  Secret Keys: ${join(
  "\n               ",
  formatlist("%s", split(",", module.iam_admin.secret_keys)),
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

