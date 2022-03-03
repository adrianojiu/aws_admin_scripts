import boto3

# Boto3 module required, "pip3 install boto3".

# Retrieve the list of existing buckets.
s3 = boto3.client('s3')
response = s3.list_buckets()

header_print = "Name;Creation_date"
print(header_print)

# Output the bucket names
#print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'{bucket["Name"]};' 
          f'{bucket["CreationDate"]}' 
    )
