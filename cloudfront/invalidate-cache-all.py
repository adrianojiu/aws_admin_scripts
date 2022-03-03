import boto3
import time
import sys

# Create an invalidation cache for all objects in distribution ID below.
# Set distribution ID and profile name.
# Cache invalidation for all paths in distribution.
# Boto3 module required, "pip3 install boto3".

DISTRIBUTION_ID = 'EYJJJJJJJJJJ'                         # Type your cloudfront distibution ID.
aws_local_profile = 'profile-dev'                        # Set local AWS profile.

session = boto3.Session(profile_name=aws_local_profile)  # Create CloudFront client.
cf = session.client('cloudfront')                        # Create CloudFront client.


def create_invalidation():
    res = cf.create_invalidation(
        DistributionId=DISTRIBUTION_ID,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [
                    '/*'
                ]
            },
            'CallerReference': str(time.time()).replace(".", "")
        }
    )
    invalidation_id = res['Invalidation']['Id']
    return invalidation_id


def get_invalidation_status(inval_id):
    res = cf.get_invalidation(
        DistributionId=DISTRIBUTION_ID,
        Id=inval_id
    )
    return res['Invalidation']['Status']


def run():
    the_id = create_invalidation()
    count = 0
    while True:
        status = get_invalidation_status(the_id)
        if status == 'Completed':
            print("Completed, id: {}".format(the_id))
            break
        elif count < 10:
            count += 1
            time.sleep(30)
        else:
            print("Timeout, please check CDN")
            sys.exit(1)


if __name__ == '__main__':
    run()
