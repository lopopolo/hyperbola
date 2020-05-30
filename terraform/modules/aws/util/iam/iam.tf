#--------------------------------------------------------------
# This module is used to create an AWS IAM group and its users
#--------------------------------------------------------------

variable "name" {
  type = string
}

variable "users" {
  type = list(string)
}

variable "policy" {
  type = string
}

resource "aws_iam_group" "group" {
  name = var.name
}

resource "aws_iam_group_policy" "policy" {
  name   = var.name
  group  = aws_iam_group.group.id
  policy = var.policy
}

resource "aws_iam_user" "user" {
  count = length(var.users)
  name  = element(var.users, count.index)

  tags = {
    project    = "aws"
    managed_by = "terraform"
  }
}

resource "aws_iam_access_key" "key" {
  count = length(var.users)
  user  = element(aws_iam_user.user.*.name, count.index)
}

resource "aws_iam_group_membership" "membership" {
  name  = var.name
  group = aws_iam_group.group.name
  users = aws_iam_user.user.*.name
}

output "users" {
  value = aws_iam_access_key.key.*.user
}

output "access_ids" {
  value = aws_iam_access_key.key.*.id
}

output "secret_keys" {
  value = aws_iam_access_key.key.*.secret
}
