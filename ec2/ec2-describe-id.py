import boto3

# Boto3 module required, "pip3 install boto3".
# Get attributs for instance list invariable "ec2idv".
# AWS default local profile its used.

ec2idv = 'i-09da4472716f23f5c','i-048266c46c6b69dc8' # <--- Put EC2 instance ID, enter one id or more than one comma separated.

for instancei in ec2idv:
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(InstanceIds=[instancei])
    print(response)