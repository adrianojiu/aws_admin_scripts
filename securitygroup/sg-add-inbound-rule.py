import boto3
import csv

# Create a rule for each ip in a csv file, you have to add description "," separated.
# Example CSV line: 108.161.240.0/20,your_description

# CSV file have to have one ip per line, only ipv4.
# Boto3 module required, "pip3 install boto3".

## You have to set variables below.
security_group_id = "sg-010101010101010" # Security Group ID you want to add the rule.
port_range_start = 80                    # Port to inbounf rule.
port_range_end = 80                      # Port to inbounf rule.
protocol = "tcp"                         # Rule protocol.
csv_file = "/home/user/ips.csv"

# Set AWS profile name.
aws_local_profile = 'profile-dev'

# Set AWS region name in "region_name=". Make AWS session.
client = boto3.Session(profile_name=aws_local_profile).resource('ec2', region_name='us-east-1')
security_group = client.SecurityGroup(security_group_id)

f = open(csv_file)
csv_f = csv.reader(f)

## !!!! Only uncomment line below if you want remove all rules in teh security group be carefull  !!!!
####security_group.revoke_ingress(IpPermissions=security_group.ip_permissions) # use this to remove all rules from the group

for row in csv_f:
    cidr = row[0] 
    print(cidr)
    
    description = row[1]
    security_group.authorize_ingress(
        DryRun=False,
        IpPermissions=[
            {
                'FromPort': port_range_start,
                'ToPort': port_range_end,
                'IpProtocol': protocol,
                'IpRanges': [
                    {
                        'CidrIp': cidr,
                        'Description': description
                    },
                ]
            }
        ]
    )

'''
# You could use csv file to get port, just adapt code above like this:

for row in csv_f:
    cidr = row[0] #+ "/32"
    description = row [1]   
    port_range_start = row[2]
    port_range_end = row[3]
'''
'''
An error similar to the one below may be related to the CSV file has something wrong.
Recommended to put its contents in a plain text file.

botocore.exceptions.ClientError: An error occurred (InvalidParameterValue) when calling the AuthorizeSecurityG 24 is malformed

'''
