#!/usr/bin/env bash

##############
# Install deps
##############
apt-get update && apt-get upgrade -y
## aws
apt-get install -y python-pip jq
pip install --upgrade awscli

#############
# Bind to EIP
#############

pip install --upgrade aws-ec2-assign-elastic-ip
INSTANCE_ID=$(wget -q -O - http://169.254.169.254/latest/meta-data/instance-id)
REGION=$(curl -s http://169.254.169.254/latest/dynamic/instance-identity/document | grep region | awk -F\" '{print $4}')
EIP=$(aws ec2 describe-tags --filters "Name=resource-id,Values=${INSTANCE_ID}" "Name=key,Values=EIP" --output text --region "${REGION}" --query 'Tags[*].Value')
aws-ec2-assign-elastic-ip --valid-ips "$EIP"

#########################
# motd with all ASG hosts
#########################

cat <<"INSTANCES_SCRIPT" >/etc/update-motd.d/60-update-list-of-running-instances
#!/bin/bash

REGION=$(curl -s http://169.254.169.254/latest/dynamic/instance-identity/document | grep region | awk -F\" '{print $4}')
echo ""
echo ""
echo "Current instances grouped by AutoScaling Groups:"
# get all ASG
for asg in $(aws autoscaling describe-auto-scaling-groups --output text --region "${REGION}" --query 'AutoScalingGroups[*].AutoScalingGroupName'); do
  echo ""
  echo "# $asg"
  # get all instances in ASG
  for ip in $(aws ec2 describe-instances --filters "Name=tag-key,Values='aws:autoscaling:groupName'" "Name=tag-value,Values='$asg'" --output text --region "${REGION}" --query 'Reservations[*].Instances[*].[PrivateIpAddress]'); do
    echo "$ip"
  done
  echo ""
  echo "========================================================================="
done
INSTANCES_SCRIPT

chmod +x /etc/update-motd.d/60-update-list-of-running-instances
