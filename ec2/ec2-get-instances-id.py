import boto3

# Get ID for all instances.
# Boto3 module required, "pip3 install boto3".

aws_region='us-east-1'

# Set AWS profile name variable
aws_local_profile = 'default'

client = boto3.Session(profile_name=aws_local_profile).client('ec2', region_name=aws_region)
response = client.describe_instances()

for i in response['Reservations']:
 print(i['Instances'][0]['InstanceId'])

