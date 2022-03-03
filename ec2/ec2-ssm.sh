#!/bin/bash

# AWS Cli required.
# Connect to as instance using AWS ssm shell.

    while [ -z $aws_instance  ];
    do
        echo "Enter the instance ID : "
        read aws_instance
    done
    
    while [ -z $aws_profile  ];
    do
        echo "Enter AWS profile name : "
        read aws_profile
    done
    while [ -z $aws_region  ];
    do
        echo "Enter AWS region name : "
        read aws_region
    done

aws --profile $aws_profile --region $aws_region ssm start-session --target $aws_instance
