import boto3

# Get instances attributes and print with ";" separeted.
# Boto3 module required, "pip3 install boto3".


aws_region='us-east-1'                                  # Set AWS region.
aws_local_profile = 'profile-dev'                       # Set AWS profile name(same as OS) variable.
session = boto3.Session(profile_name=aws_local_profile) # Set AWS profile profile variable.
ec2 = session.client('ec2', region_name=aws_region)

response = ec2.describe_instances()

header_print = "ID;Name;Type;State;Access key;Monitoring;AZ;Priv IP;Subnet;Pub IP;VPC;Sec group ID;Sec group name;EBS dev name;EBS vol ID;EBS del term"
print(header_print)

for i in response['Reservations']:
    
    # Get condition for name tag value, avoid error for null return.
    base_param = i['Instances'][0]['Tags'][0]['Value']
    
    if not base_param:
      inst_name = 'None'
    else:
      
      inst_name = i['Instances'][0]['Tags'][0]['Value']

    print(
      i['Instances'][0]['InstanceId'], ';'\
    , inst_name, ';'\
    , i['Instances'][0]['InstanceType'], ';'\
    , i['Instances'][0]['State']['Name'], ';'\
    , i['Instances'][0]['KeyName'], ';'\
    , i['Instances'][0]['Monitoring']['State'], ';'\
    , i['Instances'][0]['Placement']['AvailabilityZone'], ';'\
    , i['Instances'][0]['PrivateIpAddress'], ';'\
    , i['Instances'][0]['SubnetId'], ';'\
    , i['Instances'][0]['VpcId'], ';'\
    , i['Instances'][0]['SecurityGroups'][0]['GroupId'], ';'\
    , i['Instances'][0]['SecurityGroups'][0]['GroupName'], ';'\
    , i['Instances'][0]['BlockDeviceMappings'][0]['DeviceName'], ';'\
    , i['Instances'][0]['BlockDeviceMappings'][0]['Ebs']['VolumeId'], ';'\
    , i['Instances'][0]['BlockDeviceMappings'][0]['Ebs']['DeleteOnTermination'],
    
      )
