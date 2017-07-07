variable "vpc_cidr" {}

variable "azs" {}

variable "bastion_instance_type" {}

module "network" {
  source                = "./aws/network"
  name                  = "${var.name}"
  vpc_cidr              = "${var.vpc_cidr}"
  azs                   = "${var.azs}"
  region                = "${var.region}"
  key_name              = "${aws_key_pair.site_key.key_name}"
  bastion_instance_type = "${var.bastion_instance_type}"
}

output "bastion-configuration" {
  value = <<CONFIGURATION

Add your private key and SSH into any private node via the Bastion host:
  ssh-add ~/.ssh/hyperbola-cas
  ssh -A ${module.network.bastion_user}@${module.network.bastion_public_fqdn}

Bastion security group ${module.network.bastion_security_group_id} only allows
ingress from ${module.network.bastion_ingress_cidr}.

CONFIGURATION
}
