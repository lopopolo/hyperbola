# hyperbola terraform

This configuration borrows heavily from:

-   [hashicorp/best-practices aws](https://github.com/hashicorp/best-practices/tree/master/terraform/providers/aws)

## Architecture

Create one VPC per environment. An environment is composed of a (region, app, env) tuple. Name env after the closest
airport code.

| AWS region | Airport code |
|------------|--------------|
| us-east-1  | IAD          |
| us-west-2  | PDX          |
