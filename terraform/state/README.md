# hyperbola terraform state

The terraform configuration in this directory creates the infrastructure
necessary to store terraform state in S3.

The state for this infra is stored in the S3 bucket created by this code.

## Bootstrapping

1. Comment out the `terraform` block in `main.tf`
2. `terraform plan` and `terraform apply`
3. Uncomment the `terraform` block
4. `terraform init` and say yes to import
5. `terraform plan` and `terraform apply`
