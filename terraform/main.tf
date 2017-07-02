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

resource "aws_key_pair" "site_key" {
  key_name   = "hyperbola-cas"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCahzyhyrx5VIHEJzw8s2s3J+YUbx3Wh31Jb3BG+0TYc7Bi9EjLLOXa0ttzSVsYsKViIB6+IqwJnIGt9XoKxm1jpP4jNudMlmr9Uda8TFwVRvdAK2JSO5q/lyQ6PVJ2LK7MByGN4Tw7cuqmyzeRgIg2zU3aIwqJxQdrK5ORuOG0ChmlS4CA5jI4F4xdUCrP7wNJ3JYR7OlZ/8R1PHHtSyoub8n2dv4n+HuzG6kq9B6pJCwPXCaotifvwuJv2Ezs+Ui0aDoZjsW6RWpVCBX/hQMRIZjCa3UOUhTU3Qzi8KmuVkXG5jFwFY+RlK5Ldu9kPnxRTBv5FFW1VQVYJmoQp2k345J0pV43rUobDm9QnHCgbPe2GZa/Defje+ihsf8eSrZGnVw3SFVKoZdb18oHfuZDdQ8g9cXYcZ4oRV0yURRFLy45V8g9VTQPO3SPaDzg6FK+1e3YLFG6eWQ6ldwE9wD+CR9NIMEpuNvN26AGgPZ9xon3IO1KgNs+2vs/BazcNVfj8oK8JgCRDWG0K4+KvsUYHxT6xDw8hdj5QhhokOJjPBzCraaCdweM0cNUWumnJd4dR70dtLl4rgj/kYWd7GPvB8EGDitmAjaaYWlxeAEZ6CVCrfiqJs7CkD58AUnsZB7a3bZHAlQA46qOYLSm6h5Q4wXL9D62d1ufQPZkNzybiQ== hyperbola-cas"

  lifecycle {
    create_before_destroy = true
  }
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

module "hyperbola-app" {
  source         = "./hyperbola/app"
  host           = "hyperbola3"
  ipv4_addresses = "${var.ipv4_addresses}"
  ipv6_addresses = "${var.ipv6_addresses}"
}

module "hyperbola-cdn" {
  source         = "./hyperbola/cdn"
  host           = "hyperbola3"
  ipv4_addresses = "${var.ipv4_addresses}"
  ipv6_addresses = "${var.ipv6_addresses}"
}

module "hyperbola-wiki" {
  source                    = "./hyperbola/wiki"
  name                      = "${var.name}-wiki"
  region                    = "${var.region}"
  vpc_id                    = "${module.network.vpc_id}"
  public_subnet_ids         = "${module.network.public_subnet_ids}"
  private_subnet_ids        = "${module.network.private_subnet_ids}"
  key_name                  = "${aws_key_pair.site_key.key_name}"
  bastion_security_group_id = "${module.network.bastion_security_group_id}"

  local_ip      = "192.168.10.10"
  prod_zone_id  = "${aws_route53_zone.hyperbola-zone.id}"
  local_zone_id = "${aws_route53_zone.hyperbola-local-zone.id}"
}

output "wiki_elb_zone_id" {
  value = "${module.hyperbola-wiki.alb_zone_id}"
}

output "wiki_private_fqdn" {
  value = "${module.hyperbola-wiki.private_fqdn}"
}

output "wiki_elb_dns" {
  value = "${module.hyperbola-wiki.alb_dns}"
}
