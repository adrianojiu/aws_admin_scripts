import boto3

# Boto3 module required, "pip3 install boto3".
# List all object in a bucket recursively

#bucket name
bucket_name = 'logs-bucket'

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

# Get all objects recursively
for obj in bucket.objects.all():
    print(obj.key)

