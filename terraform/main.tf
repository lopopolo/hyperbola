variable "name" {}

variable "iam_admins" {}

terraform {
  required_version = "> 0.9.7"

  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/hyperbola/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

variable "cloudflare_email" {
  default = "rjl@hyperbo.la"
}

variable "cloudflare_token" {
  default = ""
}

provider "cloudflare" {
  email = "${var.cloudflare_email}"
  token = "${coalesce(var.cloudflare_token, trimspace(file("${path.root}/../.secrets/cloudflare-api-key.txt")))}"
}

module "iam_admin" {
  source = "./aws/util/iam"

  name  = "${var.name}-admin"
  users = "${var.iam_admins}"

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
  Admin Users: ${join("\n               ", formatlist("%s", split(",", module.iam_admin.users)))}

  Access IDs: ${join("\n              ", formatlist("%s", split(",", module.iam_admin.access_ids)))}

  Secret Keys: ${join("\n               ", formatlist("%s", split(",", module.iam_admin.secret_keys)))}

CONFIG
}

output "iam_admin_users" {
  value = "${module.iam_admin.users}"
}

output "iam_admin_access_ids" {
  value = "${module.iam_admin.access_ids}"
}

output "iam_admin_secret_keys" {
  value = "${module.iam_admin.secret_keys}"
}

module "hyperbola-wiki" {
  source                    = "./hyperbola/wiki"
  name                      = "${var.name}-wiki"
  region                    = "${var.region}"
  vpc_id                    = "${module.network.vpc_id}"
  public_subnet_name        = "${module.network.public_subnet_name}"
  private_subnet_name       = "${module.network.private_subnet_name}"
  key_name                  = "hyperbola-cas"
  bastion_security_group_id = "${module.network.bastion_security_group_id}"

  local_ip = "192.168.10.10"
}

output "wiki_elb_zone_id" {
  value = "${module.hyperbola-wiki.alb_zone_id}"
}

output "wiki_elb_dns" {
  value = "${module.hyperbola-wiki.alb_dns}"
}
