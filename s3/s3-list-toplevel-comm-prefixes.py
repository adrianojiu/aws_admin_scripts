import boto3

# Boto3 module required, "pip3 install boto3".
# List top level common prefrix in a bucket

#Bucket name
bucket_name = 'logs-bucket'

client = boto3.client('s3')
paginator = client.get_paginator('list_objects')
result = paginator.paginate(Bucket=bucket_name, Delimiter='/')
for prefix in result.search('CommonPrefixes'):
    print(prefix.get('Prefix'))