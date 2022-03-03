import boto3

# Boto3 module required, "pip3 install boto3".
# List all object in a bucket base on word patterns in if statement.

aws_local_profile = 'profile-dev'                       # Set AWS profile name(same as OS) variable.
bucket_name = 'logs-static'                             # Set bucket name variable.
session = boto3.Session(profile_name=aws_local_profile) # Set AWS profile profile variable.
s3 = session.resource('s3')                             # Set aws resource in variable.
bucket = s3.Bucket(bucket_name)                         # Set used bucket.

# Get all objects recursively.
for obj in bucket.objects.all():
    
    obj_name = obj.key
    
    # Find 1th string in " ".
    if "logs-fe/img/app-api" in obj_name:
        print(obj_name)
    
    # Find 2th string in " ".
    elif "logs-fe/img/web-api" in obj_name:
        print(obj_name)
   
   
    '''
    # Find string in " ", split "/" and get the last part.
    elif "hbo" in obj_name:
        obj_name_split = obj_name.split("/")
        print(obj_name_split[-1])
    
    '''
 
    # To find more strings, copy elif code above and set the tring you desire.
