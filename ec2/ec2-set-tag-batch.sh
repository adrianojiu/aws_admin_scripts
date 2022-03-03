#!/bin/bash

# Insert in file "instances.txt" instance id in eache line.
# the file have to bem in the same folder as this script.
# In this example this tag is inserted - Key=Backup, Value=true
# AWS Cli required.

aws_region="us-east-1"
input="instances.txt"

while IFS= read -r line
  do
    aws --profile dev-now --region $aws_region ec2 create-tags \
    --resources $line \
    --tags Key=Backup,Value=true
          echo "$line"

done < "$input"