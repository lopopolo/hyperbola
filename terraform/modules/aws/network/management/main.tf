variable "name" {}

variable "vpc_id" {}
variable "azs" {}
variable "internet_gateway_id" {}
variable "egress_gateway_id" {}

variable "s3_route_tables" {
  type = list
}

module "tier" {
  source = "../subnet_tier"
}

module "public_subnet" {
  source = "../public_subnet"

  name   = "${var.name}-public"
  vpc_id = var.vpc_id
  azs    = var.azs

  subnet_tier         = module.tier.management_public
  internet_gateway_id = var.internet_gateway_id
  egress_gateway_id   = var.egress_gateway_id
}

module "private_subnet" {
  source = "../private_subnet"

  name   = "${var.name}-private"
  vpc_id = var.vpc_id
  azs    = var.azs

  subnet_tier       = module.tier.management_private
  nat_enabled       = "false"
  nat_gateway_ids   = ""
  egress_gateway_id = var.egress_gateway_id
}

resource "aws_security_group" "this" {
  name_prefix = "management-sg-"
  description = "Management Domain Security Group"
  vpc_id      = var.vpc_id

  egress {
    from_port       = 80
    to_port         = 80
    protocol        = "tcp"
    security_groups = [aws_security_group.ssm.id]
  }

  egress {
    from_port       = 443
    to_port         = 443
    protocol        = "tcp"
    security_groups = [aws_security_group.ssm.id]
  }

  egress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Class = "management"
  }
}

data "aws_vpc_endpoint_service" "s3" {
  service = "s3"
}

resource "aws_vpc_endpoint" "s3" {
  vpc_id          = var.vpc_id
  service_name    = data.aws_vpc_endpoint_service.s3.service_name
  route_table_ids = concat(var.s3_route_tables, module.public_subnet.route_table, module.private_subnet.route_table)
}

data "aws_vpc_endpoint_service" "ssm" {
  service = "ssm"
}

resource "aws_security_group" "ssm" {
  name_prefix = "ssm-sg-"
  description = "SSM VPC Endpoint Security Group"
  vpc_id      = var.vpc_id
}

resource "aws_security_group_rule" "ssm_endpoint_from_management" {
  type                     = "ingress"
  protocol                 = "-1"
  from_port                = 0
  to_port                  = 0
  security_group_id        = aws_security_group.ssm.id
  source_security_group_id = aws_security_group.this.id
}

resource "aws_vpc_endpoint" "ssm" {
  vpc_id              = var.vpc_id
  service_name        = data.aws_vpc_endpoint_service.ssm.service_name
  vpc_endpoint_type   = "Interface"
  subnet_ids          = module.private_subnet.subnet_ids
  security_group_ids  = [aws_security_group.ssm.id]
  private_dns_enabled = true
}

output "s3_endpoint_prefix_list_id" {
  value = aws_vpc_endpoint.s3.prefix_list_id
}

output "ssm_security_group_id" {
  value = aws_security_group.ssm.id
}

output "build_subnet_ids" {
  value = join(",", module.public_subnet.subnet_ids)
}
