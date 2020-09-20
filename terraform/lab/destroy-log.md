## `terraform destroy`

```console
/usr/local/opt/terraform@0.12/bin/terraform destroy
Acquiring state lock. This may take a few moments...
module.network.module.management.data.aws_vpc_endpoint_service.ssm: Refreshing state...
module.network.module.management.data.aws_vpc_endpoint_service.s3: Refreshing state...

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:

Terraform will perform the following actions:

Plan: 0 to add, 0 to change, 0 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes


Destroy complete! Resources: 0 destroyed.
Releasing state lock. This may take a few moments...
```
