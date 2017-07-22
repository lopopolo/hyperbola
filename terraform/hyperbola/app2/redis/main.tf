variable "vpc_id" {}
variable "azs" {}
variable "name" {}
variable "env" {}

data "aws_vpc" "current" {
  id = "${var.vpc_id}"
}

resource "aws_security_group" "redis" {
  vpc_id      = "${data.aws_vpc.current.id}"
  name_prefix = "app-redis-sg-"

  tags {
    Name        = "${var.name}-sg"
    Environment = "${var.env}"
  }
}

module "tier" {
  source = "../../../aws/network/subnet_tier"
}

module "redis-subnets" {
  source = "../../../aws/network/private_subnet"

  name   = "${var.name}"
  vpc_id = "${data.aws_vpc.current.id}"
  azs    = "${var.azs}"

  subnet_tier       = "${module.tier.private-redis}"
  nat_enabled       = false
  nat_gateway_ids   = ""
  egress_gateway_id = ""
}

# ElastiCache resources
resource "aws_elasticache_subnet_group" "redis" {
  name       = "app-redis-subnet-group" # at most one per VPC
  subnet_ids = ["${split(",", module.redis-subnets.subnet_ids)}"]
}

resource "aws_elasticache_replication_group" "redis" {
  replication_group_id          = "app-redis-repl-group" # at most one per VPC
  replication_group_description = "app redis cluster"
  node_type                     = "cache.t2.micro"
  automatic_failover_enabled    = true
  port                          = "6379"
  parameter_group_name          = "default.redis3.2.cluster.on"
  subnet_group_name             = "${aws_elasticache_subnet_group.redis.name}"
  security_group_ids            = ["${aws_security_group.redis.id}"]
  maintenance_window            = "sun:02:39-sun:03:09"

  # http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Replication.Redis-RedisCluster.html
  cluster_mode {
    replicas_per_node_group = 1 # read replicas. these get promoted during failover
    num_node_groups         = 1 # shards
  }

  tags {
    Name        = "${var.name}-replication-group"
    Environment = "${var.env}"
  }
}

output "redis_endpoint" {
  value = "${aws_elasticache_replication_group.redis.configuration_endpoint_address}"
}

output "redis_port" {
  value = "${aws_elasticache_replication_group.redis.port}"
}

output "redis_security_group_id" {
  value = "${aws_security_group.redis.id}"
}
