import boto3
import botocore

# Boto3 module required, "pip3 install boto3".
# Copy files from a bucket based on if statement filter.

aws_local_profile = 'profile-dev'                       # Set AWS profile name(same as OS) variable.
bucket_name = 'log-static'                              # Set bucket name variable.
session = boto3.Session(profile_name=aws_local_profile) # Set AWS profile profile variable.
s3 = session.resource('s3')                             # Set aws resource in variable.
bucket = s3.Bucket(bucket_name)                         # Set used bucket.

def download_file(key_file):
      try:
            key_file_split = key_file.split("/") # Split key name by /
            s3.Bucket(bucket_name).download_file(key_file, "/tmp/"+key_file_split[-2] + "--" +key_file_split[-1]) # File is downloaded and saved by name, because split take [-2] folder name is add in file name,because split take [-1] file name is taken,  files with the same name will be replaced by the last one.
      except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                        print("The object does not exist.")
            else:
                  raise

# Get all objects recursively.
# Download based on streing filter below.
for obj in bucket.objects.all():
    
    obj_name = obj.key
    
    # Find string in " ".
    if "http-log" in obj_name:
        print(obj_name)
        key_file = obj_name
        download_file(key_file)
    
    # Find second string in " ".
    elif "http-access" in obj_name:
        print(obj_name)
        key_file = obj_name
        download_file(key_file)

    # Add more elif statement to download more files.
