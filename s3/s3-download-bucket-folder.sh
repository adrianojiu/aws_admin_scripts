#!/bin/bash

# AWS cli required.
# Copy files and folder wich are into the "s3_source_folder" to a local folder seted up in variable "local_destination_folder".

aws_profile="profile-dev"                                           # Set your aws profile
s3_source_folder="log-static/static/logs/"                          # Set the folder you would like to copy in the bucket.
local_destination_folder="/home/user/logs-copy/01-02-2022-18-23/"   # Set the local computer folder 

aws --profile $aws_profile s3 cp s3://$s3_source_folder $local_destination_folder --recursive
if
 [ -d abs ]
 
