# hyperbola terraform

This configuration borrows heavily from:

- [hashicorp/best-practices aws](https://github.com/hashicorp/best-practices/tree/master/terraform/providers/aws)
- [terraform-community-modules/tf_aws_bastion_s3_keys](https://github.com/terraform-community-modules/tf_aws_bastion_s3_keys)
- [aws-ec2-assign-elastic-ip](https://github.com/skymill/aws-ec2-assign-elastic-ip)

## Architecture

Create one VPC per environment. An environment is composed of a (region, app, env) tuple.
