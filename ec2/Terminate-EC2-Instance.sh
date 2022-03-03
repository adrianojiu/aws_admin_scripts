#!/bin/bash

# Remove listed instances.
# AWS Cli required.

aws_profile="profile-dev"
aws_region="us-east-1"

# Inset instance id in teh end as you can see.
aws --profile ec2 terminate-instances --instance-ids "i-0ce7c4b44409326d2" "i-0df695d498149fa34"
