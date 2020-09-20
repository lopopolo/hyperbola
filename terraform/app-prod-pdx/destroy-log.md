## `terraform destroy`

### Plan

```console
$ /usr/local/opt/terraform@0.12/bin/terraform plan -destroy -no-color
Refreshing Terraform state in-memory prior to plan...
The refreshed state will be used to calculate this plan, but will not be
persisted to local or remote state storage.

module.base.data.aws_iam_policy_document.assume: Refreshing state...
module.network.module.management.data.aws_vpc_endpoint_service.s3: Refreshing state...
module.secrets.aws_ssm_parameter.secret_key: Refreshing state... [id=/app/production/SECRET_KEY]
module.base.data.aws_route53_zone.hyperbolausercontent: Refreshing state...
data.aws_route53_zone.hyperbola: Refreshing state...
module.network.module.management.data.aws_vpc_endpoint_service.ssm: Refreshing state...
module.backend.data.aws_ami.backend: Refreshing state...
module.network.module.vpc.aws_vpc.this: Refreshing state... [id=vpc-08d0186e]
module.backend.data.aws_acm_certificate.alb-cert: Refreshing state...
module.secrets.aws_ssm_parameter.database_password: Refreshing state... [id=/app/production/DB_PASSWORD]
module.mysql.aws_db_parameter_group.main_rds_instance: Refreshing state... [id=app-mysql-custom-params-0058e036eab3f18e3d97fe5a79]
module.base.aws_iam_role.app: Refreshing state... [id=app-role-00f8d1802132e948040476a3b0]
module.base.data.aws_acm_certificate.cdn: Refreshing state...
module.base.aws_iam_role_policy.app: Refreshing state... [id=app-role-00f8d1802132e948040476a3b0:app-policy-00f8d1802132e948040476a3b2]
module.base.aws_iam_instance_profile.app: Refreshing state... [id=app-profile-00f8d1802132e948040476a3b1]
module.network.module.vpc.aws_internet_gateway.this: Refreshing state... [id=igw-0dfd786a]
module.network.module.vpc.aws_egress_only_internet_gateway.this: Refreshing state... [id=eigw-053a3838325edd831]
module.network.aws_network_acl.acl: Refreshing state... [id=acl-4e77e428]
aws_route53_zone.app_dc: Refreshing state... [id=Z1O2JQV3R0LG26]
module.network.module.public_subnet.data.aws_vpc.this: Refreshing state...
module.backend.aws_security_group.backend: Refreshing state... [id=sg-5ffd4125]
module.backend.data.aws_vpc.this: Refreshing state...
module.network.module.nat.data.aws_vpc.selected: Refreshing state...
module.network.module.private_subnet.data.aws_vpc.this: Refreshing state...
module.mysql.data.aws_vpc.current: Refreshing state...
module.network.module.management.aws_security_group.ssm: Refreshing state... [id=sg-0258424690602bd25]
module.network.module.management.module.public_subnet.data.aws_vpc.this: Refreshing state...
module.network.module.management.module.private_subnet.data.aws_vpc.this: Refreshing state...
module.backend.aws_launch_template.backend: Refreshing state... [id=lt-0d1bd9f990ac86bda]
module.base.aws_cloudfront_distribution.cdn: Refreshing state... [id=E2KESP33B8DNIU]
module.network.module.management.aws_security_group.this: Refreshing state... [id=sg-053efd7127835f9c3]
module.network.module.public_subnet.aws_subnet.public[1]: Refreshing state... [id=subnet-bfe7fdd8]
module.network.module.public_subnet.aws_subnet.public[2]: Refreshing state... [id=subnet-113a864a]
module.network.module.public_subnet.aws_subnet.public[0]: Refreshing state... [id=subnet-dc043895]
module.backend.aws_alb_target_group.backend: Refreshing state... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02]
module.backend.aws_security_group.alb: Refreshing state... [id=sg-d88caea5]
module.network.module.public_subnet.aws_route_table.public[2]: Refreshing state... [id=rtb-09fc7ce039d02974d]
module.network.module.public_subnet.aws_route_table.public[0]: Refreshing state... [id=rtb-42cc9e24]
module.network.module.public_subnet.aws_route_table.public[1]: Refreshing state... [id=rtb-01399507207aed8cc]
module.network.module.private_subnet.aws_route_table.private[2]: Refreshing state... [id=rtb-6b431c12]
module.network.module.private_subnet.aws_route_table.private[0]: Refreshing state... [id=rtb-98421de1]
module.network.module.private_subnet.aws_route_table.private[1]: Refreshing state... [id=rtb-b6431ccf]
module.network.module.private_subnet.aws_subnet.private[1]: Refreshing state... [id=subnet-46e7fd21]
module.network.module.private_subnet.aws_subnet.private[0]: Refreshing state... [id=subnet-400a3609]
module.network.module.private_subnet.aws_subnet.private[2]: Refreshing state... [id=subnet-2a3d8171]
module.mysql.aws_security_group.main_db_access: Refreshing state... [id=sg-a2381cdf]
module.network.module.management.module.public_subnet.aws_subnet.public[1]: Refreshing state... [id=subnet-011c372fcaeea68f4]
module.network.module.management.module.public_subnet.aws_subnet.public[2]: Refreshing state... [id=subnet-05b3590a52783b057]
module.network.module.management.module.public_subnet.aws_subnet.public[0]: Refreshing state... [id=subnet-03016b54639ef2fbb]
module.network.module.management.aws_security_group_rule.ssm_endpoint_from_management: Refreshing state... [id=sgrule-1308896626]
module.network.module.management.module.public_subnet.aws_route_table.public[1]: Refreshing state... [id=rtb-0273f9500b21931f6]
module.network.module.management.module.public_subnet.aws_route_table.public[0]: Refreshing state... [id=rtb-0abb1bd018750a695]
module.network.module.management.module.public_subnet.aws_route_table.public[2]: Refreshing state... [id=rtb-095d5551201e2631e]
module.network.module.management.module.private_subnet.aws_route_table.private[2]: Refreshing state... [id=rtb-0b2f17a06718620be]
module.network.module.management.module.private_subnet.aws_route_table.private[1]: Refreshing state... [id=rtb-00a32c905eba02447]
module.network.module.management.module.private_subnet.aws_route_table.private[0]: Refreshing state... [id=rtb-00a5d8d6338b91e33]
module.network.module.management.module.private_subnet.aws_subnet.private[0]: Refreshing state... [id=subnet-000c2e9bc0fa1f4ad]
module.network.module.management.module.private_subnet.aws_subnet.private[1]: Refreshing state... [id=subnet-0a019a1fb0d5aba75]
module.network.module.management.module.private_subnet.aws_subnet.private[2]: Refreshing state... [id=subnet-0485f887e73a69d40]
module.backend.aws_security_group_rule.backend-from-alb-http: Refreshing state... [id=sgrule-3372377313]
module.backend.aws_security_group_rule.backend-from-alb-health-check: Refreshing state... [id=sgrule-2556693372]
module.network.module.public_subnet.aws_route_table_association.public[0]: Refreshing state... [id=rtbassoc-c83703b1]
module.network.module.public_subnet.aws_route_table_association.public[1]: Refreshing state... [id=rtbassoc-0b62e1e2c1b721ea4]
module.network.module.public_subnet.aws_route_table_association.public[2]: Refreshing state... [id=rtbassoc-00fd5347b4f3b3182]
module.mysql.module.subnets.data.aws_vpc.this: Refreshing state...
module.backend.aws_security_group_rule.ssm_endpoint_from_backend: Refreshing state... [id=sgrule-1886272967]
module.backend.aws_security_group_rule.backend_to_ssm_endpoint: Refreshing state... [id=sgrule-2455676943]
module.network.module.private_subnet.aws_route_table_association.private[2]: Refreshing state... [id=rtbassoc-dd79aaa6]
module.network.module.private_subnet.aws_route_table_association.private[0]: Refreshing state... [id=rtbassoc-7979aa02]
module.network.module.private_subnet.aws_route_table_association.private[1]: Refreshing state... [id=rtbassoc-6375a618]
module.network.module.management.module.public_subnet.aws_route_table_association.public[0]: Refreshing state... [id=rtbassoc-0705bb27327ea3421]
module.network.module.management.module.public_subnet.aws_route_table_association.public[2]: Refreshing state... [id=rtbassoc-0c70dce4713041447]
module.network.module.management.module.public_subnet.aws_route_table_association.public[1]: Refreshing state... [id=rtbassoc-0c7351142f221c655]
module.network.module.management.module.private_subnet.aws_route_table_association.private[0]: Refreshing state... [id=rtbassoc-05ea90604a19a06e3]
module.network.module.management.module.private_subnet.aws_route_table_association.private[1]: Refreshing state... [id=rtbassoc-0cb817938a8ba2087]
module.network.module.management.module.private_subnet.aws_route_table_association.private[2]: Refreshing state... [id=rtbassoc-0cfdc3b0d395859a4]
module.network.module.nat.data.aws_subnet_ids.public: Refreshing state...
module.network.module.management.aws_vpc_endpoint.s3: Refreshing state... [id=vpce-0d077733dd16688af]
module.network.module.management.aws_vpc_endpoint.ssm: Refreshing state... [id=vpce-0eebe69e470d4c103]
module.backend.aws_security_group_rule.mysql-from-backend: Refreshing state... [id=sgrule-3393583181]
module.backend.aws_security_group_rule.backend-to-mysql: Refreshing state... [id=sgrule-3211482754]
module.backend.data.aws_subnet_ids.public: Refreshing state...
module.base.aws_route53_record.cdn-A: Refreshing state... [id=Z25GE9A9NRUR2N_www_A]
module.base.aws_route53_record.cdn-AAAA: Refreshing state... [id=Z25GE9A9NRUR2N_www_AAAA]
module.backend.data.aws_subnet_ids.private: Refreshing state...
module.backend.data.aws_subnet.public[0]: Refreshing state...
module.backend.data.aws_subnet.public[1]: Refreshing state...
module.backend.data.aws_subnet.public[2]: Refreshing state...
module.backend.data.aws_subnet.private[1]: Refreshing state...
module.backend.data.aws_subnet.private[2]: Refreshing state...
module.backend.data.aws_subnet.private[0]: Refreshing state...
module.mysql.module.subnets.aws_subnet.private[1]: Refreshing state... [id=subnet-70a0dd16]
module.mysql.module.subnets.aws_subnet.private[2]: Refreshing state... [id=subnet-60d0ec3b]
module.mysql.module.subnets.aws_route_table.private[1]: Refreshing state... [id=rtb-82722dfb]
module.mysql.module.subnets.aws_subnet.private[0]: Refreshing state... [id=subnet-d5f06d9d]
module.mysql.module.subnets.aws_route_table.private[2]: Refreshing state... [id=rtb-5a702f23]
module.mysql.module.subnets.aws_route_table.private[0]: Refreshing state... [id=rtb-fa702f83]
module.backend.aws_alb.alb: Refreshing state... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:loadbalancer/app/applb-20171106080744451200000003/45bf0d921a80598a]
module.backend.aws_autoscaling_group.backend: Refreshing state... [id=app-backend-asg-20181105004601904200000003]
module.backend.aws_security_group_rule.backend-to-s3-endpoint: Refreshing state... [id=sgrule-1220853808]
module.mysql.aws_db_subnet_group.main_db_subnet_group: Refreshing state... [id=app-mysql-subnet-group-0058e036eab3f18e3d97fe5a7a]
module.mysql.module.subnets.aws_route_table_association.private[2]: Refreshing state... [id=rtbassoc-c36dbeb8]
module.mysql.module.subnets.aws_route_table_association.private[1]: Refreshing state... [id=rtbassoc-486ebd33]
module.mysql.module.subnets.aws_route_table_association.private[0]: Refreshing state... [id=rtbassoc-636cbf18]
module.backend.aws_autoscaling_policy.backend-scaledown: Refreshing state... [id=app-prod-northwest-backend-scaledown-policy]
module.backend.aws_autoscaling_policy.backend-scaleup: Refreshing state... [id=app-prod-northwest-backend-scaleup-policy]
module.mysql.aws_db_instance.main_rds_instance: Refreshing state... [id=app-mysql-0058e036eab3f18e3d97fe5a7b]
module.backend.aws_alb_listener.alb-https: Refreshing state... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/f98b62f677df1e1c]
module.backend.aws_alb_listener.alb-http: Refreshing state... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/a2bb653297384a8e]
aws_route53_record.mysql: Refreshing state... [id=Z1O2JQV3R0LG26_mysql_CNAME]
module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaleup: Refreshing state... [id=app-prod-northwest-backend-scaleup-cpu-alarm]
module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaledown: Refreshing state... [id=app-prod-northwest-backend-scaledown-cpu-alarm]

------------------------------------------------------------------------

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_route53_record.mysql will be destroyed
  - resource "aws_route53_record" "mysql" {
      - allow_overwrite = true -> null
      - fqdn            = "mysql.app.hyperboladc.net" -> null
      - id              = "Z1O2JQV3R0LG26_mysql_CNAME" -> null
      - name            = "mysql" -> null
      - records         = [
          - "app-mysql-0058e036eab3f18e3d97fe5a7b.cpebqrq01cnd.us-west-2.rds.amazonaws.com",
        ] -> null
      - ttl             = 300 -> null
      - type            = "CNAME" -> null
      - zone_id         = "Z1O2JQV3R0LG26" -> null
    }

  # aws_route53_zone.app_dc will be destroyed
  - resource "aws_route53_zone" "app_dc" {
      - comment       = "Managed by Terraform" -> null
      - force_destroy = false -> null
      - id            = "Z1O2JQV3R0LG26" -> null
      - name          = "app.hyperboladc.net." -> null
      - name_servers  = [
          - "ns-0.awsdns-00.com.",
          - "ns-1024.awsdns-00.org.",
          - "ns-1536.awsdns-00.co.uk.",
          - "ns-512.awsdns-00.net.",
        ] -> null
      - tags          = {} -> null
      - vpc_id        = "vpc-08d0186e" -> null
      - vpc_region    = "us-west-2" -> null
      - zone_id       = "Z1O2JQV3R0LG26" -> null

      - vpc {
          - vpc_id     = "vpc-08d0186e" -> null
          - vpc_region = "us-west-2" -> null
        }
    }

  # module.backend.aws_alb.alb will be destroyed
  - resource "aws_alb" "alb" {
      - arn                        = "arn:aws:elasticloadbalancing:us-west-2:473124112471:loadbalancer/app/applb-20171106080744451200000003/45bf0d921a80598a" -> null
      - arn_suffix                 = "app/applb-20171106080744451200000003/45bf0d921a80598a" -> null
      - dns_name                   = "applb-20171106080744451200000003-922647741.us-west-2.elb.amazonaws.com" -> null
      - enable_deletion_protection = false -> null
      - enable_http2               = true -> null
      - id                         = "arn:aws:elasticloadbalancing:us-west-2:473124112471:loadbalancer/app/applb-20171106080744451200000003/45bf0d921a80598a" -> null
      - idle_timeout               = 60 -> null
      - internal                   = false -> null
      - ip_address_type            = "dualstack" -> null
      - load_balancer_type         = "application" -> null
      - name                       = "applb-20171106080744451200000003" -> null
      - name_prefix                = "applb-" -> null
      - security_groups            = [
          - "sg-d88caea5",
        ] -> null
      - subnets                    = [
          - "subnet-113a864a",
          - "subnet-bfe7fdd8",
          - "subnet-dc043895",
        ] -> null
      - tags                       = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-alb"
        } -> null
      - vpc_id                     = "vpc-08d0186e" -> null
      - zone_id                    = "Z1H1FL5HABSF5" -> null

      - access_logs {
          - enabled = false -> null
        }

      - subnet_mapping {
          - subnet_id = "subnet-113a864a" -> null
        }
      - subnet_mapping {
          - subnet_id = "subnet-bfe7fdd8" -> null
        }
      - subnet_mapping {
          - subnet_id = "subnet-dc043895" -> null
        }

      - timeouts {}
    }

  # module.backend.aws_alb_listener.alb-http will be destroyed
  - resource "aws_alb_listener" "alb-http" {
      - arn               = "arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/a2bb653297384a8e" -> null
      - id                = "arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/a2bb653297384a8e" -> null
      - load_balancer_arn = "arn:aws:elasticloadbalancing:us-west-2:473124112471:loadbalancer/app/applb-20171106080744451200000003/45bf0d921a80598a" -> null
      - port              = 80 -> null
      - protocol          = "HTTP" -> null

      - default_action {
          - order            = 0 -> null
          - target_group_arn = "arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02" -> null
          - type             = "forward" -> null
        }

      - timeouts {}
    }

  # module.backend.aws_alb_listener.alb-https will be destroyed
  - resource "aws_alb_listener" "alb-https" {
      - arn               = "arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/f98b62f677df1e1c" -> null
      - certificate_arn   = "arn:aws:acm:us-west-2:473124112471:certificate/ebb1e8c3-393d-4941-8410-af814e775159" -> null
      - id                = "arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/f98b62f677df1e1c" -> null
      - load_balancer_arn = "arn:aws:elasticloadbalancing:us-west-2:473124112471:loadbalancer/app/applb-20171106080744451200000003/45bf0d921a80598a" -> null
      - port              = 443 -> null
      - protocol          = "HTTPS" -> null
      - ssl_policy        = "ELBSecurityPolicy-TLS-1-2-2017-01" -> null

      - default_action {
          - order            = 0 -> null
          - target_group_arn = "arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02" -> null
          - type             = "forward" -> null
        }

      - timeouts {}
    }

  # module.backend.aws_alb_target_group.backend will be destroyed
  - resource "aws_alb_target_group" "backend" {
      - arn                                = "arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02" -> null
      - arn_suffix                         = "targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02" -> null
      - deregistration_delay               = 30 -> null
      - id                                 = "arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02" -> null
      - lambda_multi_value_headers_enabled = false -> null
      - load_balancing_algorithm_type      = "round_robin" -> null
      - name                               = "apptg-20171106080741745400000001" -> null
      - name_prefix                        = "apptg-" -> null
      - port                               = 80 -> null
      - protocol                           = "HTTP" -> null
      - proxy_protocol_v2                  = false -> null
      - slow_start                         = 0 -> null
      - tags                               = {} -> null
      - target_type                        = "instance" -> null
      - vpc_id                             = "vpc-08d0186e" -> null

      - health_check {
          - enabled             = true -> null
          - healthy_threshold   = 3 -> null
          - interval            = 30 -> null
          - matcher             = "200" -> null
          - path                = "/healthz" -> null
          - port                = "8888" -> null
          - protocol            = "HTTP" -> null
          - timeout             = 5 -> null
          - unhealthy_threshold = 3 -> null
        }

      - stickiness {
          - cookie_duration = 86400 -> null
          - enabled         = false -> null
          - type            = "lb_cookie" -> null
        }
    }

  # module.backend.aws_autoscaling_group.backend will be destroyed
  - resource "aws_autoscaling_group" "backend" {
      - arn                       = "arn:aws:autoscaling:us-west-2:473124112471:autoScalingGroup:7a95b0ae-fde3-4dc9-9594-a519f126b037:autoScalingGroupName/app-backend-asg-20181105004601904200000003" -> null
      - availability_zones        = [
          - "us-west-2a",
          - "us-west-2b",
          - "us-west-2c",
        ] -> null
      - default_cooldown          = 300 -> null
      - desired_capacity          = 1 -> null
      - enabled_metrics           = [] -> null
      - force_delete              = false -> null
      - health_check_grace_period = 300 -> null
      - health_check_type         = "EC2" -> null
      - id                        = "app-backend-asg-20181105004601904200000003" -> null
      - load_balancers            = [] -> null
      - max_instance_lifetime     = 0 -> null
      - max_size                  = 3 -> null
      - metrics_granularity       = "1Minute" -> null
      - min_size                  = 1 -> null
      - name                      = "app-backend-asg-20181105004601904200000003" -> null
      - name_prefix               = "app-backend-asg-" -> null
      - protect_from_scale_in     = false -> null
      - service_linked_role_arn   = "arn:aws:iam::473124112471:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling" -> null
      - suspended_processes       = [] -> null
      - target_group_arns         = [
          - "arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02",
        ] -> null
      - termination_policies      = [] -> null
      - vpc_zone_identifier       = [
          - "subnet-2a3d8171",
          - "subnet-400a3609",
          - "subnet-46e7fd21",
        ] -> null
      - wait_for_capacity_timeout = "10m" -> null
      - wait_for_elb_capacity     = 1 -> null

      - launch_template {
          - id      = "lt-0d1bd9f990ac86bda" -> null
          - name    = "app-backend-lc-20181105004601132100000001" -> null
          - version = "$Latest" -> null
        }

      - timeouts {}
    }

  # module.backend.aws_autoscaling_policy.backend-scaledown will be destroyed
  - resource "aws_autoscaling_policy" "backend-scaledown" {
      - adjustment_type           = "ChangeInCapacity" -> null
      - arn                       = "arn:aws:autoscaling:us-west-2:473124112471:scalingPolicy:7773b3cc-4a4e-4ca8-a5c6-e9c6e45907f5:autoScalingGroupName/app-backend-asg-20181105004601904200000003:policyName/app-prod-northwest-backend-scaledown-policy" -> null
      - autoscaling_group_name    = "app-backend-asg-20181105004601904200000003" -> null
      - cooldown                  = 300 -> null
      - estimated_instance_warmup = 0 -> null
      - id                        = "app-prod-northwest-backend-scaledown-policy" -> null
      - min_adjustment_step       = 0 -> null
      - name                      = "app-prod-northwest-backend-scaledown-policy" -> null
      - policy_type               = "SimpleScaling" -> null
      - scaling_adjustment        = -1 -> null
    }

  # module.backend.aws_autoscaling_policy.backend-scaleup will be destroyed
  - resource "aws_autoscaling_policy" "backend-scaleup" {
      - adjustment_type           = "ChangeInCapacity" -> null
      - arn                       = "arn:aws:autoscaling:us-west-2:473124112471:scalingPolicy:a7fa9503-7f91-4987-b5e2-a691f94f8115:autoScalingGroupName/app-backend-asg-20181105004601904200000003:policyName/app-prod-northwest-backend-scaleup-policy" -> null
      - autoscaling_group_name    = "app-backend-asg-20181105004601904200000003" -> null
      - cooldown                  = 300 -> null
      - estimated_instance_warmup = 0 -> null
      - id                        = "app-prod-northwest-backend-scaleup-policy" -> null
      - min_adjustment_step       = 0 -> null
      - name                      = "app-prod-northwest-backend-scaleup-policy" -> null
      - policy_type               = "SimpleScaling" -> null
      - scaling_adjustment        = 1 -> null
    }

  # module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaledown will be destroyed
  - resource "aws_cloudwatch_metric_alarm" "backend-cpu-scaledown" {
      - actions_enabled           = true -> null
      - alarm_actions             = [
          - "arn:aws:autoscaling:us-west-2:473124112471:scalingPolicy:7773b3cc-4a4e-4ca8-a5c6-e9c6e45907f5:autoScalingGroupName/app-backend-asg-20181105004601904200000003:policyName/app-prod-northwest-backend-scaledown-policy",
        ] -> null
      - alarm_name                = "app-prod-northwest-backend-scaledown-cpu-alarm" -> null
      - arn                       = "arn:aws:cloudwatch:us-west-2:473124112471:alarm:app-prod-northwest-backend-scaledown-cpu-alarm" -> null
      - comparison_operator       = "LessThanOrEqualToThreshold" -> null
      - datapoints_to_alarm       = 0 -> null
      - dimensions                = {
          - "AutoScalingGroupName" = "app-backend-asg-20181105004601904200000003"
        } -> null
      - evaluation_periods        = 2 -> null
      - id                        = "app-prod-northwest-backend-scaledown-cpu-alarm" -> null
      - insufficient_data_actions = [] -> null
      - metric_name               = "CPUUtilization" -> null
      - namespace                 = "AWS/EC2" -> null
      - ok_actions                = [] -> null
      - period                    = 120 -> null
      - statistic                 = "Average" -> null
      - tags                      = {} -> null
      - threshold                 = 20 -> null
      - treat_missing_data        = "missing" -> null
    }

  # module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaleup will be destroyed
  - resource "aws_cloudwatch_metric_alarm" "backend-cpu-scaleup" {
      - actions_enabled           = true -> null
      - alarm_actions             = [
          - "arn:aws:autoscaling:us-west-2:473124112471:scalingPolicy:a7fa9503-7f91-4987-b5e2-a691f94f8115:autoScalingGroupName/app-backend-asg-20181105004601904200000003:policyName/app-prod-northwest-backend-scaleup-policy",
        ] -> null
      - alarm_name                = "app-prod-northwest-backend-scaleup-cpu-alarm" -> null
      - arn                       = "arn:aws:cloudwatch:us-west-2:473124112471:alarm:app-prod-northwest-backend-scaleup-cpu-alarm" -> null
      - comparison_operator       = "GreaterThanOrEqualToThreshold" -> null
      - datapoints_to_alarm       = 0 -> null
      - dimensions                = {
          - "AutoScalingGroupName" = "app-backend-asg-20181105004601904200000003"
        } -> null
      - evaluation_periods        = 2 -> null
      - id                        = "app-prod-northwest-backend-scaleup-cpu-alarm" -> null
      - insufficient_data_actions = [] -> null
      - metric_name               = "CPUUtilization" -> null
      - namespace                 = "AWS/EC2" -> null
      - ok_actions                = [] -> null
      - period                    = 120 -> null
      - statistic                 = "Average" -> null
      - tags                      = {} -> null
      - threshold                 = 60 -> null
      - treat_missing_data        = "missing" -> null
    }

  # module.backend.aws_launch_template.backend will be destroyed
  - resource "aws_launch_template" "backend" {
      - arn                     = "arn:aws:ec2:us-west-2:473124112471:launch-template/lt-0d1bd9f990ac86bda" -> null
      - default_version         = 1 -> null
      - disable_api_termination = false -> null
      - ebs_optimized           = "true" -> null
      - id                      = "lt-0d1bd9f990ac86bda" -> null
      - image_id                = "ami-0f554629c8c210b85" -> null
      - instance_type           = "t3.nano" -> null
      - latest_version          = 20 -> null
      - name                    = "app-backend-lc-20181105004601132100000001" -> null
      - name_prefix             = "app-backend-lc-" -> null
      - security_group_names    = [] -> null
      - tags                    = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-backend"
        } -> null
      - vpc_security_group_ids  = [
          - "sg-5ffd4125",
        ] -> null

      - iam_instance_profile {
          - name = "app-profile-00f8d1802132e948040476a3b1" -> null
        }

      - instance_market_options {
          - market_type = "spot" -> null

          - spot_options {
              - block_duration_minutes = 0 -> null
              - max_price              = "0.0052" -> null
            }
        }

      - monitoring {
          - enabled = false -> null
        }

      - tag_specifications {
          - resource_type = "instance" -> null
          - tags          = {
              - "Environment" = "production"
              - "Name"        = "app-prod-northwest-backend"
              - "Version"     = "0.159.0"
            } -> null
        }
    }

  # module.backend.aws_security_group.alb will be destroyed
  - resource "aws_security_group" "alb" {
      - arn                    = "arn:aws:ec2:us-west-2:473124112471:security-group/sg-d88caea5" -> null
      - description            = "Managed by Terraform" -> null
      - egress                 = [
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-5ffd4125",
                ]
              - self             = false
              - to_port          = 80
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 8888
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-5ffd4125",
                ]
              - self             = false
              - to_port          = 8888
            },
        ] -> null
      - id                     = "sg-d88caea5" -> null
      - ingress                = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 443
              - ipv6_cidr_blocks = [
                  - "::/0",
                ]
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 443
            },
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = [
                  - "::/0",
                ]
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 80
            },
        ] -> null
      - name                   = "app-alb-sg-20171106080741747400000002" -> null
      - name_prefix            = "app-alb-sg-" -> null
      - owner_id               = "473124112471" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-alb-sg"
        } -> null
      - vpc_id                 = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.backend.aws_security_group.backend will be destroyed
  - resource "aws_security_group" "backend" {
      - arn                    = "arn:aws:ec2:us-west-2:473124112471:security-group/sg-5ffd4125" -> null
      - description            = "Managed by Terraform" -> null
      - egress                 = [
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = [
                  - "pl-68a54001",
                ]
              - protocol         = "-1"
              - security_groups  = []
              - self             = false
              - to_port          = 0
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "-1"
              - security_groups  = [
                  - "sg-0258424690602bd25",
                ]
              - self             = false
              - to_port          = 0
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 3306
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-a2381cdf",
                ]
              - self             = false
              - to_port          = 3306
            },
        ] -> null
      - id                     = "sg-5ffd4125" -> null
      - ingress                = [
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-d88caea5",
                ]
              - self             = false
              - to_port          = 80
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 8888
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-d88caea5",
                ]
              - self             = false
              - to_port          = 8888
            },
        ] -> null
      - name                   = "app-backend-sg-00ba465879944ffeffaef34926" -> null
      - name_prefix            = "app-backend-sg-" -> null
      - owner_id               = "473124112471" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-backend-sg"
        } -> null
      - vpc_id                 = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.backend.aws_security_group_rule.backend-from-alb-health-check will be destroyed
  - resource "aws_security_group_rule" "backend-from-alb-health-check" {
      - cidr_blocks              = [] -> null
      - from_port                = 8888 -> null
      - id                       = "sgrule-2556693372" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-5ffd4125" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-d88caea5" -> null
      - to_port                  = 8888 -> null
      - type                     = "ingress" -> null
    }

  # module.backend.aws_security_group_rule.backend-from-alb-http will be destroyed
  - resource "aws_security_group_rule" "backend-from-alb-http" {
      - cidr_blocks              = [] -> null
      - from_port                = 80 -> null
      - id                       = "sgrule-3372377313" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-5ffd4125" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-d88caea5" -> null
      - to_port                  = 80 -> null
      - type                     = "ingress" -> null
    }

  # module.backend.aws_security_group_rule.backend-to-mysql will be destroyed
  - resource "aws_security_group_rule" "backend-to-mysql" {
      - cidr_blocks              = [] -> null
      - from_port                = 3306 -> null
      - id                       = "sgrule-3211482754" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-5ffd4125" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-a2381cdf" -> null
      - to_port                  = 3306 -> null
      - type                     = "egress" -> null
    }

  # module.backend.aws_security_group_rule.backend-to-s3-endpoint will be destroyed
  - resource "aws_security_group_rule" "backend-to-s3-endpoint" {
      - cidr_blocks       = [] -> null
      - from_port         = 0 -> null
      - id                = "sgrule-1220853808" -> null
      - ipv6_cidr_blocks  = [] -> null
      - prefix_list_ids   = [
          - "pl-68a54001",
        ] -> null
      - protocol          = "-1" -> null
      - security_group_id = "sg-5ffd4125" -> null
      - self              = false -> null
      - to_port           = 0 -> null
      - type              = "egress" -> null
    }

  # module.backend.aws_security_group_rule.backend_to_ssm_endpoint will be destroyed
  - resource "aws_security_group_rule" "backend_to_ssm_endpoint" {
      - cidr_blocks              = [] -> null
      - from_port                = 0 -> null
      - id                       = "sgrule-2455676943" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "-1" -> null
      - security_group_id        = "sg-5ffd4125" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-0258424690602bd25" -> null
      - to_port                  = 0 -> null
      - type                     = "egress" -> null
    }

  # module.backend.aws_security_group_rule.mysql-from-backend will be destroyed
  - resource "aws_security_group_rule" "mysql-from-backend" {
      - cidr_blocks              = [] -> null
      - from_port                = 3306 -> null
      - id                       = "sgrule-3393583181" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-a2381cdf" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-5ffd4125" -> null
      - to_port                  = 3306 -> null
      - type                     = "ingress" -> null
    }

  # module.backend.aws_security_group_rule.ssm_endpoint_from_backend will be destroyed
  - resource "aws_security_group_rule" "ssm_endpoint_from_backend" {
      - cidr_blocks              = [] -> null
      - from_port                = 0 -> null
      - id                       = "sgrule-1886272967" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "-1" -> null
      - security_group_id        = "sg-0258424690602bd25" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-5ffd4125" -> null
      - to_port                  = 0 -> null
      - type                     = "ingress" -> null
    }

  # module.base.aws_cloudfront_distribution.cdn will be destroyed
  - resource "aws_cloudfront_distribution" "cdn" {
      - active_trusted_signers         = {
          - "enabled" = "false"
          - "items.#" = "0"
        } -> null
      - aliases                        = [
          - "www.hyperbolausercontent.net",
        ] -> null
      - arn                            = "arn:aws:cloudfront::473124112471:distribution/E2KESP33B8DNIU" -> null
      - caller_reference               = "2017-07-16T15:38:26.626264616-07:00" -> null
      - comment                        = "CloudFront for hyperbola-app cdn - production" -> null
      - domain_name                    = "drk9p6kxy4a37.cloudfront.net" -> null
      - enabled                        = true -> null
      - etag                           = "EY4S4YCN3OKS1" -> null
      - hosted_zone_id                 = "Z2FDTNDATAQYW2" -> null
      - http_version                   = "http2" -> null
      - id                             = "E2KESP33B8DNIU" -> null
      - in_progress_validation_batches = 0 -> null
      - is_ipv6_enabled                = true -> null
      - last_modified_time             = "2017-11-19 04:09:36.548 +0000 UTC" -> null
      - price_class                    = "PriceClass_100" -> null
      - retain_on_delete               = false -> null
      - status                         = "Deployed" -> null
      - tags                           = {
          - "Environment" = "production"
        } -> null
      - wait_for_deployment            = true -> null

      - default_cache_behavior {
          - allowed_methods        = [
              - "DELETE",
              - "GET",
              - "HEAD",
              - "OPTIONS",
              - "PATCH",
              - "POST",
              - "PUT",
            ] -> null
          - cached_methods         = [
              - "GET",
              - "HEAD",
            ] -> null
          - compress               = false -> null
          - default_ttl            = 3600 -> null
          - max_ttl                = 86400 -> null
          - min_ttl                = 0 -> null
          - smooth_streaming       = false -> null
          - target_origin_id       = "s3-media" -> null
          - trusted_signers        = [] -> null
          - viewer_protocol_policy = "https-only" -> null

          - forwarded_values {
              - headers                 = [] -> null
              - query_string            = false -> null
              - query_string_cache_keys = [] -> null

              - cookies {
                  - forward           = "none" -> null
                  - whitelisted_names = [] -> null
                }
            }
        }

      - origin {
          - domain_name = "www.hyperbolausercontent.net.s3.amazonaws.com" -> null
          - origin_id   = "s3-media" -> null
        }

      - restrictions {
          - geo_restriction {
              - locations        = [] -> null
              - restriction_type = "none" -> null
            }
        }

      - viewer_certificate {
          - acm_certificate_arn            = "arn:aws:acm:us-east-1:473124112471:certificate/ec75af41-df70-41d7-9766-01c71c80f0d3" -> null
          - cloudfront_default_certificate = false -> null
          - minimum_protocol_version       = "TLSv1.2_2018" -> null
          - ssl_support_method             = "sni-only" -> null
        }
    }

  # module.base.aws_iam_instance_profile.app will be destroyed
  - resource "aws_iam_instance_profile" "app" {
      - arn         = "arn:aws:iam::473124112471:instance-profile/app-profile-00f8d1802132e948040476a3b1" -> null
      - create_date = "2017-07-21T06:17:20Z" -> null
      - id          = "app-profile-00f8d1802132e948040476a3b1" -> null
      - name        = "app-profile-00f8d1802132e948040476a3b1" -> null
      - name_prefix = "app-profile-" -> null
      - path        = "/" -> null
      - role        = "app-role-00f8d1802132e948040476a3b0" -> null
      - roles       = [
          - "app-role-00f8d1802132e948040476a3b0",
        ] -> null
      - unique_id   = "AIPAIWNBNTHNR6PMCMXVQ" -> null
    }

  # module.base.aws_iam_role.app will be destroyed
  - resource "aws_iam_role" "app" {
      - arn                   = "arn:aws:iam::473124112471:role/app-role-00f8d1802132e948040476a3b0" -> null
      - assume_role_policy    = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = "sts:AssumeRole"
                      - Effect    = "Allow"
                      - Principal = {
                          - Service = "ec2.amazonaws.com"
                        }
                      - Sid       = "AppAssumeRole"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - create_date           = "2017-07-21T06:17:19Z" -> null
      - force_detach_policies = false -> null
      - id                    = "app-role-00f8d1802132e948040476a3b0" -> null
      - max_session_duration  = 3600 -> null
      - name                  = "app-role-00f8d1802132e948040476a3b0" -> null
      - name_prefix           = "app-role-" -> null
      - path                  = "/" -> null
      - tags                  = {} -> null
      - unique_id             = "AROAJR5B5YNSIOFJ4DKI6" -> null
    }

  # module.base.aws_iam_role_policy.app will be destroyed
  - resource "aws_iam_role_policy" "app" {
      - id          = "app-role-00f8d1802132e948040476a3b0:app-policy-00f8d1802132e948040476a3b2" -> null
      - name        = "app-policy-00f8d1802132e948040476a3b2" -> null
      - name_prefix = "app-policy-" -> null
      - policy      = jsonencode(
            {
              - Statement = [
                  - {
                      - Action   = [
                          - "s3:ListBucket",
                          - "s3:GetBucketLocation",
                        ]
                      - Effect   = "Allow"
                      - Resource = [
                          - "arn:aws:s3:::www.hyperbolausercontent.net",
                          - "arn:aws:s3:::hyperbola-app-backup-production",
                        ]
                      - Sid      = "AllowAppBucketPermissions"
                    },
                  - {
                      - Action   = [
                          - "s3:*Object*",
                        ]
                      - Effect   = "Allow"
                      - Resource = [
                          - "arn:aws:s3:::www.hyperbolausercontent.net/*",
                          - "arn:aws:s3:::hyperbola-app-backup-production/*",
                        ]
                      - Sid      = "AllowAppBucketContentPermissions"
                    },
                  - {
                      - Action   = [
                          - "ssm:GetParametersByPath",
                        ]
                      - Effect   = "Allow"
                      - Resource = [
                          - "arn:aws:ssm:*:*:parameter/app/production/*",
                        ]
                      - Sid      = "AllowSecretsAccess"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - role        = "app-role-00f8d1802132e948040476a3b0" -> null
    }

  # module.base.aws_route53_record.cdn-A will be destroyed
  - resource "aws_route53_record" "cdn-A" {
      - allow_overwrite = true -> null
      - fqdn            = "www.hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_www_A" -> null
      - name            = "www" -> null
      - records         = [] -> null
      - ttl             = 0 -> null
      - type            = "A" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null

      - alias {
          - evaluate_target_health = false -> null
          - name                   = "drk9p6kxy4a37.cloudfront.net" -> null
          - zone_id                = "Z2FDTNDATAQYW2" -> null
        }
    }

  # module.base.aws_route53_record.cdn-AAAA will be destroyed
  - resource "aws_route53_record" "cdn-AAAA" {
      - allow_overwrite = true -> null
      - fqdn            = "www.hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_www_AAAA" -> null
      - name            = "www" -> null
      - records         = [] -> null
      - ttl             = 0 -> null
      - type            = "AAAA" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null

      - alias {
          - evaluate_target_health = false -> null
          - name                   = "drk9p6kxy4a37.cloudfront.net" -> null
          - zone_id                = "Z2FDTNDATAQYW2" -> null
        }
    }

  # module.mysql.aws_db_instance.main_rds_instance will be destroyed
  - resource "aws_db_instance" "main_rds_instance" {
      - address                               = "app-mysql-0058e036eab3f18e3d97fe5a7b.cpebqrq01cnd.us-west-2.rds.amazonaws.com" -> null
      - allocated_storage                     = 5 -> null
      - allow_major_version_upgrade           = false -> null
      - apply_immediately                     = true -> null
      - arn                                   = "arn:aws:rds:us-west-2:473124112471:db:app-mysql-0058e036eab3f18e3d97fe5a7b" -> null
      - auto_minor_version_upgrade            = true -> null
      - availability_zone                     = "us-west-2c" -> null
      - backup_retention_period               = 10 -> null
      - backup_window                         = "09:22-09:52" -> null
      - ca_cert_identifier                    = "rds-ca-2019" -> null
      - copy_tags_to_snapshot                 = false -> null
      - db_subnet_group_name                  = "app-mysql-subnet-group-0058e036eab3f18e3d97fe5a7a" -> null
      - delete_automated_backups              = true -> null
      - deletion_protection                   = false -> null
      - enabled_cloudwatch_logs_exports       = [] -> null
      - endpoint                              = "app-mysql-0058e036eab3f18e3d97fe5a7b.cpebqrq01cnd.us-west-2.rds.amazonaws.com:3306" -> null
      - engine                                = "mysql" -> null
      - engine_version                        = "5.7.19" -> null
      - final_snapshot_identifier             = "app-mysql-final-snapshot" -> null
      - hosted_zone_id                        = "Z1PVIF0B656C1W" -> null
      - iam_database_authentication_enabled   = false -> null
      - id                                    = "app-mysql-0058e036eab3f18e3d97fe5a7b" -> null
      - identifier                            = "app-mysql-0058e036eab3f18e3d97fe5a7b" -> null
      - identifier_prefix                     = "app-mysql-" -> null
      - instance_class                        = "db.t2.micro" -> null
      - iops                                  = 0 -> null
      - license_model                         = "general-public-license" -> null
      - maintenance_window                    = "sun:10:18-sun:10:48" -> null
      - max_allocated_storage                 = 0 -> null
      - monitoring_interval                   = 0 -> null
      - multi_az                              = false -> null
      - name                                  = "hyperbola" -> null
      - option_group_name                     = "default:mysql-5-7" -> null
      - parameter_group_name                  = "app-mysql-custom-params-0058e036eab3f18e3d97fe5a79" -> null
      - password                              = (sensitive value)
      - performance_insights_enabled          = false -> null
      - performance_insights_retention_period = 0 -> null
      - port                                  = 3306 -> null
      - publicly_accessible                   = false -> null
      - replicas                              = [] -> null
      - resource_id                           = "db-DQM3UVZ7THHR4QKWQZ4TEEOBAM" -> null
      - security_group_names                  = [] -> null
      - skip_final_snapshot                   = false -> null
      - status                                = "available" -> null
      - storage_encrypted                     = false -> null
      - storage_type                          = "gp2" -> null
      - tags                                  = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-mysql"
        } -> null
      - username                              = "app" -> null
      - vpc_security_group_ids                = [
          - "sg-a2381cdf",
        ] -> null

      - timeouts {}
    }

  # module.mysql.aws_db_parameter_group.main_rds_instance will be destroyed
  - resource "aws_db_parameter_group" "main_rds_instance" {
      - arn         = "arn:aws:rds:us-west-2:473124112471:pg:app-mysql-custom-params-0058e036eab3f18e3d97fe5a79" -> null
      - description = "Managed by Terraform" -> null
      - family      = "mysql5.7" -> null
      - id          = "app-mysql-custom-params-0058e036eab3f18e3d97fe5a79" -> null
      - name        = "app-mysql-custom-params-0058e036eab3f18e3d97fe5a79" -> null
      - name_prefix = "app-mysql-custom-params-" -> null
      - tags        = {
          - "Environment" = "production"
        } -> null

      - parameter {
          - apply_method = "immediate" -> null
          - name         = "character_set_client" -> null
          - value        = "utf8mb4" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "character_set_connection" -> null
          - value        = "utf8mb4" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "character_set_database" -> null
          - value        = "utf8mb4" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "character_set_results" -> null
          - value        = "utf8mb4" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "character_set_server" -> null
          - value        = "utf8mb4" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "collation_connection" -> null
          - value        = "utf8mb4_unicode_ci" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "collation_server" -> null
          - value        = "utf8mb4_unicode_ci" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "innodb_strict_mode" -> null
          - value        = "1" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "sql_mode" -> null
          - value        = "traditional" -> null
        }
    }

  # module.mysql.aws_db_subnet_group.main_db_subnet_group will be destroyed
  - resource "aws_db_subnet_group" "main_db_subnet_group" {
      - arn         = "arn:aws:rds:us-west-2:473124112471:subgrp:app-mysql-subnet-group-0058e036eab3f18e3d97fe5a7a" -> null
      - description = "RDS subnet group" -> null
      - id          = "app-mysql-subnet-group-0058e036eab3f18e3d97fe5a7a" -> null
      - name        = "app-mysql-subnet-group-0058e036eab3f18e3d97fe5a7a" -> null
      - name_prefix = "app-mysql-subnet-group-" -> null
      - subnet_ids  = [
          - "subnet-60d0ec3b",
          - "subnet-70a0dd16",
          - "subnet-d5f06d9d",
        ] -> null
      - tags        = {
          - "Environment" = "production"
        } -> null
    }

  # module.mysql.aws_security_group.main_db_access will be destroyed
  - resource "aws_security_group" "main_db_access" {
      - arn                    = "arn:aws:ec2:us-west-2:473124112471:security-group/sg-a2381cdf" -> null
      - description            = "Allow access to the database" -> null
      - egress                 = [] -> null
      - id                     = "sg-a2381cdf" -> null
      - ingress                = [
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 3306
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-5ffd4125",
                ]
              - self             = false
              - to_port          = 3306
            },
        ] -> null
      - name                   = "app-mysql-sg-0058e036eab3f18e3d97fe5a78" -> null
      - name_prefix            = "app-mysql-sg-" -> null
      - owner_id               = "473124112471" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-mysql-sg"
        } -> null
      - vpc_id                 = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.aws_network_acl.acl will be destroyed
  - resource "aws_network_acl" "acl" {
      - egress     = [
          - {
              - action          = "allow"
              - cidr_block      = ""
              - from_port       = 0
              - icmp_code       = 0
              - icmp_type       = 0
              - ipv6_cidr_block = "::/0"
              - protocol        = "-1"
              - rule_no         = 200
              - to_port         = 0
            },
          - {
              - action          = "allow"
              - cidr_block      = "0.0.0.0/0"
              - from_port       = 0
              - icmp_code       = 0
              - icmp_type       = 0
              - ipv6_cidr_block = ""
              - protocol        = "-1"
              - rule_no         = 100
              - to_port         = 0
            },
        ] -> null
      - id         = "acl-4e77e428" -> null
      - ingress    = [
          - {
              - action          = "allow"
              - cidr_block      = ""
              - from_port       = 0
              - icmp_code       = 0
              - icmp_type       = 0
              - ipv6_cidr_block = "::/0"
              - protocol        = "-1"
              - rule_no         = 200
              - to_port         = 0
            },
          - {
              - action          = "allow"
              - cidr_block      = "0.0.0.0/0"
              - from_port       = 0
              - icmp_code       = 0
              - icmp_type       = 0
              - ipv6_cidr_block = ""
              - protocol        = "-1"
              - rule_no         = 100
              - to_port         = 0
            },
        ] -> null
      - owner_id   = "473124112471" -> null
      - subnet_ids = [
          - "subnet-113a864a",
          - "subnet-2a3d8171",
          - "subnet-400a3609",
          - "subnet-46e7fd21",
          - "subnet-bfe7fdd8",
          - "subnet-dc043895",
        ] -> null
      - tags       = {
          - "Name" = "app-prod-northwest-all"
        } -> null
      - vpc_id     = "vpc-08d0186e" -> null
    }

  # module.secrets.aws_ssm_parameter.database_password will be destroyed
  - resource "aws_ssm_parameter" "database_password" {
      - arn         = "arn:aws:ssm:us-west-2:473124112471:parameter/app/production/DB_PASSWORD" -> null
      - description = "App database password" -> null
      - id          = "/app/production/DB_PASSWORD" -> null
      - key_id      = "alias/aws/ssm" -> null
      - name        = "/app/production/DB_PASSWORD" -> null
      - tags        = {
          - "Environment" = "production"
          - "Project"     = "app"
        } -> null
      - tier        = "Standard" -> null
      - type        = "SecureString" -> null
      - value       = (sensitive value)
      - version     = 1 -> null
    }

  # module.secrets.aws_ssm_parameter.secret_key will be destroyed
  - resource "aws_ssm_parameter" "secret_key" {
      - arn         = "arn:aws:ssm:us-west-2:473124112471:parameter/app/production/SECRET_KEY" -> null
      - description = "Django secret key" -> null
      - id          = "/app/production/SECRET_KEY" -> null
      - key_id      = "alias/aws/ssm" -> null
      - name        = "/app/production/SECRET_KEY" -> null
      - tags        = {
          - "Environment" = "production"
          - "Project"     = "app"
        } -> null
      - tier        = "Standard" -> null
      - type        = "SecureString" -> null
      - value       = (sensitive value)
      - version     = 1 -> null
    }

  # module.mysql.module.subnets.aws_route_table.private[0] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-fa702f83" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-mysql.us-west-2a"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.mysql.module.subnets.aws_route_table.private[1] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-82722dfb" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-mysql.us-west-2b"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.mysql.module.subnets.aws_route_table.private[2] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-5a702f23" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-mysql.us-west-2c"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.mysql.module.subnets.aws_route_table_association.private[0] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-636cbf18" -> null
      - route_table_id = "rtb-fa702f83" -> null
      - subnet_id      = "subnet-d5f06d9d" -> null
    }

  # module.mysql.module.subnets.aws_route_table_association.private[1] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-486ebd33" -> null
      - route_table_id = "rtb-82722dfb" -> null
      - subnet_id      = "subnet-70a0dd16" -> null
    }

  # module.mysql.module.subnets.aws_route_table_association.private[2] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-c36dbeb8" -> null
      - route_table_id = "rtb-5a702f23" -> null
      - subnet_id      = "subnet-60d0ec3b" -> null
    }

  # module.mysql.module.subnets.aws_subnet.private[0] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-d5f06d9d" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2a" -> null
      - availability_zone_id            = "usw2-az2" -> null
      - cidr_block                      = "10.149.160.0/24" -> null
      - id                              = "subnet-d5f06d9d" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a5a0::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-8b7871f3" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-mysql.us-west-2a"
          - "Network" = "subnet-tier-5"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.mysql.module.subnets.aws_subnet.private[1] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-70a0dd16" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2b" -> null
      - availability_zone_id            = "usw2-az1" -> null
      - cidr_block                      = "10.149.161.0/24" -> null
      - id                              = "subnet-70a0dd16" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a5a1::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-eecd2d87" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-mysql.us-west-2b"
          - "Network" = "subnet-tier-5"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.mysql.module.subnets.aws_subnet.private[2] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-60d0ec3b" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2c" -> null
      - availability_zone_id            = "usw2-az3" -> null
      - cidr_block                      = "10.149.162.0/24" -> null
      - id                              = "subnet-60d0ec3b" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a5a2::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-4389ab09" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-mysql.us-west-2c"
          - "Network" = "subnet-tier-5"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.aws_security_group.ssm will be destroyed
  - resource "aws_security_group" "ssm" {
      - arn                    = "arn:aws:ec2:us-west-2:473124112471:security-group/sg-0258424690602bd25" -> null
      - description            = "SSM VPC Endpoint Security Group" -> null
      - egress                 = [] -> null
      - id                     = "sg-0258424690602bd25" -> null
      - ingress                = [
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "-1"
              - security_groups  = [
                  - "sg-053efd7127835f9c3",
                ]
              - self             = false
              - to_port          = 0
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "-1"
              - security_groups  = [
                  - "sg-5ffd4125",
                ]
              - self             = false
              - to_port          = 0
            },
        ] -> null
      - name                   = "ssm-sg-20181112012252024800000001" -> null
      - name_prefix            = "ssm-sg-" -> null
      - owner_id               = "473124112471" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {} -> null
      - vpc_id                 = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.aws_security_group.this will be destroyed
  - resource "aws_security_group" "this" {
      - arn                    = "arn:aws:ec2:us-west-2:473124112471:security-group/sg-053efd7127835f9c3" -> null
      - description            = "Management Domain Security Group" -> null
      - egress                 = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 443
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 443
            },
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 80
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 443
              - ipv6_cidr_blocks = [
                  - "::/0",
                ]
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 443
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 443
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-0258424690602bd25",
                ]
              - self             = false
              - to_port          = 443
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = [
                  - "::/0",
                ]
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 80
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-0258424690602bd25",
                ]
              - self             = false
              - to_port          = 80
            },
        ] -> null
      - id                     = "sg-053efd7127835f9c3" -> null
      - ingress                = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 22
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 22
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 22
              - ipv6_cidr_blocks = [
                  - "::/0",
                ]
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 22
            },
        ] -> null
      - name                   = "management-sg-20181111224432945200000001" -> null
      - name_prefix            = "management-sg-" -> null
      - owner_id               = "473124112471" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Class" = "management"
        } -> null
      - vpc_id                 = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.aws_security_group_rule.ssm_endpoint_from_management will be destroyed
  - resource "aws_security_group_rule" "ssm_endpoint_from_management" {
      - cidr_blocks              = [] -> null
      - from_port                = 0 -> null
      - id                       = "sgrule-1308896626" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "-1" -> null
      - security_group_id        = "sg-0258424690602bd25" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-053efd7127835f9c3" -> null
      - to_port                  = 0 -> null
      - type                     = "ingress" -> null
    }

  # module.network.module.management.aws_vpc_endpoint.s3 will be destroyed
  - resource "aws_vpc_endpoint" "s3" {
      - cidr_blocks           = [
          - "52.218.128.0/17",
        ] -> null
      - dns_entry             = [] -> null
      - id                    = "vpce-0d077733dd16688af" -> null
      - network_interface_ids = [] -> null
      - owner_id              = "473124112471" -> null
      - policy                = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = "*"
                      - Effect    = "Allow"
                      - Principal = "*"
                      - Resource  = "*"
                    },
                ]
              - Version   = "2008-10-17"
            }
        ) -> null
      - prefix_list_id        = "pl-68a54001" -> null
      - private_dns_enabled   = false -> null
      - requester_managed     = false -> null
      - route_table_ids       = [
          - "rtb-00a32c905eba02447",
          - "rtb-00a5d8d6338b91e33",
          - "rtb-01399507207aed8cc",
          - "rtb-0273f9500b21931f6",
          - "rtb-095d5551201e2631e",
          - "rtb-09fc7ce039d02974d",
          - "rtb-0abb1bd018750a695",
          - "rtb-0b2f17a06718620be",
          - "rtb-42cc9e24",
          - "rtb-6b431c12",
          - "rtb-98421de1",
          - "rtb-b6431ccf",
        ] -> null
      - security_group_ids    = [] -> null
      - service_name          = "com.amazonaws.us-west-2.s3" -> null
      - state                 = "available" -> null
      - subnet_ids            = [] -> null
      - tags                  = {} -> null
      - vpc_endpoint_type     = "Gateway" -> null
      - vpc_id                = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.aws_vpc_endpoint.ssm will be destroyed
  - resource "aws_vpc_endpoint" "ssm" {
      - cidr_blocks           = [] -> null
      - dns_entry             = [
          - {
              - dns_name       = "vpce-0eebe69e470d4c103-rcckwkho.ssm.us-west-2.vpce.amazonaws.com"
              - hosted_zone_id = "Z1YSA3EXCYUU9Z"
            },
          - {
              - dns_name       = "vpce-0eebe69e470d4c103-rcckwkho-us-west-2c.ssm.us-west-2.vpce.amazonaws.com"
              - hosted_zone_id = "Z1YSA3EXCYUU9Z"
            },
          - {
              - dns_name       = "vpce-0eebe69e470d4c103-rcckwkho-us-west-2b.ssm.us-west-2.vpce.amazonaws.com"
              - hosted_zone_id = "Z1YSA3EXCYUU9Z"
            },
          - {
              - dns_name       = "vpce-0eebe69e470d4c103-rcckwkho-us-west-2a.ssm.us-west-2.vpce.amazonaws.com"
              - hosted_zone_id = "Z1YSA3EXCYUU9Z"
            },
          - {
              - dns_name       = "ssm.us-west-2.amazonaws.com"
              - hosted_zone_id = "Z2EJ2YPX0Z2JQH"
            },
        ] -> null
      - id                    = "vpce-0eebe69e470d4c103" -> null
      - network_interface_ids = [
          - "eni-0445cae8665638fb5",
          - "eni-08bdd1b026fc31e28",
          - "eni-0ed38954739e13756",
        ] -> null
      - owner_id              = "473124112471" -> null
      - policy                = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = "*"
                      - Effect    = "Allow"
                      - Principal = "*"
                      - Resource  = "*"
                    },
                ]
            }
        ) -> null
      - private_dns_enabled   = true -> null
      - requester_managed     = false -> null
      - route_table_ids       = [] -> null
      - security_group_ids    = [
          - "sg-0258424690602bd25",
        ] -> null
      - service_name          = "com.amazonaws.us-west-2.ssm" -> null
      - state                 = "available" -> null
      - subnet_ids            = [
          - "subnet-000c2e9bc0fa1f4ad",
          - "subnet-0485f887e73a69d40",
          - "subnet-0a019a1fb0d5aba75",
        ] -> null
      - tags                  = {} -> null
      - vpc_endpoint_type     = "Interface" -> null
      - vpc_id                = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.private_subnet.aws_route_table.private[0] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-98421de1" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-private.us-west-2a"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.private_subnet.aws_route_table.private[1] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-b6431ccf" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-private.us-west-2b"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.private_subnet.aws_route_table.private[2] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-6b431c12" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-private.us-west-2c"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.private_subnet.aws_route_table_association.private[0] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-7979aa02" -> null
      - route_table_id = "rtb-98421de1" -> null
      - subnet_id      = "subnet-400a3609" -> null
    }

  # module.network.module.private_subnet.aws_route_table_association.private[1] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-6375a618" -> null
      - route_table_id = "rtb-b6431ccf" -> null
      - subnet_id      = "subnet-46e7fd21" -> null
    }

  # module.network.module.private_subnet.aws_route_table_association.private[2] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-dd79aaa6" -> null
      - route_table_id = "rtb-6b431c12" -> null
      - subnet_id      = "subnet-2a3d8171" -> null
    }

  # module.network.module.private_subnet.aws_subnet.private[0] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-400a3609" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2a" -> null
      - availability_zone_id            = "usw2-az2" -> null
      - cidr_block                      = "10.149.64.0/24" -> null
      - id                              = "subnet-400a3609" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a540::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-ca8785b2" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-private.us-west-2a"
          - "Network" = "subnet-tier-2"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.private_subnet.aws_subnet.private[1] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-46e7fd21" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2b" -> null
      - availability_zone_id            = "usw2-az1" -> null
      - cidr_block                      = "10.149.65.0/24" -> null
      - id                              = "subnet-46e7fd21" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a541::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-30b45259" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-private.us-west-2b"
          - "Network" = "subnet-tier-2"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.private_subnet.aws_subnet.private[2] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-2a3d8171" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2c" -> null
      - availability_zone_id            = "usw2-az3" -> null
      - cidr_block                      = "10.149.66.0/24" -> null
      - id                              = "subnet-2a3d8171" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a542::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-986f4cd2" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-private.us-west-2c"
          - "Network" = "subnet-tier-2"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.public_subnet.aws_route_table.public[0] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-42cc9e24" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-public.us-west-2a"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.public_subnet.aws_route_table.public[1] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-01399507207aed8cc" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-public.us-west-2b"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.public_subnet.aws_route_table.public[2] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-09fc7ce039d02974d" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-public.us-west-2c"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.public_subnet.aws_route_table_association.public[0] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-c83703b1" -> null
      - route_table_id = "rtb-42cc9e24" -> null
      - subnet_id      = "subnet-dc043895" -> null
    }

  # module.network.module.public_subnet.aws_route_table_association.public[1] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-0b62e1e2c1b721ea4" -> null
      - route_table_id = "rtb-01399507207aed8cc" -> null
      - subnet_id      = "subnet-bfe7fdd8" -> null
    }

  # module.network.module.public_subnet.aws_route_table_association.public[2] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-00fd5347b4f3b3182" -> null
      - route_table_id = "rtb-09fc7ce039d02974d" -> null
      - subnet_id      = "subnet-113a864a" -> null
    }

  # module.network.module.public_subnet.aws_subnet.public[0] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-dc043895" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2a" -> null
      - availability_zone_id            = "usw2-az2" -> null
      - cidr_block                      = "10.149.32.0/24" -> null
      - id                              = "subnet-dc043895" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a520::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-c7888abf" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-public.us-west-2a"
          - "Network" = "subnet-tier-1"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.public_subnet.aws_subnet.public[1] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-bfe7fdd8" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2b" -> null
      - availability_zone_id            = "usw2-az1" -> null
      - cidr_block                      = "10.149.33.0/24" -> null
      - id                              = "subnet-bfe7fdd8" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a521::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-2fab4d46" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-public.us-west-2b"
          - "Network" = "subnet-tier-1"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.public_subnet.aws_subnet.public[2] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-113a864a" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2c" -> null
      - availability_zone_id            = "usw2-az3" -> null
      - cidr_block                      = "10.149.34.0/24" -> null
      - id                              = "subnet-113a864a" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a522::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-ee684ba4" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-public.us-west-2c"
          - "Network" = "subnet-tier-1"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.vpc.aws_egress_only_internet_gateway.this will be destroyed
  - resource "aws_egress_only_internet_gateway" "this" {
      - id     = "eigw-053a3838325edd831" -> null
      - vpc_id = "vpc-08d0186e" -> null
    }

  # module.network.module.vpc.aws_internet_gateway.this will be destroyed
  - resource "aws_internet_gateway" "this" {
      - id       = "igw-0dfd786a" -> null
      - owner_id = "473124112471" -> null
      - tags     = {
          - "Name" = "app-prod-northwest-vpc"
        } -> null
      - vpc_id   = "vpc-08d0186e" -> null
    }

  # module.network.module.vpc.aws_vpc.this will be destroyed
  - resource "aws_vpc" "this" {
      - arn                              = "arn:aws:ec2:us-west-2:473124112471:vpc/vpc-08d0186e" -> null
      - assign_generated_ipv6_cidr_block = true -> null
      - cidr_block                       = "10.149.0.0/16" -> null
      - default_network_acl_id           = "acl-4d74e72b" -> null
      - default_route_table_id           = "rtb-99ce9cff" -> null
      - default_security_group_id        = "sg-ef57fa95" -> null
      - dhcp_options_id                  = "dopt-0495df60" -> null
      - enable_classiclink               = false -> null
      - enable_classiclink_dns_support   = false -> null
      - enable_dns_hostnames             = true -> null
      - enable_dns_support               = true -> null
      - id                               = "vpc-08d0186e" -> null
      - instance_tenancy                 = "default" -> null
      - ipv6_association_id              = "vpc-cidr-assoc-61840609" -> null
      - ipv6_cidr_block                  = "2600:1f14:1b1:a500::/56" -> null
      - main_route_table_id              = "rtb-99ce9cff" -> null
      - owner_id                         = "473124112471" -> null
      - tags                             = {
          - "Name" = "app-prod-northwest-vpc"
        } -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table.private[0] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-00a5d8d6338b91e33" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-private.us-west-2a"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table.private[1] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-00a32c905eba02447" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-private.us-west-2b"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table.private[2] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-0b2f17a06718620be" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-private.us-west-2c"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table_association.private[0] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-05ea90604a19a06e3" -> null
      - route_table_id = "rtb-00a5d8d6338b91e33" -> null
      - subnet_id      = "subnet-000c2e9bc0fa1f4ad" -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table_association.private[1] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-0cb817938a8ba2087" -> null
      - route_table_id = "rtb-00a32c905eba02447" -> null
      - subnet_id      = "subnet-0a019a1fb0d5aba75" -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table_association.private[2] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-0cfdc3b0d395859a4" -> null
      - route_table_id = "rtb-0b2f17a06718620be" -> null
      - subnet_id      = "subnet-0485f887e73a69d40" -> null
    }

  # module.network.module.management.module.private_subnet.aws_subnet.private[0] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-000c2e9bc0fa1f4ad" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2a" -> null
      - availability_zone_id            = "usw2-az2" -> null
      - cidr_block                      = "10.149.128.0/24" -> null
      - id                              = "subnet-000c2e9bc0fa1f4ad" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a580::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-0b5676ecaf90cb306" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-private.us-west-2a"
          - "Network" = "subnet-tier-4"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.module.private_subnet.aws_subnet.private[1] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-0a019a1fb0d5aba75" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2b" -> null
      - availability_zone_id            = "usw2-az1" -> null
      - cidr_block                      = "10.149.129.0/24" -> null
      - id                              = "subnet-0a019a1fb0d5aba75" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a581::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-07dd42d7cea11c85b" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-private.us-west-2b"
          - "Network" = "subnet-tier-4"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.module.private_subnet.aws_subnet.private[2] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-0485f887e73a69d40" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2c" -> null
      - availability_zone_id            = "usw2-az3" -> null
      - cidr_block                      = "10.149.130.0/24" -> null
      - id                              = "subnet-0485f887e73a69d40" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a582::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-08d085c48b70fb171" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-private.us-west-2c"
          - "Network" = "subnet-tier-4"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.module.public_subnet.aws_route_table.public[0] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-0abb1bd018750a695" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-public.us-west-2a"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.public_subnet.aws_route_table.public[1] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-0273f9500b21931f6" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-public.us-west-2b"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.public_subnet.aws_route_table.public[2] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-095d5551201e2631e" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-public.us-west-2c"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.public_subnet.aws_route_table_association.public[0] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-0705bb27327ea3421" -> null
      - route_table_id = "rtb-0abb1bd018750a695" -> null
      - subnet_id      = "subnet-03016b54639ef2fbb" -> null
    }

  # module.network.module.management.module.public_subnet.aws_route_table_association.public[1] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-0c7351142f221c655" -> null
      - route_table_id = "rtb-0273f9500b21931f6" -> null
      - subnet_id      = "subnet-011c372fcaeea68f4" -> null
    }

  # module.network.module.management.module.public_subnet.aws_route_table_association.public[2] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-0c70dce4713041447" -> null
      - route_table_id = "rtb-095d5551201e2631e" -> null
      - subnet_id      = "subnet-05b3590a52783b057" -> null
    }

  # module.network.module.management.module.public_subnet.aws_subnet.public[0] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-03016b54639ef2fbb" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2a" -> null
      - availability_zone_id            = "usw2-az2" -> null
      - cidr_block                      = "10.149.96.0/24" -> null
      - id                              = "subnet-03016b54639ef2fbb" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a560::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-0b4cb7b58039f09bc" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-public.us-west-2a"
          - "Network" = "subnet-tier-3"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.module.public_subnet.aws_subnet.public[1] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-011c372fcaeea68f4" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2b" -> null
      - availability_zone_id            = "usw2-az1" -> null
      - cidr_block                      = "10.149.97.0/24" -> null
      - id                              = "subnet-011c372fcaeea68f4" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a561::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-068f13da6ec566218" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-public.us-west-2b"
          - "Network" = "subnet-tier-3"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.module.public_subnet.aws_subnet.public[2] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-05b3590a52783b057" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2c" -> null
      - availability_zone_id            = "usw2-az3" -> null
      - cidr_block                      = "10.149.98.0/24" -> null
      - id                              = "subnet-05b3590a52783b057" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a562::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-03c2f5d2ca4330925" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-public.us-west-2c"
          - "Network" = "subnet-tier-3"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

Plan: 0 to add, 0 to change, 87 to destroy.

------------------------------------------------------------------------

Note: You didn't specify an "-out" parameter to save this plan, so Terraform
can't guarantee that exactly these actions will be performed if
"terraform apply" is subsequently run.

Releasing state lock. This may take a few moments...
```

