import boto3

# Get all security groups information.
# Boto3 module required, "pip3 install boto3".

client = boto3.client('ec2')
response = client.describe_security_groups()

print(response)