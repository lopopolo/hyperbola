variable "vpc_id" {}
variable "private_subnet_tier" {}

data "aws_vpc" "current" {
  id = "${var.vpc_id}"
}

data "aws_subnet_ids" "private" {
  vpc_id = "${data.aws_vpc.current.id}"

  tags {
    Network = "${var.private_subnet_tier}"
  }
}

data "aws_route_table" "private" {
  count     = "${length(data.aws_subnet_ids.private.ids)}"
  subnet_id = "${data.aws_subnet_ids.private.ids[count.index]}"
}

data "aws_vpc_endpoint_service" "s3" {
  service = "s3"
}

resource "aws_vpc_endpoint" "s3" {
  vpc_id          = "${data.aws_vpc.current.id}"
  service_name    = "${data.aws_vpc_endpoint_service.s3.service_name}"
  route_table_ids = ["${data.aws_route_table.private.*.id}"]
}

output "s3_endpoint_prefix_list_id" {
  value = "${aws_vpc_endpoint.s3.prefix_list_id}"
}
