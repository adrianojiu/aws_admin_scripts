from itertools import count
from urllib.request import urlopen
import json
import boto3

# Boto3 module required, "pip3 install boto3".

'''
This script creates rules in a security group which contains subnet/ips for CloudFront Global and Edge locations.
Change variables as you need, the most important to be changed are the variables in lines just below.
If a rule exist the creation of that will be skipped.
By default you can create up to 60 rules in a security group, if you need more than 60 rules in a security group request to AWS to increase a number of rules tha you can create in a security groups.

'''
security_group_id = "sg-01010101010101010"  # Set Security Group ID
port_range_start = 80                       # Set port range to be opened.
port_range_end = 80                         # Set port range to be opened.
protocol = "tcp"                            # Set rule protocol.
aws_local_profile = 'profile-dev'           # Set AWS profile name variable.
aws_region = 'us-east-1'                    # Ser AWS region
url_cf_ip = "https://d7uri8nf7uskq.cloudfront.net/tools/list-cloudfront-ips"   # Cloudfront ips url api.
description_global = "CloudfrontGlobalIPandNetwork"                            # Rules description.
description_edge = "CloudfrontEdgeIPandNetwork"                                # Rules description.

# Set AWS region name in "region_name=". Make AWS session.
client = boto3.Session(profile_name=aws_local_profile).resource('ec2', region_name=aws_region)
security_group = client.SecurityGroup(security_group_id)

response = urlopen(url_cf_ip)                                           # Getting IPs in AWS api.
data_json = json.loads(response.read())                                 # Storing the JSON response from url in data.

# Add rules cloudfront global.
data_json_ip_glo = data_json['CLOUDFRONT_GLOBAL_IP_LIST']               # Getting cloudfront global ips.
for ip_i_glo in data_json_ip_glo: 
    
    try:
        # Creating rule for each IP in the list.
        security_group.authorize_ingress(
            DryRun=False,
            IpPermissions=[
                {
                    'FromPort': port_range_start,
                    'ToPort': port_range_end,
                    'IpProtocol': protocol,
                    'IpRanges': [
                        {
                            'CidrIp': ip_i_glo,
                            'Description': description_global
                        },
                    ]
                }
            ]
        )
    except Exception as error:
        error_strig = str(error)
        print(error_strig)


# Create global IP rules.
data_json_ip_edg = data_json['CLOUDFRONT_REGIONAL_EDGE_IP_LIST']        # Getting cloudfront edge ips.
for ip_i_edg in data_json_ip_edg: 
    
    try:
        # Creating rule for each IP in the list.
        security_group.authorize_ingress(
            DryRun=False,
            IpPermissions=[
                {
                    'FromPort': port_range_start,
                    'ToPort': port_range_end,
                    'IpProtocol': protocol,
                    'IpRanges': [
                        {
                            'CidrIp': ip_i_edg,
                            'Description': description_edge
                        },
                    ]
                }
            ]
        )
    except Exception as error:
        error_strig = str(error)
        print(error_strig)


# Getting count of itens in variable/key
#print(len(data_json_ip_glo))
