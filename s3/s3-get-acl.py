import boto3

# Get acl for all buckets.
# Boto3 module required, "pip3 install boto3".

# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        print("Bucket Name:", bucket_name)
        bucket_acl = s3.get_bucket_acl(Bucket=bucket_name)
        
        for grantee in bucket_acl['Grants']:
                print(str(grantee).replace("{","").replace("}",""))
