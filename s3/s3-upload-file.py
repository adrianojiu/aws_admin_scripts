import boto3

# Boto3 module required, "pip3 install boto3".
# Upload a local file to s3 bucket.

bucket_name = 'bucketdev'

file_path = '/mnt/c/Temp/pasta3/config.json'

s3 = boto3.resource('s3')
s3.meta.client.upload_file(file_path, bucket_name, 'pasta3/config.json' )