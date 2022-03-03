import boto3

# Boto3 module required, "pip3 install boto3".
# Get attributs for all EC2 instances.

aws_region = 'us-east-1'                                # Set AWS rerion.
aws_local_profile = 'dev-now'                           # Set AWS profile name(same as OS) variable.
session = boto3.Session(profile_name=aws_local_profile) # Set AWS profile profile variable.

ec2 = session.client('ec2', region_name=aws_region)
response = ec2.describe_instances()

#Get all instances information json format
print(response)