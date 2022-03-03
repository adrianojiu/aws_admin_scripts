import boto3
import datetime

# Boto3 module required, "pip3 install boto3".
# List all object in a bucket, and delete files if before a date specified below.

# Set AWS profile name variable
aws_local_profile = 'profile-dev'

# Set bucket name variable
bucket_name = 'log-report'

session = boto3.Session(profile_name=aws_local_profile)
s3 = session.resource('s3')
bucket = s3.Bucket(bucket_name)

for file in bucket.objects.all():
    
    # Get date time of file in bucket
    f_last_modified = (file.last_modified).replace(tzinfo = None)
    
    # Get file if less than date ahead     YYYY  M  D  H  M  S (files before that date going to be deleted)
    if f_last_modified < datetime.datetime(2021, 5, 1, 0, 0, 0, tzinfo = None):
        print(f_last_modified, file)
        #file.delete()      ### !!!!! To delete files remove comment in the line begining. !!!!!
