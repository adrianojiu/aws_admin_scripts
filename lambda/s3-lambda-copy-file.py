import boto3

# Lambda funcion to copy files between folders.

bucket_name = 'logs-bucket' # --> set bucket name.
s3 = boto3.resource('s3')

folder_origim = 'folder1'
file_origin = 'content.json'

folder_dest = 'folder2' 
file_dest = 'content.json'

def lambda_handler(event, context):

    # Copy file from origin folder.
    copy_source = {
        'Bucket': bucket_name,
        'Key': folder_origim+'/'+file_origin
    }

    # Paste file in destination folder.
    s3.meta.client.copy(copy_source, bucket_name, folder_dest+'/'+file_dest)
