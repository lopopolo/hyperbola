variable "vpc_id" {}
variable "private_subnet_name" {}

data "aws_vpc" "current" {
  id = "${var.vpc_id}"
}

data "aws_region" "current" {
  current = true
}

data "aws_subnet_ids" "private" {
  vpc_id = "${data.aws_vpc.current.id}"

  tags {
    Network = "${var.private_subnet_name}"
  }
}

data "aws_route_table" "private" {
  count     = "${length(data.aws_subnet_ids.private.ids)}"
  subnet_id = "${data.aws_subnet_ids.private.ids[count.index]}"
}

resource "aws_vpc_endpoint" "private-backup-s3-endpoint" {
  vpc_id          = "${data.aws_vpc.current.id}"
  service_name    = "com.amazonaws.${data.aws_region.current.name}.s3"
  route_table_ids = ["${data.aws_route_table.private.*.id}"]
}
