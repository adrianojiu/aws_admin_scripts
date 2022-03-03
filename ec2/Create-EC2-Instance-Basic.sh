#!/bin/bash

# Launch EC2 instance simple mode.
# It use AWS default local profile, if you need specify a profile use "--profile".
# AWS Cli required.
# Set variables as you need.
# Execution ./Create-EC2-Instance-Basic.sh

ami="ami-0742b4e673072066f"
instance_count=2 
instance_type="t2.micro"
key_name="GeneralKeyAccess"
security_group="app_sg"
region_name="us-east-1"

aws ec2 run-instances --image-id $ami --count $instance_count --instance-type $instance_type --key-name $key_name --security-groups $security_group --region $region_name
