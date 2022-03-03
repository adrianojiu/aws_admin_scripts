import boto3
import json

# Boto3 module required, "pip3 install boto3".
# Get inbound rules.
# Execution scrip example:
# python sg-describe-ip-permissions-inbound-rules.py | jq '.'

aws_local_profile = 'profile-dev'   # Set AWS profile name variable.
aws_region='sa-east-1'              # Set AWS region.
sg_id = 'sg-010101010101010'        # Set security group id.

# Set AWS region name in "region_name=". Make AWS session.
client = boto3.Session(profile_name=aws_local_profile).client('ec2', region_name=aws_region)
response = client.describe_security_groups()

for i in response['SecurityGroups']:
    if i['GroupId'] == sg_id:
        print(
        json.dumps(i['IpPermissions'])
        )