### Destroy

```console
$ /usr/local/opt/terraform@0.12/bin/terraform destroy
module.secrets.aws_ssm_parameter.secret_key: Refreshing state... [id=/app/production/SECRET_KEY]
module.secrets.aws_ssm_parameter.database_password: Refreshing state... [id=/app/production/DB_PASSWORD]
module.base.data.aws_iam_policy_document.assume: Refreshing state...
module.network.module.vpc.aws_vpc.this: Refreshing state... [id=vpc-08d0186e]
module.mysql.aws_db_parameter_group.main_rds_instance: Refreshing state... [id=app-mysql-custom-params-0058e036eab3f18e3d97fe5a79]
module.base.data.aws_route53_zone.hyperbolausercontent: Refreshing state...
module.network.module.management.data.aws_vpc_endpoint_service.s3: Refreshing state...
data.aws_route53_zone.hyperbola: Refreshing state...
module.backend.data.aws_acm_certificate.alb-cert: Refreshing state...
module.backend.data.aws_ami.backend: Refreshing state...
module.network.module.management.data.aws_vpc_endpoint_service.ssm: Refreshing state...
module.base.aws_iam_role.app: Refreshing state... [id=app-role-00f8d1802132e948040476a3b0]
module.base.data.aws_acm_certificate.cdn: Refreshing state...
module.base.aws_iam_role_policy.app: Refreshing state... [id=app-role-00f8d1802132e948040476a3b0:app-policy-00f8d1802132e948040476a3b2]
module.base.aws_iam_instance_profile.app: Refreshing state... [id=app-profile-00f8d1802132e948040476a3b1]
module.network.module.vpc.aws_egress_only_internet_gateway.this: Refreshing state... [id=eigw-053a3838325edd831]
module.network.module.vpc.aws_internet_gateway.this: Refreshing state... [id=igw-0dfd786a]
module.network.module.private_subnet.data.aws_vpc.this: Refreshing state...
module.network.aws_network_acl.acl: Refreshing state... [id=acl-4e77e428]
module.network.module.management.aws_security_group.ssm: Refreshing state... [id=sg-0258424690602bd25]
module.network.module.public_subnet.data.aws_vpc.this: Refreshing state...
module.network.module.nat.data.aws_vpc.selected: Refreshing state...
module.network.module.management.module.private_subnet.data.aws_vpc.this: Refreshing state...
aws_route53_zone.app_dc: Refreshing state... [id=Z1O2JQV3R0LG26]
module.backend.data.aws_vpc.this: Refreshing state...
module.backend.aws_security_group.backend: Refreshing state... [id=sg-5ffd4125]
module.network.module.management.module.public_subnet.data.aws_vpc.this: Refreshing state...
module.mysql.data.aws_vpc.current: Refreshing state...
module.base.aws_cloudfront_distribution.cdn: Refreshing state... [id=E2KESP33B8DNIU]
module.network.module.management.aws_security_group.this: Refreshing state... [id=sg-053efd7127835f9c3]
module.backend.aws_launch_template.backend: Refreshing state... [id=lt-0d1bd9f990ac86bda]
module.network.module.public_subnet.aws_subnet.public[1]: Refreshing state... [id=subnet-bfe7fdd8]
module.network.module.public_subnet.aws_subnet.public[0]: Refreshing state... [id=subnet-dc043895]
module.network.module.public_subnet.aws_subnet.public[2]: Refreshing state... [id=subnet-113a864a]
module.network.module.public_subnet.aws_route_table.public[2]: Refreshing state... [id=rtb-09fc7ce039d02974d]
module.network.module.public_subnet.aws_route_table.public[1]: Refreshing state... [id=rtb-01399507207aed8cc]
module.network.module.public_subnet.aws_route_table.public[0]: Refreshing state... [id=rtb-42cc9e24]
module.network.module.management.module.private_subnet.aws_route_table.private[0]: Refreshing state... [id=rtb-00a5d8d6338b91e33]
module.network.module.management.module.private_subnet.aws_route_table.private[2]: Refreshing state... [id=rtb-0b2f17a06718620be]
module.network.module.management.module.private_subnet.aws_route_table.private[1]: Refreshing state... [id=rtb-00a32c905eba02447]
module.network.module.management.module.private_subnet.aws_subnet.private[2]: Refreshing state... [id=subnet-0485f887e73a69d40]
module.network.module.management.module.private_subnet.aws_subnet.private[1]: Refreshing state... [id=subnet-0a019a1fb0d5aba75]
module.network.module.management.module.private_subnet.aws_subnet.private[0]: Refreshing state... [id=subnet-000c2e9bc0fa1f4ad]
module.network.module.private_subnet.aws_subnet.private[1]: Refreshing state... [id=subnet-46e7fd21]
module.network.module.private_subnet.aws_subnet.private[2]: Refreshing state... [id=subnet-2a3d8171]
module.network.module.private_subnet.aws_subnet.private[0]: Refreshing state... [id=subnet-400a3609]
module.network.module.private_subnet.aws_route_table.private[0]: Refreshing state... [id=rtb-98421de1]
module.network.module.private_subnet.aws_route_table.private[1]: Refreshing state... [id=rtb-b6431ccf]
module.network.module.private_subnet.aws_route_table.private[2]: Refreshing state... [id=rtb-6b431c12]
module.network.module.management.aws_security_group_rule.ssm_endpoint_from_management: Refreshing state... [id=sgrule-1308896626]
module.backend.aws_security_group_rule.backend_to_ssm_endpoint: Refreshing state... [id=sgrule-2455676943]
module.backend.aws_security_group_rule.ssm_endpoint_from_backend: Refreshing state... [id=sgrule-1886272967]
module.backend.aws_alb_target_group.backend: Refreshing state... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02]
module.backend.aws_security_group.alb: Refreshing state... [id=sg-d88caea5]
module.network.module.management.module.public_subnet.aws_subnet.public[2]: Refreshing state... [id=subnet-05b3590a52783b057]
module.network.module.management.module.public_subnet.aws_subnet.public[1]: Refreshing state... [id=subnet-011c372fcaeea68f4]
module.network.module.management.module.public_subnet.aws_subnet.public[0]: Refreshing state... [id=subnet-03016b54639ef2fbb]
module.network.module.management.module.public_subnet.aws_route_table.public[0]: Refreshing state... [id=rtb-0abb1bd018750a695]
module.network.module.management.module.public_subnet.aws_route_table.public[1]: Refreshing state... [id=rtb-0273f9500b21931f6]
module.network.module.management.module.public_subnet.aws_route_table.public[2]: Refreshing state... [id=rtb-095d5551201e2631e]
module.mysql.aws_security_group.main_db_access: Refreshing state... [id=sg-a2381cdf]
module.network.module.public_subnet.aws_route_table_association.public[0]: Refreshing state... [id=rtbassoc-c83703b1]
module.network.module.public_subnet.aws_route_table_association.public[1]: Refreshing state... [id=rtbassoc-0b62e1e2c1b721ea4]
module.network.module.public_subnet.aws_route_table_association.public[2]: Refreshing state... [id=rtbassoc-00fd5347b4f3b3182]
module.network.module.management.module.private_subnet.aws_route_table_association.private[2]: Refreshing state... [id=rtbassoc-0cfdc3b0d395859a4]
module.network.module.management.module.private_subnet.aws_route_table_association.private[0]: Refreshing state... [id=rtbassoc-05ea90604a19a06e3]
module.network.module.management.module.private_subnet.aws_route_table_association.private[1]: Refreshing state... [id=rtbassoc-0cb817938a8ba2087]
module.backend.aws_security_group_rule.backend-from-alb-http: Refreshing state... [id=sgrule-3372377313]
module.backend.aws_security_group_rule.backend-from-alb-health-check: Refreshing state... [id=sgrule-2556693372]
module.mysql.module.subnets.data.aws_vpc.this: Refreshing state...
module.base.aws_route53_record.cdn-A: Refreshing state... [id=Z25GE9A9NRUR2N_www_A]
module.base.aws_route53_record.cdn-AAAA: Refreshing state... [id=Z25GE9A9NRUR2N_www_AAAA]
module.network.module.management.aws_vpc_endpoint.ssm: Refreshing state... [id=vpce-0eebe69e470d4c103]
module.network.module.management.module.public_subnet.aws_route_table_association.public[0]: Refreshing state... [id=rtbassoc-0705bb27327ea3421]
module.network.module.management.module.public_subnet.aws_route_table_association.public[2]: Refreshing state... [id=rtbassoc-0c70dce4713041447]
module.network.module.management.module.public_subnet.aws_route_table_association.public[1]: Refreshing state... [id=rtbassoc-0c7351142f221c655]
module.network.module.nat.data.aws_subnet_ids.public: Refreshing state...
module.backend.data.aws_subnet_ids.public: Refreshing state...
module.network.module.management.aws_vpc_endpoint.s3: Refreshing state... [id=vpce-0d077733dd16688af]
module.backend.aws_security_group_rule.backend-to-mysql: Refreshing state... [id=sgrule-3211482754]
module.backend.aws_security_group_rule.mysql-from-backend: Refreshing state... [id=sgrule-3393583181]
module.network.module.private_subnet.aws_route_table_association.private[2]: Refreshing state... [id=rtbassoc-dd79aaa6]
module.network.module.private_subnet.aws_route_table_association.private[0]: Refreshing state... [id=rtbassoc-7979aa02]
module.network.module.private_subnet.aws_route_table_association.private[1]: Refreshing state... [id=rtbassoc-6375a618]
module.backend.data.aws_subnet.public[1]: Refreshing state...
module.backend.data.aws_subnet.public[2]: Refreshing state...
module.backend.data.aws_subnet.public[0]: Refreshing state...
module.backend.data.aws_subnet_ids.private: Refreshing state...
module.backend.aws_security_group_rule.backend-to-s3-endpoint: Refreshing state... [id=sgrule-1220853808]
module.mysql.module.subnets.aws_route_table.private[0]: Refreshing state... [id=rtb-fa702f83]
module.mysql.module.subnets.aws_route_table.private[2]: Refreshing state... [id=rtb-5a702f23]
module.mysql.module.subnets.aws_route_table.private[1]: Refreshing state... [id=rtb-82722dfb]
module.mysql.module.subnets.aws_subnet.private[2]: Refreshing state... [id=subnet-60d0ec3b]
module.mysql.module.subnets.aws_subnet.private[0]: Refreshing state... [id=subnet-d5f06d9d]
module.mysql.module.subnets.aws_subnet.private[1]: Refreshing state... [id=subnet-70a0dd16]
module.backend.data.aws_subnet.private[2]: Refreshing state...
module.backend.data.aws_subnet.private[1]: Refreshing state...
module.backend.data.aws_subnet.private[0]: Refreshing state...
module.backend.aws_alb.alb: Refreshing state... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:loadbalancer/app/applb-20171106080744451200000003/45bf0d921a80598a]
module.mysql.module.subnets.aws_route_table_association.private[1]: Refreshing state... [id=rtbassoc-486ebd33]
module.mysql.module.subnets.aws_route_table_association.private[2]: Refreshing state... [id=rtbassoc-c36dbeb8]
module.mysql.module.subnets.aws_route_table_association.private[0]: Refreshing state... [id=rtbassoc-636cbf18]
module.mysql.aws_db_subnet_group.main_db_subnet_group: Refreshing state... [id=app-mysql-subnet-group-0058e036eab3f18e3d97fe5a7a]
module.backend.aws_autoscaling_group.backend: Refreshing state... [id=app-backend-asg-20181105004601904200000003]
module.mysql.aws_db_instance.main_rds_instance: Refreshing state... [id=app-mysql-0058e036eab3f18e3d97fe5a7b]
module.backend.aws_autoscaling_policy.backend-scaledown: Refreshing state... [id=app-prod-northwest-backend-scaledown-policy]
module.backend.aws_autoscaling_policy.backend-scaleup: Refreshing state... [id=app-prod-northwest-backend-scaleup-policy]
module.backend.aws_alb_listener.alb-http: Refreshing state... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/a2bb653297384a8e]
module.backend.aws_alb_listener.alb-https: Refreshing state... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/f98b62f677df1e1c]
module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaledown: Refreshing state... [id=app-prod-northwest-backend-scaledown-cpu-alarm]
module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaleup: Refreshing state... [id=app-prod-northwest-backend-scaleup-cpu-alarm]
aws_route53_record.mysql: Refreshing state... [id=Z1O2JQV3R0LG26_mysql_CNAME]

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_route53_record.mysql will be destroyed
  - resource "aws_route53_record" "mysql" {
      - allow_overwrite = true -> null
      - fqdn            = "mysql.app.hyperboladc.net" -> null
      - id              = "Z1O2JQV3R0LG26_mysql_CNAME" -> null
      - name            = "mysql" -> null
      - records         = [
          - "app-mysql-0058e036eab3f18e3d97fe5a7b.cpebqrq01cnd.us-west-2.rds.amazonaws.com",
        ] -> null
      - ttl             = 300 -> null
      - type            = "CNAME" -> null
      - zone_id         = "Z1O2JQV3R0LG26" -> null
    }

  # aws_route53_zone.app_dc will be destroyed
  - resource "aws_route53_zone" "app_dc" {
      - comment       = "Managed by Terraform" -> null
      - force_destroy = false -> null
      - id            = "Z1O2JQV3R0LG26" -> null
      - name          = "app.hyperboladc.net." -> null
      - name_servers  = [
          - "ns-0.awsdns-00.com.",
          - "ns-1024.awsdns-00.org.",
          - "ns-1536.awsdns-00.co.uk.",
          - "ns-512.awsdns-00.net.",
        ] -> null
      - tags          = {} -> null
      - vpc_id        = "vpc-08d0186e" -> null
      - vpc_region    = "us-west-2" -> null
      - zone_id       = "Z1O2JQV3R0LG26" -> null

      - vpc {
          - vpc_id     = "vpc-08d0186e" -> null
          - vpc_region = "us-west-2" -> null
        }
    }

  # module.backend.aws_alb.alb will be destroyed
  - resource "aws_alb" "alb" {
      - arn                        = "arn:aws:elasticloadbalancing:us-west-2:473124112471:loadbalancer/app/applb-20171106080744451200000003/45bf0d921a80598a" -> null
      - arn_suffix                 = "app/applb-20171106080744451200000003/45bf0d921a80598a" -> null
      - dns_name                   = "applb-20171106080744451200000003-922647741.us-west-2.elb.amazonaws.com" -> null
      - enable_deletion_protection = false -> null
      - enable_http2               = true -> null
      - id                         = "arn:aws:elasticloadbalancing:us-west-2:473124112471:loadbalancer/app/applb-20171106080744451200000003/45bf0d921a80598a" -> null
      - idle_timeout               = 60 -> null
      - internal                   = false -> null
      - ip_address_type            = "dualstack" -> null
      - load_balancer_type         = "application" -> null
      - name                       = "applb-20171106080744451200000003" -> null
      - name_prefix                = "applb-" -> null
      - security_groups            = [
          - "sg-d88caea5",
        ] -> null
      - subnets                    = [
          - "subnet-113a864a",
          - "subnet-bfe7fdd8",
          - "subnet-dc043895",
        ] -> null
      - tags                       = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-alb"
        } -> null
      - vpc_id                     = "vpc-08d0186e" -> null
      - zone_id                    = "Z1H1FL5HABSF5" -> null

      - access_logs {
          - enabled = false -> null
        }

      - subnet_mapping {
          - subnet_id = "subnet-113a864a" -> null
        }
      - subnet_mapping {
          - subnet_id = "subnet-bfe7fdd8" -> null
        }
      - subnet_mapping {
          - subnet_id = "subnet-dc043895" -> null
        }

      - timeouts {}
    }

  # module.backend.aws_alb_listener.alb-http will be destroyed
  - resource "aws_alb_listener" "alb-http" {
      - arn               = "arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/a2bb653297384a8e" -> null
      - id                = "arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/a2bb653297384a8e" -> null
      - load_balancer_arn = "arn:aws:elasticloadbalancing:us-west-2:473124112471:loadbalancer/app/applb-20171106080744451200000003/45bf0d921a80598a" -> null
      - port              = 80 -> null
      - protocol          = "HTTP" -> null

      - default_action {
          - order            = 0 -> null
          - target_group_arn = "arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02" -> null
          - type             = "forward" -> null
        }

      - timeouts {}
    }

  # module.backend.aws_alb_listener.alb-https will be destroyed
  - resource "aws_alb_listener" "alb-https" {
      - arn               = "arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/f98b62f677df1e1c" -> null
      - certificate_arn   = "arn:aws:acm:us-west-2:473124112471:certificate/ebb1e8c3-393d-4941-8410-af814e775159" -> null
      - id                = "arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/f98b62f677df1e1c" -> null
      - load_balancer_arn = "arn:aws:elasticloadbalancing:us-west-2:473124112471:loadbalancer/app/applb-20171106080744451200000003/45bf0d921a80598a" -> null
      - port              = 443 -> null
      - protocol          = "HTTPS" -> null
      - ssl_policy        = "ELBSecurityPolicy-TLS-1-2-2017-01" -> null

      - default_action {
          - order            = 0 -> null
          - target_group_arn = "arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02" -> null
          - type             = "forward" -> null
        }

      - timeouts {}
    }

  # module.backend.aws_alb_target_group.backend will be destroyed
  - resource "aws_alb_target_group" "backend" {
      - arn                                = "arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02" -> null
      - arn_suffix                         = "targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02" -> null
      - deregistration_delay               = 30 -> null
      - id                                 = "arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02" -> null
      - lambda_multi_value_headers_enabled = false -> null
      - load_balancing_algorithm_type      = "round_robin" -> null
      - name                               = "apptg-20171106080741745400000001" -> null
      - name_prefix                        = "apptg-" -> null
      - port                               = 80 -> null
      - protocol                           = "HTTP" -> null
      - proxy_protocol_v2                  = false -> null
      - slow_start                         = 0 -> null
      - tags                               = {} -> null
      - target_type                        = "instance" -> null
      - vpc_id                             = "vpc-08d0186e" -> null

      - health_check {
          - enabled             = true -> null
          - healthy_threshold   = 3 -> null
          - interval            = 30 -> null
          - matcher             = "200" -> null
          - path                = "/healthz" -> null
          - port                = "8888" -> null
          - protocol            = "HTTP" -> null
          - timeout             = 5 -> null
          - unhealthy_threshold = 3 -> null
        }

      - stickiness {
          - cookie_duration = 86400 -> null
          - enabled         = false -> null
          - type            = "lb_cookie" -> null
        }
    }

  # module.backend.aws_autoscaling_group.backend will be destroyed
  - resource "aws_autoscaling_group" "backend" {
      - arn                       = "arn:aws:autoscaling:us-west-2:473124112471:autoScalingGroup:7a95b0ae-fde3-4dc9-9594-a519f126b037:autoScalingGroupName/app-backend-asg-20181105004601904200000003" -> null
      - availability_zones        = [
          - "us-west-2a",
          - "us-west-2b",
          - "us-west-2c",
        ] -> null
      - default_cooldown          = 300 -> null
      - desired_capacity          = 1 -> null
      - enabled_metrics           = [] -> null
      - force_delete              = false -> null
      - health_check_grace_period = 300 -> null
      - health_check_type         = "EC2" -> null
      - id                        = "app-backend-asg-20181105004601904200000003" -> null
      - load_balancers            = [] -> null
      - max_instance_lifetime     = 0 -> null
      - max_size                  = 3 -> null
      - metrics_granularity       = "1Minute" -> null
      - min_size                  = 1 -> null
      - name                      = "app-backend-asg-20181105004601904200000003" -> null
      - name_prefix               = "app-backend-asg-" -> null
      - protect_from_scale_in     = false -> null
      - service_linked_role_arn   = "arn:aws:iam::473124112471:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling" -> null
      - suspended_processes       = [] -> null
      - target_group_arns         = [
          - "arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02",
        ] -> null
      - termination_policies      = [] -> null
      - vpc_zone_identifier       = [
          - "subnet-2a3d8171",
          - "subnet-400a3609",
          - "subnet-46e7fd21",
        ] -> null
      - wait_for_capacity_timeout = "10m" -> null
      - wait_for_elb_capacity     = 1 -> null

      - launch_template {
          - id      = "lt-0d1bd9f990ac86bda" -> null
          - name    = "app-backend-lc-20181105004601132100000001" -> null
          - version = "$Latest" -> null
        }

      - timeouts {}
    }

  # module.backend.aws_autoscaling_policy.backend-scaledown will be destroyed
  - resource "aws_autoscaling_policy" "backend-scaledown" {
      - adjustment_type           = "ChangeInCapacity" -> null
      - arn                       = "arn:aws:autoscaling:us-west-2:473124112471:scalingPolicy:7773b3cc-4a4e-4ca8-a5c6-e9c6e45907f5:autoScalingGroupName/app-backend-asg-20181105004601904200000003:policyName/app-prod-northwest-backend-scaledown-policy" -> null
      - autoscaling_group_name    = "app-backend-asg-20181105004601904200000003" -> null
      - cooldown                  = 300 -> null
      - estimated_instance_warmup = 0 -> null
      - id                        = "app-prod-northwest-backend-scaledown-policy" -> null
      - min_adjustment_step       = 0 -> null
      - name                      = "app-prod-northwest-backend-scaledown-policy" -> null
      - policy_type               = "SimpleScaling" -> null
      - scaling_adjustment        = -1 -> null
    }

  # module.backend.aws_autoscaling_policy.backend-scaleup will be destroyed
  - resource "aws_autoscaling_policy" "backend-scaleup" {
      - adjustment_type           = "ChangeInCapacity" -> null
      - arn                       = "arn:aws:autoscaling:us-west-2:473124112471:scalingPolicy:a7fa9503-7f91-4987-b5e2-a691f94f8115:autoScalingGroupName/app-backend-asg-20181105004601904200000003:policyName/app-prod-northwest-backend-scaleup-policy" -> null
      - autoscaling_group_name    = "app-backend-asg-20181105004601904200000003" -> null
      - cooldown                  = 300 -> null
      - estimated_instance_warmup = 0 -> null
      - id                        = "app-prod-northwest-backend-scaleup-policy" -> null
      - min_adjustment_step       = 0 -> null
      - name                      = "app-prod-northwest-backend-scaleup-policy" -> null
      - policy_type               = "SimpleScaling" -> null
      - scaling_adjustment        = 1 -> null
    }

  # module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaledown will be destroyed
  - resource "aws_cloudwatch_metric_alarm" "backend-cpu-scaledown" {
      - actions_enabled           = true -> null
      - alarm_actions             = [
          - "arn:aws:autoscaling:us-west-2:473124112471:scalingPolicy:7773b3cc-4a4e-4ca8-a5c6-e9c6e45907f5:autoScalingGroupName/app-backend-asg-20181105004601904200000003:policyName/app-prod-northwest-backend-scaledown-policy",
        ] -> null
      - alarm_name                = "app-prod-northwest-backend-scaledown-cpu-alarm" -> null
      - arn                       = "arn:aws:cloudwatch:us-west-2:473124112471:alarm:app-prod-northwest-backend-scaledown-cpu-alarm" -> null
      - comparison_operator       = "LessThanOrEqualToThreshold" -> null
      - datapoints_to_alarm       = 0 -> null
      - dimensions                = {
          - "AutoScalingGroupName" = "app-backend-asg-20181105004601904200000003"
        } -> null
      - evaluation_periods        = 2 -> null
      - id                        = "app-prod-northwest-backend-scaledown-cpu-alarm" -> null
      - insufficient_data_actions = [] -> null
      - metric_name               = "CPUUtilization" -> null
      - namespace                 = "AWS/EC2" -> null
      - ok_actions                = [] -> null
      - period                    = 120 -> null
      - statistic                 = "Average" -> null
      - tags                      = {} -> null
      - threshold                 = 20 -> null
      - treat_missing_data        = "missing" -> null
    }

  # module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaleup will be destroyed
  - resource "aws_cloudwatch_metric_alarm" "backend-cpu-scaleup" {
      - actions_enabled           = true -> null
      - alarm_actions             = [
          - "arn:aws:autoscaling:us-west-2:473124112471:scalingPolicy:a7fa9503-7f91-4987-b5e2-a691f94f8115:autoScalingGroupName/app-backend-asg-20181105004601904200000003:policyName/app-prod-northwest-backend-scaleup-policy",
        ] -> null
      - alarm_name                = "app-prod-northwest-backend-scaleup-cpu-alarm" -> null
      - arn                       = "arn:aws:cloudwatch:us-west-2:473124112471:alarm:app-prod-northwest-backend-scaleup-cpu-alarm" -> null
      - comparison_operator       = "GreaterThanOrEqualToThreshold" -> null
      - datapoints_to_alarm       = 0 -> null
      - dimensions                = {
          - "AutoScalingGroupName" = "app-backend-asg-20181105004601904200000003"
        } -> null
      - evaluation_periods        = 2 -> null
      - id                        = "app-prod-northwest-backend-scaleup-cpu-alarm" -> null
      - insufficient_data_actions = [] -> null
      - metric_name               = "CPUUtilization" -> null
      - namespace                 = "AWS/EC2" -> null
      - ok_actions                = [] -> null
      - period                    = 120 -> null
      - statistic                 = "Average" -> null
      - tags                      = {} -> null
      - threshold                 = 60 -> null
      - treat_missing_data        = "missing" -> null
    }

  # module.backend.aws_launch_template.backend will be destroyed
  - resource "aws_launch_template" "backend" {
      - arn                     = "arn:aws:ec2:us-west-2:473124112471:launch-template/lt-0d1bd9f990ac86bda" -> null
      - default_version         = 1 -> null
      - disable_api_termination = false -> null
      - ebs_optimized           = "true" -> null
      - id                      = "lt-0d1bd9f990ac86bda" -> null
      - image_id                = "ami-0f554629c8c210b85" -> null
      - instance_type           = "t3.nano" -> null
      - latest_version          = 20 -> null
      - name                    = "app-backend-lc-20181105004601132100000001" -> null
      - name_prefix             = "app-backend-lc-" -> null
      - security_group_names    = [] -> null
      - tags                    = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-backend"
        } -> null
      - vpc_security_group_ids  = [
          - "sg-5ffd4125",
        ] -> null

      - iam_instance_profile {
          - name = "app-profile-00f8d1802132e948040476a3b1" -> null
        }

      - instance_market_options {
          - market_type = "spot" -> null

          - spot_options {
              - block_duration_minutes = 0 -> null
              - max_price              = "0.0052" -> null
            }
        }

      - monitoring {
          - enabled = false -> null
        }

      - tag_specifications {
          - resource_type = "instance" -> null
          - tags          = {
              - "Environment" = "production"
              - "Name"        = "app-prod-northwest-backend"
              - "Version"     = "0.159.0"
            } -> null
        }
    }

  # module.backend.aws_security_group.alb will be destroyed
  - resource "aws_security_group" "alb" {
      - arn                    = "arn:aws:ec2:us-west-2:473124112471:security-group/sg-d88caea5" -> null
      - description            = "Managed by Terraform" -> null
      - egress                 = [
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-5ffd4125",
                ]
              - self             = false
              - to_port          = 80
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 8888
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-5ffd4125",
                ]
              - self             = false
              - to_port          = 8888
            },
        ] -> null
      - id                     = "sg-d88caea5" -> null
      - ingress                = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 443
              - ipv6_cidr_blocks = [
                  - "::/0",
                ]
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 443
            },
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = [
                  - "::/0",
                ]
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 80
            },
        ] -> null
      - name                   = "app-alb-sg-20171106080741747400000002" -> null
      - name_prefix            = "app-alb-sg-" -> null
      - owner_id               = "473124112471" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-alb-sg"
        } -> null
      - vpc_id                 = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.backend.aws_security_group.backend will be destroyed
  - resource "aws_security_group" "backend" {
      - arn                    = "arn:aws:ec2:us-west-2:473124112471:security-group/sg-5ffd4125" -> null
      - description            = "Managed by Terraform" -> null
      - egress                 = [
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = [
                  - "pl-68a54001",
                ]
              - protocol         = "-1"
              - security_groups  = []
              - self             = false
              - to_port          = 0
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "-1"
              - security_groups  = [
                  - "sg-0258424690602bd25",
                ]
              - self             = false
              - to_port          = 0
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 3306
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-a2381cdf",
                ]
              - self             = false
              - to_port          = 3306
            },
        ] -> null
      - id                     = "sg-5ffd4125" -> null
      - ingress                = [
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-d88caea5",
                ]
              - self             = false
              - to_port          = 80
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 8888
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-d88caea5",
                ]
              - self             = false
              - to_port          = 8888
            },
        ] -> null
      - name                   = "app-backend-sg-00ba465879944ffeffaef34926" -> null
      - name_prefix            = "app-backend-sg-" -> null
      - owner_id               = "473124112471" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-backend-sg"
        } -> null
      - vpc_id                 = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.backend.aws_security_group_rule.backend-from-alb-health-check will be destroyed
  - resource "aws_security_group_rule" "backend-from-alb-health-check" {
      - cidr_blocks              = [] -> null
      - from_port                = 8888 -> null
      - id                       = "sgrule-2556693372" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-5ffd4125" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-d88caea5" -> null
      - to_port                  = 8888 -> null
      - type                     = "ingress" -> null
    }

  # module.backend.aws_security_group_rule.backend-from-alb-http will be destroyed
  - resource "aws_security_group_rule" "backend-from-alb-http" {
      - cidr_blocks              = [] -> null
      - from_port                = 80 -> null
      - id                       = "sgrule-3372377313" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-5ffd4125" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-d88caea5" -> null
      - to_port                  = 80 -> null
      - type                     = "ingress" -> null
    }

  # module.backend.aws_security_group_rule.backend-to-mysql will be destroyed
  - resource "aws_security_group_rule" "backend-to-mysql" {
      - cidr_blocks              = [] -> null
      - from_port                = 3306 -> null
      - id                       = "sgrule-3211482754" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-5ffd4125" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-a2381cdf" -> null
      - to_port                  = 3306 -> null
      - type                     = "egress" -> null
    }

  # module.backend.aws_security_group_rule.backend-to-s3-endpoint will be destroyed
  - resource "aws_security_group_rule" "backend-to-s3-endpoint" {
      - cidr_blocks       = [] -> null
      - from_port         = 0 -> null
      - id                = "sgrule-1220853808" -> null
      - ipv6_cidr_blocks  = [] -> null
      - prefix_list_ids   = [
          - "pl-68a54001",
        ] -> null
      - protocol          = "-1" -> null
      - security_group_id = "sg-5ffd4125" -> null
      - self              = false -> null
      - to_port           = 0 -> null
      - type              = "egress" -> null
    }

  # module.backend.aws_security_group_rule.backend_to_ssm_endpoint will be destroyed
  - resource "aws_security_group_rule" "backend_to_ssm_endpoint" {
      - cidr_blocks              = [] -> null
      - from_port                = 0 -> null
      - id                       = "sgrule-2455676943" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "-1" -> null
      - security_group_id        = "sg-5ffd4125" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-0258424690602bd25" -> null
      - to_port                  = 0 -> null
      - type                     = "egress" -> null
    }

  # module.backend.aws_security_group_rule.mysql-from-backend will be destroyed
  - resource "aws_security_group_rule" "mysql-from-backend" {
      - cidr_blocks              = [] -> null
      - from_port                = 3306 -> null
      - id                       = "sgrule-3393583181" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-a2381cdf" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-5ffd4125" -> null
      - to_port                  = 3306 -> null
      - type                     = "ingress" -> null
    }

  # module.backend.aws_security_group_rule.ssm_endpoint_from_backend will be destroyed
  - resource "aws_security_group_rule" "ssm_endpoint_from_backend" {
      - cidr_blocks              = [] -> null
      - from_port                = 0 -> null
      - id                       = "sgrule-1886272967" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "-1" -> null
      - security_group_id        = "sg-0258424690602bd25" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-5ffd4125" -> null
      - to_port                  = 0 -> null
      - type                     = "ingress" -> null
    }

  # module.base.aws_cloudfront_distribution.cdn will be destroyed
  - resource "aws_cloudfront_distribution" "cdn" {
      - active_trusted_signers         = {
          - "enabled" = "false"
          - "items.#" = "0"
        } -> null
      - aliases                        = [
          - "www.hyperbolausercontent.net",
        ] -> null
      - arn                            = "arn:aws:cloudfront::473124112471:distribution/E2KESP33B8DNIU" -> null
      - caller_reference               = "2017-07-16T15:38:26.626264616-07:00" -> null
      - comment                        = "CloudFront for hyperbola-app cdn - production" -> null
      - domain_name                    = "drk9p6kxy4a37.cloudfront.net" -> null
      - enabled                        = true -> null
      - etag                           = "EY4S4YCN3OKS1" -> null
      - hosted_zone_id                 = "Z2FDTNDATAQYW2" -> null
      - http_version                   = "http2" -> null
      - id                             = "E2KESP33B8DNIU" -> null
      - in_progress_validation_batches = 0 -> null
      - is_ipv6_enabled                = true -> null
      - last_modified_time             = "2017-11-19 04:09:36.548 +0000 UTC" -> null
      - price_class                    = "PriceClass_100" -> null
      - retain_on_delete               = false -> null
      - status                         = "Deployed" -> null
      - tags                           = {
          - "Environment" = "production"
        } -> null
      - wait_for_deployment            = true -> null

      - default_cache_behavior {
          - allowed_methods        = [
              - "DELETE",
              - "GET",
              - "HEAD",
              - "OPTIONS",
              - "PATCH",
              - "POST",
              - "PUT",
            ] -> null
          - cached_methods         = [
              - "GET",
              - "HEAD",
            ] -> null
          - compress               = false -> null
          - default_ttl            = 3600 -> null
          - max_ttl                = 86400 -> null
          - min_ttl                = 0 -> null
          - smooth_streaming       = false -> null
          - target_origin_id       = "s3-media" -> null
          - trusted_signers        = [] -> null
          - viewer_protocol_policy = "https-only" -> null

          - forwarded_values {
              - headers                 = [] -> null
              - query_string            = false -> null
              - query_string_cache_keys = [] -> null

              - cookies {
                  - forward           = "none" -> null
                  - whitelisted_names = [] -> null
                }
            }
        }

      - origin {
          - domain_name = "www.hyperbolausercontent.net.s3.amazonaws.com" -> null
          - origin_id   = "s3-media" -> null
        }

      - restrictions {
          - geo_restriction {
              - locations        = [] -> null
              - restriction_type = "none" -> null
            }
        }

      - viewer_certificate {
          - acm_certificate_arn            = "arn:aws:acm:us-east-1:473124112471:certificate/ec75af41-df70-41d7-9766-01c71c80f0d3" -> null
          - cloudfront_default_certificate = false -> null
          - minimum_protocol_version       = "TLSv1.2_2018" -> null
          - ssl_support_method             = "sni-only" -> null
        }
    }

  # module.base.aws_iam_instance_profile.app will be destroyed
  - resource "aws_iam_instance_profile" "app" {
      - arn         = "arn:aws:iam::473124112471:instance-profile/app-profile-00f8d1802132e948040476a3b1" -> null
      - create_date = "2017-07-21T06:17:20Z" -> null
      - id          = "app-profile-00f8d1802132e948040476a3b1" -> null
      - name        = "app-profile-00f8d1802132e948040476a3b1" -> null
      - name_prefix = "app-profile-" -> null
      - path        = "/" -> null
      - role        = "app-role-00f8d1802132e948040476a3b0" -> null
      - roles       = [
          - "app-role-00f8d1802132e948040476a3b0",
        ] -> null
      - unique_id   = "AIPAIWNBNTHNR6PMCMXVQ" -> null
    }

  # module.base.aws_iam_role.app will be destroyed
  - resource "aws_iam_role" "app" {
      - arn                   = "arn:aws:iam::473124112471:role/app-role-00f8d1802132e948040476a3b0" -> null
      - assume_role_policy    = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = "sts:AssumeRole"
                      - Effect    = "Allow"
                      - Principal = {
                          - Service = "ec2.amazonaws.com"
                        }
                      - Sid       = "AppAssumeRole"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - create_date           = "2017-07-21T06:17:19Z" -> null
      - force_detach_policies = false -> null
      - id                    = "app-role-00f8d1802132e948040476a3b0" -> null
      - max_session_duration  = 3600 -> null
      - name                  = "app-role-00f8d1802132e948040476a3b0" -> null
      - name_prefix           = "app-role-" -> null
      - path                  = "/" -> null
      - tags                  = {} -> null
      - unique_id             = "AROAJR5B5YNSIOFJ4DKI6" -> null
    }

  # module.base.aws_iam_role_policy.app will be destroyed
  - resource "aws_iam_role_policy" "app" {
      - id          = "app-role-00f8d1802132e948040476a3b0:app-policy-00f8d1802132e948040476a3b2" -> null
      - name        = "app-policy-00f8d1802132e948040476a3b2" -> null
      - name_prefix = "app-policy-" -> null
      - policy      = jsonencode(
            {
              - Statement = [
                  - {
                      - Action   = [
                          - "s3:ListBucket",
                          - "s3:GetBucketLocation",
                        ]
                      - Effect   = "Allow"
                      - Resource = [
                          - "arn:aws:s3:::www.hyperbolausercontent.net",
                          - "arn:aws:s3:::hyperbola-app-backup-production",
                        ]
                      - Sid      = "AllowAppBucketPermissions"
                    },
                  - {
                      - Action   = [
                          - "s3:*Object*",
                        ]
                      - Effect   = "Allow"
                      - Resource = [
                          - "arn:aws:s3:::www.hyperbolausercontent.net/*",
                          - "arn:aws:s3:::hyperbola-app-backup-production/*",
                        ]
                      - Sid      = "AllowAppBucketContentPermissions"
                    },
                  - {
                      - Action   = [
                          - "ssm:GetParametersByPath",
                        ]
                      - Effect   = "Allow"
                      - Resource = [
                          - "arn:aws:ssm:*:*:parameter/app/production/*",
                        ]
                      - Sid      = "AllowSecretsAccess"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - role        = "app-role-00f8d1802132e948040476a3b0" -> null
    }

  # module.base.aws_route53_record.cdn-A will be destroyed
  - resource "aws_route53_record" "cdn-A" {
      - allow_overwrite = true -> null
      - fqdn            = "www.hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_www_A" -> null
      - name            = "www" -> null
      - records         = [] -> null
      - ttl             = 0 -> null
      - type            = "A" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null

      - alias {
          - evaluate_target_health = false -> null
          - name                   = "drk9p6kxy4a37.cloudfront.net" -> null
          - zone_id                = "Z2FDTNDATAQYW2" -> null
        }
    }

  # module.base.aws_route53_record.cdn-AAAA will be destroyed
  - resource "aws_route53_record" "cdn-AAAA" {
      - allow_overwrite = true -> null
      - fqdn            = "www.hyperbolausercontent.net" -> null
      - id              = "Z25GE9A9NRUR2N_www_AAAA" -> null
      - name            = "www" -> null
      - records         = [] -> null
      - ttl             = 0 -> null
      - type            = "AAAA" -> null
      - zone_id         = "Z25GE9A9NRUR2N" -> null

      - alias {
          - evaluate_target_health = false -> null
          - name                   = "drk9p6kxy4a37.cloudfront.net" -> null
          - zone_id                = "Z2FDTNDATAQYW2" -> null
        }
    }

  # module.mysql.aws_db_instance.main_rds_instance will be destroyed
  - resource "aws_db_instance" "main_rds_instance" {
      - address                               = "app-mysql-0058e036eab3f18e3d97fe5a7b.cpebqrq01cnd.us-west-2.rds.amazonaws.com" -> null
      - allocated_storage                     = 5 -> null
      - allow_major_version_upgrade           = false -> null
      - apply_immediately                     = true -> null
      - arn                                   = "arn:aws:rds:us-west-2:473124112471:db:app-mysql-0058e036eab3f18e3d97fe5a7b" -> null
      - auto_minor_version_upgrade            = true -> null
      - availability_zone                     = "us-west-2c" -> null
      - backup_retention_period               = 10 -> null
      - backup_window                         = "09:22-09:52" -> null
      - ca_cert_identifier                    = "rds-ca-2019" -> null
      - copy_tags_to_snapshot                 = false -> null
      - db_subnet_group_name                  = "app-mysql-subnet-group-0058e036eab3f18e3d97fe5a7a" -> null
      - delete_automated_backups              = true -> null
      - deletion_protection                   = false -> null
      - enabled_cloudwatch_logs_exports       = [] -> null
      - endpoint                              = "app-mysql-0058e036eab3f18e3d97fe5a7b.cpebqrq01cnd.us-west-2.rds.amazonaws.com:3306" -> null
      - engine                                = "mysql" -> null
      - engine_version                        = "5.7.19" -> null
      - final_snapshot_identifier             = "app-mysql-final-snapshot" -> null
      - hosted_zone_id                        = "Z1PVIF0B656C1W" -> null
      - iam_database_authentication_enabled   = false -> null
      - id                                    = "app-mysql-0058e036eab3f18e3d97fe5a7b" -> null
      - identifier                            = "app-mysql-0058e036eab3f18e3d97fe5a7b" -> null
      - identifier_prefix                     = "app-mysql-" -> null
      - instance_class                        = "db.t2.micro" -> null
      - iops                                  = 0 -> null
      - license_model                         = "general-public-license" -> null
      - maintenance_window                    = "sun:10:18-sun:10:48" -> null
      - max_allocated_storage                 = 0 -> null
      - monitoring_interval                   = 0 -> null
      - multi_az                              = false -> null
      - name                                  = "hyperbola" -> null
      - option_group_name                     = "default:mysql-5-7" -> null
      - parameter_group_name                  = "app-mysql-custom-params-0058e036eab3f18e3d97fe5a79" -> null
      - password                              = (sensitive value)
      - performance_insights_enabled          = false -> null
      - performance_insights_retention_period = 0 -> null
      - port                                  = 3306 -> null
      - publicly_accessible                   = false -> null
      - replicas                              = [] -> null
      - resource_id                           = "db-DQM3UVZ7THHR4QKWQZ4TEEOBAM" -> null
      - security_group_names                  = [] -> null
      - skip_final_snapshot                   = false -> null
      - status                                = "available" -> null
      - storage_encrypted                     = false -> null
      - storage_type                          = "gp2" -> null
      - tags                                  = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-mysql"
        } -> null
      - username                              = "app" -> null
      - vpc_security_group_ids                = [
          - "sg-a2381cdf",
        ] -> null

      - timeouts {}
    }

  # module.mysql.aws_db_parameter_group.main_rds_instance will be destroyed
  - resource "aws_db_parameter_group" "main_rds_instance" {
      - arn         = "arn:aws:rds:us-west-2:473124112471:pg:app-mysql-custom-params-0058e036eab3f18e3d97fe5a79" -> null
      - description = "Managed by Terraform" -> null
      - family      = "mysql5.7" -> null
      - id          = "app-mysql-custom-params-0058e036eab3f18e3d97fe5a79" -> null
      - name        = "app-mysql-custom-params-0058e036eab3f18e3d97fe5a79" -> null
      - name_prefix = "app-mysql-custom-params-" -> null
      - tags        = {
          - "Environment" = "production"
        } -> null

      - parameter {
          - apply_method = "immediate" -> null
          - name         = "character_set_client" -> null
          - value        = "utf8mb4" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "character_set_connection" -> null
          - value        = "utf8mb4" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "character_set_database" -> null
          - value        = "utf8mb4" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "character_set_results" -> null
          - value        = "utf8mb4" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "character_set_server" -> null
          - value        = "utf8mb4" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "collation_connection" -> null
          - value        = "utf8mb4_unicode_ci" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "collation_server" -> null
          - value        = "utf8mb4_unicode_ci" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "innodb_strict_mode" -> null
          - value        = "1" -> null
        }
      - parameter {
          - apply_method = "immediate" -> null
          - name         = "sql_mode" -> null
          - value        = "traditional" -> null
        }
    }

  # module.mysql.aws_db_subnet_group.main_db_subnet_group will be destroyed
  - resource "aws_db_subnet_group" "main_db_subnet_group" {
      - arn         = "arn:aws:rds:us-west-2:473124112471:subgrp:app-mysql-subnet-group-0058e036eab3f18e3d97fe5a7a" -> null
      - description = "RDS subnet group" -> null
      - id          = "app-mysql-subnet-group-0058e036eab3f18e3d97fe5a7a" -> null
      - name        = "app-mysql-subnet-group-0058e036eab3f18e3d97fe5a7a" -> null
      - name_prefix = "app-mysql-subnet-group-" -> null
      - subnet_ids  = [
          - "subnet-60d0ec3b",
          - "subnet-70a0dd16",
          - "subnet-d5f06d9d",
        ] -> null
      - tags        = {
          - "Environment" = "production"
        } -> null
    }

  # module.mysql.aws_security_group.main_db_access will be destroyed
  - resource "aws_security_group" "main_db_access" {
      - arn                    = "arn:aws:ec2:us-west-2:473124112471:security-group/sg-a2381cdf" -> null
      - description            = "Allow access to the database" -> null
      - egress                 = [] -> null
      - id                     = "sg-a2381cdf" -> null
      - ingress                = [
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 3306
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-5ffd4125",
                ]
              - self             = false
              - to_port          = 3306
            },
        ] -> null
      - name                   = "app-mysql-sg-0058e036eab3f18e3d97fe5a78" -> null
      - name_prefix            = "app-mysql-sg-" -> null
      - owner_id               = "473124112471" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Environment" = "production"
          - "Name"        = "app-prod-northwest-mysql-sg"
        } -> null
      - vpc_id                 = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.aws_network_acl.acl will be destroyed
  - resource "aws_network_acl" "acl" {
      - egress     = [
          - {
              - action          = "allow"
              - cidr_block      = ""
              - from_port       = 0
              - icmp_code       = 0
              - icmp_type       = 0
              - ipv6_cidr_block = "::/0"
              - protocol        = "-1"
              - rule_no         = 200
              - to_port         = 0
            },
          - {
              - action          = "allow"
              - cidr_block      = "0.0.0.0/0"
              - from_port       = 0
              - icmp_code       = 0
              - icmp_type       = 0
              - ipv6_cidr_block = ""
              - protocol        = "-1"
              - rule_no         = 100
              - to_port         = 0
            },
        ] -> null
      - id         = "acl-4e77e428" -> null
      - ingress    = [
          - {
              - action          = "allow"
              - cidr_block      = ""
              - from_port       = 0
              - icmp_code       = 0
              - icmp_type       = 0
              - ipv6_cidr_block = "::/0"
              - protocol        = "-1"
              - rule_no         = 200
              - to_port         = 0
            },
          - {
              - action          = "allow"
              - cidr_block      = "0.0.0.0/0"
              - from_port       = 0
              - icmp_code       = 0
              - icmp_type       = 0
              - ipv6_cidr_block = ""
              - protocol        = "-1"
              - rule_no         = 100
              - to_port         = 0
            },
        ] -> null
      - owner_id   = "473124112471" -> null
      - subnet_ids = [
          - "subnet-113a864a",
          - "subnet-2a3d8171",
          - "subnet-400a3609",
          - "subnet-46e7fd21",
          - "subnet-bfe7fdd8",
          - "subnet-dc043895",
        ] -> null
      - tags       = {
          - "Name" = "app-prod-northwest-all"
        } -> null
      - vpc_id     = "vpc-08d0186e" -> null
    }

  # module.secrets.aws_ssm_parameter.database_password will be destroyed
  - resource "aws_ssm_parameter" "database_password" {
      - arn         = "arn:aws:ssm:us-west-2:473124112471:parameter/app/production/DB_PASSWORD" -> null
      - description = "App database password" -> null
      - id          = "/app/production/DB_PASSWORD" -> null
      - key_id      = "alias/aws/ssm" -> null
      - name        = "/app/production/DB_PASSWORD" -> null
      - tags        = {
          - "Environment" = "production"
          - "Project"     = "app"
        } -> null
      - tier        = "Standard" -> null
      - type        = "SecureString" -> null
      - value       = (sensitive value)
      - version     = 1 -> null
    }

  # module.secrets.aws_ssm_parameter.secret_key will be destroyed
  - resource "aws_ssm_parameter" "secret_key" {
      - arn         = "arn:aws:ssm:us-west-2:473124112471:parameter/app/production/SECRET_KEY" -> null
      - description = "Django secret key" -> null
      - id          = "/app/production/SECRET_KEY" -> null
      - key_id      = "alias/aws/ssm" -> null
      - name        = "/app/production/SECRET_KEY" -> null
      - tags        = {
          - "Environment" = "production"
          - "Project"     = "app"
        } -> null
      - tier        = "Standard" -> null
      - type        = "SecureString" -> null
      - value       = (sensitive value)
      - version     = 1 -> null
    }

  # module.mysql.module.subnets.aws_route_table.private[0] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-fa702f83" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-mysql.us-west-2a"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.mysql.module.subnets.aws_route_table.private[1] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-82722dfb" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-mysql.us-west-2b"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.mysql.module.subnets.aws_route_table.private[2] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-5a702f23" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-mysql.us-west-2c"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.mysql.module.subnets.aws_route_table_association.private[0] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-636cbf18" -> null
      - route_table_id = "rtb-fa702f83" -> null
      - subnet_id      = "subnet-d5f06d9d" -> null
    }

  # module.mysql.module.subnets.aws_route_table_association.private[1] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-486ebd33" -> null
      - route_table_id = "rtb-82722dfb" -> null
      - subnet_id      = "subnet-70a0dd16" -> null
    }

  # module.mysql.module.subnets.aws_route_table_association.private[2] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-c36dbeb8" -> null
      - route_table_id = "rtb-5a702f23" -> null
      - subnet_id      = "subnet-60d0ec3b" -> null
    }

  # module.mysql.module.subnets.aws_subnet.private[0] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-d5f06d9d" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2a" -> null
      - availability_zone_id            = "usw2-az2" -> null
      - cidr_block                      = "10.149.160.0/24" -> null
      - id                              = "subnet-d5f06d9d" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a5a0::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-8b7871f3" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-mysql.us-west-2a"
          - "Network" = "subnet-tier-5"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.mysql.module.subnets.aws_subnet.private[1] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-70a0dd16" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2b" -> null
      - availability_zone_id            = "usw2-az1" -> null
      - cidr_block                      = "10.149.161.0/24" -> null
      - id                              = "subnet-70a0dd16" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a5a1::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-eecd2d87" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-mysql.us-west-2b"
          - "Network" = "subnet-tier-5"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.mysql.module.subnets.aws_subnet.private[2] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-60d0ec3b" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2c" -> null
      - availability_zone_id            = "usw2-az3" -> null
      - cidr_block                      = "10.149.162.0/24" -> null
      - id                              = "subnet-60d0ec3b" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a5a2::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-4389ab09" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-mysql.us-west-2c"
          - "Network" = "subnet-tier-5"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.aws_security_group.ssm will be destroyed
  - resource "aws_security_group" "ssm" {
      - arn                    = "arn:aws:ec2:us-west-2:473124112471:security-group/sg-0258424690602bd25" -> null
      - description            = "SSM VPC Endpoint Security Group" -> null
      - egress                 = [] -> null
      - id                     = "sg-0258424690602bd25" -> null
      - ingress                = [
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "-1"
              - security_groups  = [
                  - "sg-053efd7127835f9c3",
                ]
              - self             = false
              - to_port          = 0
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "-1"
              - security_groups  = [
                  - "sg-5ffd4125",
                ]
              - self             = false
              - to_port          = 0
            },
        ] -> null
      - name                   = "ssm-sg-20181112012252024800000001" -> null
      - name_prefix            = "ssm-sg-" -> null
      - owner_id               = "473124112471" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {} -> null
      - vpc_id                 = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.aws_security_group.this will be destroyed
  - resource "aws_security_group" "this" {
      - arn                    = "arn:aws:ec2:us-west-2:473124112471:security-group/sg-053efd7127835f9c3" -> null
      - description            = "Management Domain Security Group" -> null
      - egress                 = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 443
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 443
            },
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 80
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 443
              - ipv6_cidr_blocks = [
                  - "::/0",
                ]
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 443
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 443
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-0258424690602bd25",
                ]
              - self             = false
              - to_port          = 443
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = [
                  - "::/0",
                ]
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 80
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-0258424690602bd25",
                ]
              - self             = false
              - to_port          = 80
            },
        ] -> null
      - id                     = "sg-053efd7127835f9c3" -> null
      - ingress                = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 22
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 22
            },
          - {
              - cidr_blocks      = []
              - description      = ""
              - from_port        = 22
              - ipv6_cidr_blocks = [
                  - "::/0",
                ]
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 22
            },
        ] -> null
      - name                   = "management-sg-20181111224432945200000001" -> null
      - name_prefix            = "management-sg-" -> null
      - owner_id               = "473124112471" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Class" = "management"
        } -> null
      - vpc_id                 = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.aws_security_group_rule.ssm_endpoint_from_management will be destroyed
  - resource "aws_security_group_rule" "ssm_endpoint_from_management" {
      - cidr_blocks              = [] -> null
      - from_port                = 0 -> null
      - id                       = "sgrule-1308896626" -> null
      - ipv6_cidr_blocks         = [] -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "-1" -> null
      - security_group_id        = "sg-0258424690602bd25" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-053efd7127835f9c3" -> null
      - to_port                  = 0 -> null
      - type                     = "ingress" -> null
    }

  # module.network.module.management.aws_vpc_endpoint.s3 will be destroyed
  - resource "aws_vpc_endpoint" "s3" {
      - cidr_blocks           = [
          - "52.218.128.0/17",
        ] -> null
      - dns_entry             = [] -> null
      - id                    = "vpce-0d077733dd16688af" -> null
      - network_interface_ids = [] -> null
      - owner_id              = "473124112471" -> null
      - policy                = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = "*"
                      - Effect    = "Allow"
                      - Principal = "*"
                      - Resource  = "*"
                    },
                ]
              - Version   = "2008-10-17"
            }
        ) -> null
      - prefix_list_id        = "pl-68a54001" -> null
      - private_dns_enabled   = false -> null
      - requester_managed     = false -> null
      - route_table_ids       = [
          - "rtb-00a32c905eba02447",
          - "rtb-00a5d8d6338b91e33",
          - "rtb-01399507207aed8cc",
          - "rtb-0273f9500b21931f6",
          - "rtb-095d5551201e2631e",
          - "rtb-09fc7ce039d02974d",
          - "rtb-0abb1bd018750a695",
          - "rtb-0b2f17a06718620be",
          - "rtb-42cc9e24",
          - "rtb-6b431c12",
          - "rtb-98421de1",
          - "rtb-b6431ccf",
        ] -> null
      - security_group_ids    = [] -> null
      - service_name          = "com.amazonaws.us-west-2.s3" -> null
      - state                 = "available" -> null
      - subnet_ids            = [] -> null
      - tags                  = {} -> null
      - vpc_endpoint_type     = "Gateway" -> null
      - vpc_id                = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.aws_vpc_endpoint.ssm will be destroyed
  - resource "aws_vpc_endpoint" "ssm" {
      - cidr_blocks           = [] -> null
      - dns_entry             = [
          - {
              - dns_name       = "vpce-0eebe69e470d4c103-rcckwkho.ssm.us-west-2.vpce.amazonaws.com"
              - hosted_zone_id = "Z1YSA3EXCYUU9Z"
            },
          - {
              - dns_name       = "vpce-0eebe69e470d4c103-rcckwkho-us-west-2c.ssm.us-west-2.vpce.amazonaws.com"
              - hosted_zone_id = "Z1YSA3EXCYUU9Z"
            },
          - {
              - dns_name       = "vpce-0eebe69e470d4c103-rcckwkho-us-west-2b.ssm.us-west-2.vpce.amazonaws.com"
              - hosted_zone_id = "Z1YSA3EXCYUU9Z"
            },
          - {
              - dns_name       = "vpce-0eebe69e470d4c103-rcckwkho-us-west-2a.ssm.us-west-2.vpce.amazonaws.com"
              - hosted_zone_id = "Z1YSA3EXCYUU9Z"
            },
          - {
              - dns_name       = "ssm.us-west-2.amazonaws.com"
              - hosted_zone_id = "Z2EJ2YPX0Z2JQH"
            },
        ] -> null
      - id                    = "vpce-0eebe69e470d4c103" -> null
      - network_interface_ids = [
          - "eni-0445cae8665638fb5",
          - "eni-08bdd1b026fc31e28",
          - "eni-0ed38954739e13756",
        ] -> null
      - owner_id              = "473124112471" -> null
      - policy                = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = "*"
                      - Effect    = "Allow"
                      - Principal = "*"
                      - Resource  = "*"
                    },
                ]
            }
        ) -> null
      - private_dns_enabled   = true -> null
      - requester_managed     = false -> null
      - route_table_ids       = [] -> null
      - security_group_ids    = [
          - "sg-0258424690602bd25",
        ] -> null
      - service_name          = "com.amazonaws.us-west-2.ssm" -> null
      - state                 = "available" -> null
      - subnet_ids            = [
          - "subnet-000c2e9bc0fa1f4ad",
          - "subnet-0485f887e73a69d40",
          - "subnet-0a019a1fb0d5aba75",
        ] -> null
      - tags                  = {} -> null
      - vpc_endpoint_type     = "Interface" -> null
      - vpc_id                = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.private_subnet.aws_route_table.private[0] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-98421de1" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-private.us-west-2a"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.private_subnet.aws_route_table.private[1] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-b6431ccf" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-private.us-west-2b"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.private_subnet.aws_route_table.private[2] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-6b431c12" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-private.us-west-2c"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.private_subnet.aws_route_table_association.private[0] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-7979aa02" -> null
      - route_table_id = "rtb-98421de1" -> null
      - subnet_id      = "subnet-400a3609" -> null
    }

  # module.network.module.private_subnet.aws_route_table_association.private[1] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-6375a618" -> null
      - route_table_id = "rtb-b6431ccf" -> null
      - subnet_id      = "subnet-46e7fd21" -> null
    }

  # module.network.module.private_subnet.aws_route_table_association.private[2] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-dd79aaa6" -> null
      - route_table_id = "rtb-6b431c12" -> null
      - subnet_id      = "subnet-2a3d8171" -> null
    }

  # module.network.module.private_subnet.aws_subnet.private[0] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-400a3609" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2a" -> null
      - availability_zone_id            = "usw2-az2" -> null
      - cidr_block                      = "10.149.64.0/24" -> null
      - id                              = "subnet-400a3609" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a540::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-ca8785b2" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-private.us-west-2a"
          - "Network" = "subnet-tier-2"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.private_subnet.aws_subnet.private[1] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-46e7fd21" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2b" -> null
      - availability_zone_id            = "usw2-az1" -> null
      - cidr_block                      = "10.149.65.0/24" -> null
      - id                              = "subnet-46e7fd21" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a541::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-30b45259" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-private.us-west-2b"
          - "Network" = "subnet-tier-2"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.private_subnet.aws_subnet.private[2] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-2a3d8171" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2c" -> null
      - availability_zone_id            = "usw2-az3" -> null
      - cidr_block                      = "10.149.66.0/24" -> null
      - id                              = "subnet-2a3d8171" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a542::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-986f4cd2" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-private.us-west-2c"
          - "Network" = "subnet-tier-2"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.public_subnet.aws_route_table.public[0] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-42cc9e24" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-public.us-west-2a"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.public_subnet.aws_route_table.public[1] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-01399507207aed8cc" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-public.us-west-2b"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.public_subnet.aws_route_table.public[2] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-09fc7ce039d02974d" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-public.us-west-2c"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.public_subnet.aws_route_table_association.public[0] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-c83703b1" -> null
      - route_table_id = "rtb-42cc9e24" -> null
      - subnet_id      = "subnet-dc043895" -> null
    }

  # module.network.module.public_subnet.aws_route_table_association.public[1] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-0b62e1e2c1b721ea4" -> null
      - route_table_id = "rtb-01399507207aed8cc" -> null
      - subnet_id      = "subnet-bfe7fdd8" -> null
    }

  # module.network.module.public_subnet.aws_route_table_association.public[2] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-00fd5347b4f3b3182" -> null
      - route_table_id = "rtb-09fc7ce039d02974d" -> null
      - subnet_id      = "subnet-113a864a" -> null
    }

  # module.network.module.public_subnet.aws_subnet.public[0] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-dc043895" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2a" -> null
      - availability_zone_id            = "usw2-az2" -> null
      - cidr_block                      = "10.149.32.0/24" -> null
      - id                              = "subnet-dc043895" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a520::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-c7888abf" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-public.us-west-2a"
          - "Network" = "subnet-tier-1"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.public_subnet.aws_subnet.public[1] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-bfe7fdd8" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2b" -> null
      - availability_zone_id            = "usw2-az1" -> null
      - cidr_block                      = "10.149.33.0/24" -> null
      - id                              = "subnet-bfe7fdd8" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a521::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-2fab4d46" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-public.us-west-2b"
          - "Network" = "subnet-tier-1"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.public_subnet.aws_subnet.public[2] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-113a864a" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2c" -> null
      - availability_zone_id            = "usw2-az3" -> null
      - cidr_block                      = "10.149.34.0/24" -> null
      - id                              = "subnet-113a864a" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a522::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-ee684ba4" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-public.us-west-2c"
          - "Network" = "subnet-tier-1"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.vpc.aws_egress_only_internet_gateway.this will be destroyed
  - resource "aws_egress_only_internet_gateway" "this" {
      - id     = "eigw-053a3838325edd831" -> null
      - vpc_id = "vpc-08d0186e" -> null
    }

  # module.network.module.vpc.aws_internet_gateway.this will be destroyed
  - resource "aws_internet_gateway" "this" {
      - id       = "igw-0dfd786a" -> null
      - owner_id = "473124112471" -> null
      - tags     = {
          - "Name" = "app-prod-northwest-vpc"
        } -> null
      - vpc_id   = "vpc-08d0186e" -> null
    }

  # module.network.module.vpc.aws_vpc.this will be destroyed
  - resource "aws_vpc" "this" {
      - arn                              = "arn:aws:ec2:us-west-2:473124112471:vpc/vpc-08d0186e" -> null
      - assign_generated_ipv6_cidr_block = true -> null
      - cidr_block                       = "10.149.0.0/16" -> null
      - default_network_acl_id           = "acl-4d74e72b" -> null
      - default_route_table_id           = "rtb-99ce9cff" -> null
      - default_security_group_id        = "sg-ef57fa95" -> null
      - dhcp_options_id                  = "dopt-0495df60" -> null
      - enable_classiclink               = false -> null
      - enable_classiclink_dns_support   = false -> null
      - enable_dns_hostnames             = true -> null
      - enable_dns_support               = true -> null
      - id                               = "vpc-08d0186e" -> null
      - instance_tenancy                 = "default" -> null
      - ipv6_association_id              = "vpc-cidr-assoc-61840609" -> null
      - ipv6_cidr_block                  = "2600:1f14:1b1:a500::/56" -> null
      - main_route_table_id              = "rtb-99ce9cff" -> null
      - owner_id                         = "473124112471" -> null
      - tags                             = {
          - "Name" = "app-prod-northwest-vpc"
        } -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table.private[0] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-00a5d8d6338b91e33" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-private.us-west-2a"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table.private[1] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-00a32c905eba02447" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-private.us-west-2b"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table.private[2] will be destroyed
  - resource "aws_route_table" "private" {
      - id               = "rtb-0b2f17a06718620be" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-private.us-west-2c"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table_association.private[0] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-05ea90604a19a06e3" -> null
      - route_table_id = "rtb-00a5d8d6338b91e33" -> null
      - subnet_id      = "subnet-000c2e9bc0fa1f4ad" -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table_association.private[1] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-0cb817938a8ba2087" -> null
      - route_table_id = "rtb-00a32c905eba02447" -> null
      - subnet_id      = "subnet-0a019a1fb0d5aba75" -> null
    }

  # module.network.module.management.module.private_subnet.aws_route_table_association.private[2] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-0cfdc3b0d395859a4" -> null
      - route_table_id = "rtb-0b2f17a06718620be" -> null
      - subnet_id      = "subnet-0485f887e73a69d40" -> null
    }

  # module.network.module.management.module.private_subnet.aws_subnet.private[0] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-000c2e9bc0fa1f4ad" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2a" -> null
      - availability_zone_id            = "usw2-az2" -> null
      - cidr_block                      = "10.149.128.0/24" -> null
      - id                              = "subnet-000c2e9bc0fa1f4ad" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a580::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-0b5676ecaf90cb306" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-private.us-west-2a"
          - "Network" = "subnet-tier-4"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.module.private_subnet.aws_subnet.private[1] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-0a019a1fb0d5aba75" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2b" -> null
      - availability_zone_id            = "usw2-az1" -> null
      - cidr_block                      = "10.149.129.0/24" -> null
      - id                              = "subnet-0a019a1fb0d5aba75" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a581::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-07dd42d7cea11c85b" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-private.us-west-2b"
          - "Network" = "subnet-tier-4"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.module.private_subnet.aws_subnet.private[2] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-0485f887e73a69d40" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2c" -> null
      - availability_zone_id            = "usw2-az3" -> null
      - cidr_block                      = "10.149.130.0/24" -> null
      - id                              = "subnet-0485f887e73a69d40" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a582::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-08d085c48b70fb171" -> null
      - map_public_ip_on_launch         = false -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-private.us-west-2c"
          - "Network" = "subnet-tier-4"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.module.public_subnet.aws_route_table.public[0] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-0abb1bd018750a695" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-public.us-west-2a"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.public_subnet.aws_route_table.public[1] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-0273f9500b21931f6" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-public.us-west-2b"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.public_subnet.aws_route_table.public[2] will be destroyed
  - resource "aws_route_table" "public" {
      - id               = "rtb-095d5551201e2631e" -> null
      - owner_id         = "473124112471" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                = ""
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = "::/0"
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
          - {
              - cidr_block                = "0.0.0.0/0"
              - egress_only_gateway_id    = ""
              - gateway_id                = "igw-0dfd786a"
              - instance_id               = ""
              - ipv6_cidr_block           = ""
              - nat_gateway_id            = ""
              - network_interface_id      = ""
              - transit_gateway_id        = ""
              - vpc_peering_connection_id = ""
            },
        ] -> null
      - tags             = {
          - "Name" = "app-prod-northwest-management-public.us-west-2c"
        } -> null
      - vpc_id           = "vpc-08d0186e" -> null
    }

  # module.network.module.management.module.public_subnet.aws_route_table_association.public[0] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-0705bb27327ea3421" -> null
      - route_table_id = "rtb-0abb1bd018750a695" -> null
      - subnet_id      = "subnet-03016b54639ef2fbb" -> null
    }

  # module.network.module.management.module.public_subnet.aws_route_table_association.public[1] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-0c7351142f221c655" -> null
      - route_table_id = "rtb-0273f9500b21931f6" -> null
      - subnet_id      = "subnet-011c372fcaeea68f4" -> null
    }

  # module.network.module.management.module.public_subnet.aws_route_table_association.public[2] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-0c70dce4713041447" -> null
      - route_table_id = "rtb-095d5551201e2631e" -> null
      - subnet_id      = "subnet-05b3590a52783b057" -> null
    }

  # module.network.module.management.module.public_subnet.aws_subnet.public[0] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-03016b54639ef2fbb" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2a" -> null
      - availability_zone_id            = "usw2-az2" -> null
      - cidr_block                      = "10.149.96.0/24" -> null
      - id                              = "subnet-03016b54639ef2fbb" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a560::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-0b4cb7b58039f09bc" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-public.us-west-2a"
          - "Network" = "subnet-tier-3"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.module.public_subnet.aws_subnet.public[1] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-011c372fcaeea68f4" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2b" -> null
      - availability_zone_id            = "usw2-az1" -> null
      - cidr_block                      = "10.149.97.0/24" -> null
      - id                              = "subnet-011c372fcaeea68f4" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a561::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-068f13da6ec566218" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-public.us-west-2b"
          - "Network" = "subnet-tier-3"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

  # module.network.module.management.module.public_subnet.aws_subnet.public[2] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                             = "arn:aws:ec2:us-west-2:473124112471:subnet/subnet-05b3590a52783b057" -> null
      - assign_ipv6_address_on_creation = true -> null
      - availability_zone               = "us-west-2c" -> null
      - availability_zone_id            = "usw2-az3" -> null
      - cidr_block                      = "10.149.98.0/24" -> null
      - id                              = "subnet-05b3590a52783b057" -> null
      - ipv6_cidr_block                 = "2600:1f14:1b1:a562::/64" -> null
      - ipv6_cidr_block_association_id  = "subnet-cidr-assoc-03c2f5d2ca4330925" -> null
      - map_public_ip_on_launch         = true -> null
      - owner_id                        = "473124112471" -> null
      - tags                            = {
          - "Name"    = "app-prod-northwest-management-public.us-west-2c"
          - "Network" = "subnet-tier-3"
        } -> null
      - vpc_id                          = "vpc-08d0186e" -> null

      - timeouts {}
    }

Plan: 0 to add, 0 to change, 87 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

module.mysql.module.subnets.aws_route_table_association.private[1]: Destroying... [id=rtbassoc-486ebd33]
module.mysql.module.subnets.aws_route_table_association.private[2]: Destroying... [id=rtbassoc-c36dbeb8]
module.network.module.public_subnet.aws_route_table_association.public[1]: Destroying... [id=rtbassoc-0b62e1e2c1b721ea4]
module.network.module.management.module.private_subnet.aws_route_table_association.private[2]: Destroying... [id=rtbassoc-0cfdc3b0d395859a4]
aws_route53_record.mysql: Destroying... [id=Z1O2JQV3R0LG26_mysql_CNAME]
module.network.module.private_subnet.aws_route_table_association.private[2]: Destroying... [id=rtbassoc-dd79aaa6]
module.network.module.management.module.private_subnet.aws_route_table_association.private[1]: Destroying... [id=rtbassoc-0cb817938a8ba2087]
module.backend.aws_security_group_rule.backend-from-alb-http: Destroying... [id=sgrule-3372377313]
module.backend.aws_security_group_rule.backend_to_ssm_endpoint: Destroying... [id=sgrule-2455676943]
module.network.module.private_subnet.aws_route_table_association.private[1]: Destroying... [id=rtbassoc-6375a618]
module.network.module.management.module.private_subnet.aws_route_table_association.private[2]: Destruction complete after 0s
module.base.aws_route53_record.cdn-A: Destroying... [id=Z25GE9A9NRUR2N_www_A]
module.mysql.module.subnets.aws_route_table_association.private[2]: Destruction complete after 0s
module.network.aws_network_acl.acl: Destroying... [id=acl-4e77e428]
module.mysql.module.subnets.aws_route_table_association.private[1]: Destruction complete after 0s
module.network.module.public_subnet.aws_route_table_association.public[1]: Destruction complete after 0s
module.backend.aws_alb_listener.alb-http: Destroying... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/a2bb653297384a8e]
module.backend.aws_security_group_rule.backend-from-alb-health-check: Destroying... [id=sgrule-2556693372]
module.network.module.private_subnet.aws_route_table_association.private[2]: Destruction complete after 0s
module.network.module.public_subnet.aws_route_table_association.public[2]: Destroying... [id=rtbassoc-00fd5347b4f3b3182]
module.network.module.management.module.private_subnet.aws_route_table_association.private[1]: Destruction complete after 0s
module.network.module.management.aws_vpc_endpoint.ssm: Destroying... [id=vpce-0eebe69e470d4c103]
module.network.module.private_subnet.aws_route_table_association.private[1]: Destruction complete after 0s
module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaleup: Destroying... [id=app-prod-northwest-backend-scaleup-cpu-alarm]
module.backend.aws_alb_listener.alb-http: Destruction complete after 0s
module.network.module.management.aws_security_group_rule.ssm_endpoint_from_management: Destroying... [id=sgrule-1308896626]
module.backend.aws_security_group_rule.backend-from-alb-http: Destruction complete after 0s
module.network.module.management.module.public_subnet.aws_route_table_association.public[2]: Destroying... [id=rtbassoc-0c70dce4713041447]
module.network.module.public_subnet.aws_route_table_association.public[2]: Destruction complete after 0s
module.backend.aws_security_group_rule.backend-to-s3-endpoint: Destroying... [id=sgrule-1220853808]
module.network.module.management.module.public_subnet.aws_route_table_association.public[2]: Destruction complete after 0s
module.network.module.management.module.private_subnet.aws_route_table_association.private[0]: Destroying... [id=rtbassoc-05ea90604a19a06e3]
module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaleup: Destruction complete after 0s
module.network.module.management.module.public_subnet.aws_route_table_association.public[0]: Destroying... [id=rtbassoc-0705bb27327ea3421]
module.backend.aws_security_group_rule.backend_to_ssm_endpoint: Destruction complete after 1s
module.base.aws_route53_record.cdn-AAAA: Destroying... [id=Z25GE9A9NRUR2N_www_AAAA]
module.network.module.management.module.private_subnet.aws_route_table_association.private[0]: Destruction complete after 1s
module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaledown: Destroying... [id=app-prod-northwest-backend-scaledown-cpu-alarm]
module.network.module.management.aws_security_group_rule.ssm_endpoint_from_management: Destruction complete after 1s
module.base.aws_iam_role_policy.app: Destroying... [id=app-role-00f8d1802132e948040476a3b0:app-policy-00f8d1802132e948040476a3b2]
module.network.module.management.module.public_subnet.aws_route_table_association.public[0]: Destruction complete after 1s
module.network.module.private_subnet.aws_route_table_association.private[0]: Destroying... [id=rtbassoc-7979aa02]
module.network.module.private_subnet.aws_route_table_association.private[0]: Destruction complete after 0s
module.mysql.module.subnets.aws_route_table_association.private[0]: Destroying... [id=rtbassoc-636cbf18]
module.backend.aws_cloudwatch_metric_alarm.backend-cpu-scaledown: Destruction complete after 0s
module.network.module.public_subnet.aws_route_table_association.public[0]: Destroying... [id=rtbassoc-c83703b1]
module.base.aws_iam_role_policy.app: Destruction complete after 0s
module.secrets.aws_ssm_parameter.database_password: Destroying... [id=/app/production/DB_PASSWORD]
module.backend.aws_security_group_rule.backend-from-alb-health-check: Destruction complete after 1s
module.backend.aws_security_group_rule.ssm_endpoint_from_backend: Destroying... [id=sgrule-1886272967]
module.secrets.aws_ssm_parameter.database_password: Destruction complete after 0s
module.secrets.aws_ssm_parameter.secret_key: Destroying... [id=/app/production/SECRET_KEY]
module.mysql.module.subnets.aws_route_table_association.private[0]: Destruction complete after 0s
module.network.module.management.module.public_subnet.aws_route_table_association.public[1]: Destroying... [id=rtbassoc-0c7351142f221c655]
module.network.module.public_subnet.aws_route_table_association.public[0]: Destruction complete after 0s
module.backend.aws_alb_listener.alb-https: Destroying... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:listener/app/applb-20171106080744451200000003/45bf0d921a80598a/f98b62f677df1e1c]
module.secrets.aws_ssm_parameter.secret_key: Destruction complete after 0s
module.network.module.vpc.aws_egress_only_internet_gateway.this: Destroying... [id=eigw-053a3838325edd831]
module.backend.aws_alb_listener.alb-https: Destruction complete after 0s
module.backend.aws_autoscaling_policy.backend-scaleup: Destroying... [id=app-prod-northwest-backend-scaleup-policy]
module.network.module.management.module.public_subnet.aws_route_table_association.public[1]: Destruction complete after 0s
module.network.module.management.aws_security_group.this: Destroying... [id=sg-053efd7127835f9c3]
module.backend.aws_security_group_rule.backend-to-s3-endpoint: Destruction complete after 1s
module.backend.aws_autoscaling_policy.backend-scaledown: Destroying... [id=app-prod-northwest-backend-scaledown-policy]
module.backend.aws_security_group_rule.ssm_endpoint_from_backend: Destruction complete after 0s
module.mysql.module.subnets.aws_route_table.private[2]: Destroying... [id=rtb-5a702f23]
module.network.module.vpc.aws_egress_only_internet_gateway.this: Destruction complete after 0s
module.mysql.module.subnets.aws_route_table.private[0]: Destroying... [id=rtb-fa702f83]
module.network.module.management.aws_security_group.this: Destruction complete after 1s
module.mysql.module.subnets.aws_route_table.private[1]: Destroying... [id=rtb-82722dfb]
module.backend.aws_autoscaling_policy.backend-scaleup: Destruction complete after 1s
module.backend.aws_alb.alb: Destroying... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:loadbalancer/app/applb-20171106080744451200000003/45bf0d921a80598a]
module.backend.aws_autoscaling_policy.backend-scaledown: Destruction complete after 1s
module.network.module.management.module.public_subnet.aws_subnet.public[2]: Destroying... [id=subnet-05b3590a52783b057]
module.mysql.module.subnets.aws_route_table.private[0]: Destruction complete after 1s
module.network.module.management.module.public_subnet.aws_subnet.public[0]: Destroying... [id=subnet-03016b54639ef2fbb]
module.mysql.module.subnets.aws_route_table.private[2]: Destruction complete after 1s
module.network.module.management.module.public_subnet.aws_subnet.public[1]: Destroying... [id=subnet-011c372fcaeea68f4]
module.mysql.module.subnets.aws_route_table.private[1]: Destruction complete after 0s
module.network.module.management.aws_vpc_endpoint.s3: Destroying... [id=vpce-0d077733dd16688af]
module.network.module.management.module.public_subnet.aws_subnet.public[2]: Destruction complete after 0s
module.backend.aws_autoscaling_group.backend: Destroying... [id=app-backend-asg-20181105004601904200000003]
module.network.module.management.module.public_subnet.aws_subnet.public[1]: Destruction complete after 0s
module.network.module.management.module.public_subnet.aws_subnet.public[0]: Destruction complete after 0s
module.backend.aws_alb.alb: Destruction complete after 0s
module.backend.aws_security_group.alb: Destroying... [id=sg-d88caea5]
module.network.module.public_subnet.aws_subnet.public[2]: Destroying... [id=subnet-113a864a]
module.network.module.public_subnet.aws_subnet.public[0]: Destroying... [id=subnet-dc043895]
module.network.aws_network_acl.acl: Destruction complete after 3s
module.network.module.public_subnet.aws_subnet.public[1]: Destroying... [id=subnet-bfe7fdd8]
module.network.module.public_subnet.aws_subnet.public[0]: Destruction complete after 1s
module.network.module.management.aws_vpc_endpoint.s3: Destruction complete after 5s
module.network.module.management.module.private_subnet.aws_route_table.private[1]: Destroying... [id=rtb-00a32c905eba02447]
module.network.module.public_subnet.aws_route_table.public[0]: Destroying... [id=rtb-42cc9e24]
module.network.module.public_subnet.aws_route_table.public[0]: Destruction complete after 1s
module.network.module.private_subnet.aws_route_table.private[0]: Destroying... [id=rtb-98421de1]
module.network.module.management.module.private_subnet.aws_route_table.private[1]: Destruction complete after 1s
module.network.module.management.module.public_subnet.aws_route_table.public[2]: Destroying... [id=rtb-095d5551201e2631e]
module.network.module.private_subnet.aws_route_table.private[0]: Destruction complete after 0s
module.network.module.public_subnet.aws_route_table.public[2]: Destroying... [id=rtb-09fc7ce039d02974d]
module.network.module.management.module.public_subnet.aws_route_table.public[2]: Destruction complete after 0s
module.network.module.management.module.private_subnet.aws_route_table.private[2]: Destroying... [id=rtb-0b2f17a06718620be]
module.network.module.public_subnet.aws_route_table.public[2]: Destruction complete after 0s
module.network.module.private_subnet.aws_route_table.private[1]: Destroying... [id=rtb-b6431ccf]
module.network.module.management.module.private_subnet.aws_route_table.private[2]: Destruction complete after 1s
module.network.module.management.module.public_subnet.aws_route_table.public[1]: Destroying... [id=rtb-0273f9500b21931f6]
module.network.module.private_subnet.aws_route_table.private[1]: Destruction complete after 1s
module.network.module.management.module.private_subnet.aws_route_table.private[0]: Destroying... [id=rtb-00a5d8d6338b91e33]
module.network.module.management.module.public_subnet.aws_route_table.public[1]: Destruction complete after 0s
module.network.module.private_subnet.aws_route_table.private[2]: Destroying... [id=rtb-6b431c12]
module.network.module.management.module.private_subnet.aws_route_table.private[0]: Destruction complete after 0s
module.network.module.management.module.public_subnet.aws_route_table.public[0]: Destroying... [id=rtb-0abb1bd018750a695]
module.network.module.private_subnet.aws_route_table.private[2]: Destruction complete after 0s
module.network.module.public_subnet.aws_route_table.public[1]: Destroying... [id=rtb-01399507207aed8cc]
module.network.module.management.module.public_subnet.aws_route_table.public[0]: Destruction complete after 1s
module.network.module.public_subnet.aws_route_table.public[1]: Destruction complete after 1s
module.network.module.vpc.aws_internet_gateway.this: Destroying... [id=igw-0dfd786a]
aws_route53_record.mysql: Still destroying... [id=Z1O2JQV3R0LG26_mysql_CNAME, 10s elapsed]
module.base.aws_route53_record.cdn-A: Still destroying... [id=Z25GE9A9NRUR2N_www_A, 10s elapsed]
module.network.module.management.aws_vpc_endpoint.ssm: Still destroying... [id=vpce-0eebe69e470d4c103, 10s elapsed]
module.base.aws_route53_record.cdn-AAAA: Still destroying... [id=Z25GE9A9NRUR2N_www_AAAA, 10s elapsed]
module.backend.aws_autoscaling_group.backend: Still destroying... [id=app-backend-asg-20181105004601904200000003, 10s elapsed]
module.backend.aws_security_group.alb: Still destroying... [id=sg-d88caea5, 10s elapsed]
module.network.module.public_subnet.aws_subnet.public[2]: Still destroying... [id=subnet-113a864a, 10s elapsed]
module.network.module.public_subnet.aws_subnet.public[1]: Still destroying... [id=subnet-bfe7fdd8, 10s elapsed]
module.network.module.vpc.aws_internet_gateway.this: Still destroying... [id=igw-0dfd786a, 10s elapsed]
aws_route53_record.mysql: Still destroying... [id=Z1O2JQV3R0LG26_mysql_CNAME, 20s elapsed]
module.base.aws_route53_record.cdn-A: Still destroying... [id=Z25GE9A9NRUR2N_www_A, 20s elapsed]
module.network.module.management.aws_vpc_endpoint.ssm: Still destroying... [id=vpce-0eebe69e470d4c103, 20s elapsed]
module.base.aws_route53_record.cdn-AAAA: Still destroying... [id=Z25GE9A9NRUR2N_www_AAAA, 20s elapsed]
module.backend.aws_autoscaling_group.backend: Still destroying... [id=app-backend-asg-20181105004601904200000003, 20s elapsed]
module.backend.aws_security_group.alb: Still destroying... [id=sg-d88caea5, 20s elapsed]
module.network.module.public_subnet.aws_subnet.public[2]: Still destroying... [id=subnet-113a864a, 20s elapsed]
module.network.module.public_subnet.aws_subnet.public[1]: Still destroying... [id=subnet-bfe7fdd8, 20s elapsed]
module.network.module.vpc.aws_internet_gateway.this: Still destroying... [id=igw-0dfd786a, 20s elapsed]
aws_route53_record.mysql: Still destroying... [id=Z1O2JQV3R0LG26_mysql_CNAME, 30s elapsed]
module.base.aws_route53_record.cdn-A: Still destroying... [id=Z25GE9A9NRUR2N_www_A, 30s elapsed]
module.network.module.management.aws_vpc_endpoint.ssm: Still destroying... [id=vpce-0eebe69e470d4c103, 30s elapsed]
module.base.aws_route53_record.cdn-AAAA: Still destroying... [id=Z25GE9A9NRUR2N_www_AAAA, 30s elapsed]
module.base.aws_route53_record.cdn-A: Destruction complete after 32s
module.backend.aws_autoscaling_group.backend: Still destroying... [id=app-backend-asg-20181105004601904200000003, 30s elapsed]
module.backend.aws_security_group.alb: Still destroying... [id=sg-d88caea5, 30s elapsed]
module.network.module.public_subnet.aws_subnet.public[2]: Still destroying... [id=subnet-113a864a, 30s elapsed]
module.network.module.public_subnet.aws_subnet.public[1]: Still destroying... [id=subnet-bfe7fdd8, 30s elapsed]
module.base.aws_route53_record.cdn-AAAA: Destruction complete after 37s
module.base.aws_cloudfront_distribution.cdn: Destroying... [id=E2KESP33B8DNIU]
module.network.module.vpc.aws_internet_gateway.this: Still destroying... [id=igw-0dfd786a, 30s elapsed]
aws_route53_record.mysql: Still destroying... [id=Z1O2JQV3R0LG26_mysql_CNAME, 40s elapsed]
module.network.module.management.aws_vpc_endpoint.ssm: Still destroying... [id=vpce-0eebe69e470d4c103, 40s elapsed]
module.backend.aws_autoscaling_group.backend: Still destroying... [id=app-backend-asg-20181105004601904200000003, 40s elapsed]
module.network.module.public_subnet.aws_subnet.public[2]: Still destroying... [id=subnet-113a864a, 40s elapsed]
module.backend.aws_security_group.alb: Still destroying... [id=sg-d88caea5, 40s elapsed]
module.network.module.public_subnet.aws_subnet.public[1]: Still destroying... [id=subnet-bfe7fdd8, 40s elapsed]
module.network.module.vpc.aws_internet_gateway.this: Destruction complete after 35s
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E2KESP33B8DNIU, 10s elapsed]
aws_route53_record.mysql: Still destroying... [id=Z1O2JQV3R0LG26_mysql_CNAME, 50s elapsed]
module.network.module.management.aws_vpc_endpoint.ssm: Still destroying... [id=vpce-0eebe69e470d4c103, 50s elapsed]
module.network.module.public_subnet.aws_subnet.public[2]: Destruction complete after 48s
module.network.module.public_subnet.aws_subnet.public[1]: Destruction complete after 49s
module.backend.aws_security_group.alb: Destruction complete after 50s
module.backend.aws_autoscaling_group.backend: Still destroying... [id=app-backend-asg-20181105004601904200000003, 50s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E2KESP33B8DNIU, 20s elapsed]
aws_route53_record.mysql: Still destroying... [id=Z1O2JQV3R0LG26_mysql_CNAME, 1m0s elapsed]
module.network.module.management.aws_vpc_endpoint.ssm: Still destroying... [id=vpce-0eebe69e470d4c103, 1m0s elapsed]
module.backend.aws_autoscaling_group.backend: Still destroying... [id=app-backend-asg-20181105004601904200000003, 1m0s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E2KESP33B8DNIU, 30s elapsed]
aws_route53_record.mysql: Destruction complete after 1m9s
aws_route53_zone.app_dc: Destroying... [id=Z1O2JQV3R0LG26]
module.mysql.aws_db_instance.main_rds_instance: Destroying... [id=app-mysql-0058e036eab3f18e3d97fe5a7b]
aws_route53_zone.app_dc: Destruction complete after 0s
module.network.module.management.aws_vpc_endpoint.ssm: Still destroying... [id=vpce-0eebe69e470d4c103, 1m10s elapsed]
module.backend.aws_autoscaling_group.backend: Still destroying... [id=app-backend-asg-20181105004601904200000003, 1m10s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E2KESP33B8DNIU, 40s elapsed]
module.mysql.aws_db_instance.main_rds_instance: Still destroying... [id=app-mysql-0058e036eab3f18e3d97fe5a7b, 10s elapsed]
module.network.module.management.aws_vpc_endpoint.ssm: Still destroying... [id=vpce-0eebe69e470d4c103, 1m20s elapsed]
module.backend.aws_autoscaling_group.backend: Still destroying... [id=app-backend-asg-20181105004601904200000003, 1m20s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E2KESP33B8DNIU, 50s elapsed]
module.mysql.aws_db_instance.main_rds_instance: Still destroying... [id=app-mysql-0058e036eab3f18e3d97fe5a7b, 20s elapsed]
module.network.module.management.aws_vpc_endpoint.ssm: Still destroying... [id=vpce-0eebe69e470d4c103, 1m30s elapsed]
module.network.module.management.aws_vpc_endpoint.ssm: Destruction complete after 1m31s
module.network.module.management.module.private_subnet.aws_subnet.private[1]: Destroying... [id=subnet-0a019a1fb0d5aba75]
module.network.module.management.module.private_subnet.aws_subnet.private[0]: Destroying... [id=subnet-000c2e9bc0fa1f4ad]
module.network.module.management.module.private_subnet.aws_subnet.private[2]: Destroying... [id=subnet-0485f887e73a69d40]
module.network.module.management.aws_security_group.ssm: Destroying... [id=sg-0258424690602bd25]
module.network.module.management.aws_security_group.ssm: Destruction complete after 1s
module.network.module.management.module.private_subnet.aws_subnet.private[2]: Destruction complete after 1s
module.network.module.management.module.private_subnet.aws_subnet.private[0]: Destruction complete after 1s
module.network.module.management.module.private_subnet.aws_subnet.private[1]: Destruction complete after 1s
module.backend.aws_autoscaling_group.backend: Still destroying... [id=app-backend-asg-20181105004601904200000003, 1m30s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E2KESP33B8DNIU, 1m0s elapsed]
module.mysql.aws_db_instance.main_rds_instance: Still destroying... [id=app-mysql-0058e036eab3f18e3d97fe5a7b, 30s elapsed]
module.backend.aws_autoscaling_group.backend: Still destroying... [id=app-backend-asg-20181105004601904200000003, 1m40s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E2KESP33B8DNIU, 1m10s elapsed]
module.mysql.aws_db_instance.main_rds_instance: Still destroying... [id=app-mysql-0058e036eab3f18e3d97fe5a7b, 40s elapsed]
module.backend.aws_autoscaling_group.backend: Still destroying... [id=app-backend-asg-20181105004601904200000003, 1m50s elapsed]
module.backend.aws_autoscaling_group.backend: Destruction complete after 1m55s
module.backend.aws_security_group_rule.backend-to-mysql: Destroying... [id=sgrule-3211482754]
module.backend.aws_security_group_rule.mysql-from-backend: Destroying... [id=sgrule-3393583181]
module.backend.aws_alb_target_group.backend: Destroying... [id=arn:aws:elasticloadbalancing:us-west-2:473124112471:targetgroup/apptg-20171106080741745400000001/0d3fbbfac44a6a02]
module.network.module.private_subnet.aws_subnet.private[0]: Destroying... [id=subnet-400a3609]
module.network.module.private_subnet.aws_subnet.private[1]: Destroying... [id=subnet-46e7fd21]
module.network.module.private_subnet.aws_subnet.private[2]: Destroying... [id=subnet-2a3d8171]
module.backend.aws_launch_template.backend: Destroying... [id=lt-0d1bd9f990ac86bda]
module.backend.aws_alb_target_group.backend: Destruction complete after 0s
module.backend.aws_launch_template.backend: Destruction complete after 0s
module.base.aws_iam_instance_profile.app: Destroying... [id=app-profile-00f8d1802132e948040476a3b1]
module.backend.aws_security_group_rule.backend-to-mysql: Destruction complete after 0s
module.backend.aws_security_group_rule.mysql-from-backend: Destruction complete after 0s
module.backend.aws_security_group.backend: Destroying... [id=sg-5ffd4125]
module.network.module.private_subnet.aws_subnet.private[0]: Destruction complete after 0s
module.network.module.private_subnet.aws_subnet.private[1]: Destruction complete after 0s
module.network.module.private_subnet.aws_subnet.private[2]: Destruction complete after 0s
module.base.aws_iam_instance_profile.app: Destruction complete after 1s
module.base.aws_iam_role.app: Destroying... [id=app-role-00f8d1802132e948040476a3b0]
module.backend.aws_security_group.backend: Destruction complete after 1s
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E2KESP33B8DNIU, 1m20s elapsed]
module.base.aws_iam_role.app: Destruction complete after 0s
module.mysql.aws_db_instance.main_rds_instance: Still destroying... [id=app-mysql-0058e036eab3f18e3d97fe5a7b, 50s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E2KESP33B8DNIU, 1m30s elapsed]
module.mysql.aws_db_instance.main_rds_instance: Still destroying... [id=app-mysql-0058e036eab3f18e3d97fe5a7b, 1m0s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E2KESP33B8DNIU, 1m40s elapsed]
module.mysql.aws_db_instance.main_rds_instance: Still destroying... [id=app-mysql-0058e036eab3f18e3d97fe5a7b, 1m10s elapsed]
module.base.aws_cloudfront_distribution.cdn: Still destroying... [id=E2KESP33B8DNIU, 1m50s elapsed]
module.mysql.aws_db_instance.main_rds_instance: Still destroying... [id=app-mysql-0058e036eab3f18e3d97fe5a7b, 1m20s elapsed]
module.base.aws_cloudfront_distribution.cdn: Destruction complete after 10m21s
module.mysql.aws_db_instance.main_rds_instance: Still destroying... [id=app-mysql-0058e036eab3f18e3d97fe5a7b, 9m51s elapsed]
module.mysql.aws_db_instance.main_rds_instance: Destruction complete after 9m53s
module.mysql.aws_db_subnet_group.main_db_subnet_group: Destroying... [id=app-mysql-subnet-group-0058e036eab3f18e3d97fe5a7a]
module.mysql.aws_security_group.main_db_access: Destroying... [id=sg-a2381cdf]
module.mysql.aws_db_parameter_group.main_rds_instance: Destroying... [id=app-mysql-custom-params-0058e036eab3f18e3d97fe5a79]
module.mysql.aws_db_subnet_group.main_db_subnet_group: Destruction complete after 0s
module.mysql.module.subnets.aws_subnet.private[1]: Destroying... [id=subnet-70a0dd16]
module.mysql.module.subnets.aws_subnet.private[0]: Destroying... [id=subnet-d5f06d9d]
module.mysql.module.subnets.aws_subnet.private[2]: Destroying... [id=subnet-60d0ec3b]
module.mysql.aws_db_parameter_group.main_rds_instance: Destruction complete after 0s
module.mysql.aws_security_group.main_db_access: Destruction complete after 0s
module.mysql.module.subnets.aws_subnet.private[1]: Destruction complete after 0s
module.mysql.module.subnets.aws_subnet.private[2]: Destruction complete after 0s
module.mysql.module.subnets.aws_subnet.private[0]: Destruction complete after 0s
module.network.module.vpc.aws_vpc.this: Destroying... [id=vpc-08d0186e]
module.network.module.vpc.aws_vpc.this: Destruction complete after 1s

Destroy complete! Resources: 87 destroyed.
Releasing state lock. This may take a few moments...
```
