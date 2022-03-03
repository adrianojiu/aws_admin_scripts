import boto3

# Get tags for all EBS volumes.
# Boto3 module required, "pip3 install boto3".

# Set AWS profile name variable.
aws_local_profile = 'profile-dev'

# Set AWS region name in "region_name=". Make AWS session.
client = boto3.Session(profile_name=aws_local_profile).client('ec2', region_name='sa-east-1')
response = client.describe_volumes() # --> Get response for all Volumes

# Get all volumes and display, volume ID and tags.
for i in response['Volumes']:
 try:
     i['Tags'][0]  # Validation to avoid error if there is no tags.
 except:
    print(i['VolumeId'] , " -- ","Not have tags")  # if no tags found, diplay this.
 else:
    print(i['VolumeId'] , " -- ", i['Tags']) # If tags found display tags.
