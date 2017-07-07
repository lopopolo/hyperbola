# hyperbola terraform

This configuration borrows heavily from:

- [hashicorp/best-practices aws](https://github.com/hashicorp/best-practices/tree/master/terraform/providers/aws)
- [terraform-community-modules/tf_aws_bastion_s3_keys](https://github.com/terraform-community-modules/tf_aws_bastion_s3_keys)
- [aws-ec2-assign-elastic-ip](https://github.com/skymill/aws-ec2-assign-elastic-ip)

## Architecture

### Global

- Deploys a VPC in 3 AZs to us-east-1
- Each AZ gets a public and a private subnet
- Private subnets connect to the internet through a single NAT
- A bastion host is deployed in the public subnets using an autoscaling group and an elastic IP
- Bastion has a IAM role and motd script to display all ASGs and IPs associated with them

### hyperbola

#### app

- DNS records in route53 and cloudflare

#### cdn

- DNS records in route53 and cloudflare

#### wiki

- DNS records in route53 and cloudflare
- wiki image deployed in a min/max/desired 1/1/1 autoscaling group in 3 private subnets
- Public ELB associated with ASG
- ELB associated with DNS records
