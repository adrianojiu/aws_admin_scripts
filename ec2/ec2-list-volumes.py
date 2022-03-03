import boto3
from operator import itemgetter

# Get instance volumes and print volume ID, size, state and tags.
# Boto3 module required, "pip3 install boto3".

aws_region = 'sa-east-1'                                # Set AWS region.
aws_local_profile = 'prd-now'                           # Set AWS profile name(same as OS) variable.
session = boto3.Session(profile_name=aws_local_profile) # Create AWS logon.
ec2_resource = session.resource('ec2', region_name=aws_region) # Create AWS logon.

ec2 = session.client('ec2', region_name=aws_region)

for volume in ec2_resource.volumes.all():
    volume_att = volume.attachments     # Get attachments attribute, which has instance ID "volume.attachments" returns a python list.
    volume_att_InstanceId = list(map(itemgetter('InstanceId'),volume_att))      # Get only instanceID in attachments list.
    volume_att_InstanceId_to_string = str(volume_att_InstanceId)        # Convert to string.
    volume_att_InstanceId_clean1 = volume_att_InstanceId_to_string.replace("['", "")        # Clean variable to display more fancy.
    volume_att_InstanceId_clean2 = volume_att_InstanceId_clean1.replace("']", "")           # Clean variable to display more fancy.
    
    if '[]' in volume_att_InstanceId_clean2:  # If there is no instance id, set '0000000000000000000' to the variabe to display more fancy.
        volume_att_InstanceId_clean2 = '0000000000000000000'

    print(f'Instance = {volume_att_InstanceId_clean2} ; VolumeID = {volume.id} ; Size = {volume.size} GiB ; State = {volume.state} ; Tags = {volume.tags}')
