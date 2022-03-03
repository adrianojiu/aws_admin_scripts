#!/bin/bash

# Launch EC2 instance setting up a boot strap.
# It use AWS default local profile, if you need specify a profile use "--profile".
# AWS Cli required.
# Set variables as you need.
# The file "boot-script.txt" which has boot strap commands have to be in the same directory as command will be running.
# Execution ./Create-EC2-Instance-boot-strap.sh

ami="ami-0742b4e673072066f"
instance_count=2 
instance_type="t2.micro"
key_name="GeneralKeyAccess"
security_group="app_sg"
region_name="us-east-1"
user_data="file://boot-script.txt"

aws ec2 run-instances --image-id $ami --count $instance_count --instance-type $instance_type --key-name $key_name --security-groups $security_group --region $region_name --user-data $user_data
