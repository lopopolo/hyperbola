variable "artifact_type" {}

variable "vpc_cidr" {}

variable "azs" {}

variable "private_subnets" {}

variable "public_subnets" {}

variable "bastion_instance_type" {}

module "network" {
  source                = "./aws/network"
  name                  = "${var.name}"
  vpc_cidr              = "${var.vpc_cidr}"
  azs                   = "${var.azs}"
  region                = "${var.region}"
  key_name              = "${aws_key_pair.site_key.key_name}"
  private_subnets       = "${var.private_subnets}"
  public_subnets        = "${var.public_subnets}"
  bastion_instance_type = "${var.bastion_instance_type}"
}

output "configuration" {
  value = <<CONFIGURATION

Add your private key and SSH into any private node via the Bastion host:
  ssh-add ../../../modules/keys/demo.pem
  ssh -A ${module.network.bastion_user}@${module.network.bastion_public_ip}

CONFIGURATION
}
