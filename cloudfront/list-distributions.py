import boto3

# Set profile variable.
# List CloudFront distribution and some attributes.
# Boto3 module required, "pip3 install boto3".

aws_local_profile = 'profile-dev'

# Create CloudFront client
session = boto3.Session(profile_name=aws_local_profile)
cf = session.client('cloudfront')

# List distributions
print("\nCloudFront Distributions:\n")
distributions=cf.list_distributions()

if distributions['DistributionList']['Quantity'] > 0:
  for distribution in distributions['DistributionList']['Items']:
    print("---")
    print("Domain: " + distribution['DomainName'])
    alias_items_str =  str(distribution['Aliases']['Items'])
    print("Alias:",  alias_items_str.replace("['","").replace("']","") )
    for oid in distribution['Origins']['Items']:
        print("Origins Id: ",  oid['Id'])
        print("  Domain Name: ",  oid['DomainName'])
        print("  Origin path: ",  oid['OriginPath'])

        #http origin
        try:
            http_null = oid['CustomOriginConfig']['HTTPPort']
        except:
            print("  Port http: None")
        else:
            print("  Port http:",  oid['CustomOriginConfig']['HTTPPort'])

        #https origin
        try:
            https_null = oid['CustomOriginConfig']['HTTPSPort']
        except:
            print("  Port https: None")
        else:
            print("  Port https:",  oid['CustomOriginConfig']['HTTPSPort'])

        #S3 Origin
        try:
            s3_origin_null = oid['S3OriginConfig']['OriginAccessIdentity']
        except:
            print("  S3 origin: None")
        else:
            print("  S3 origin:",  oid['S3OriginConfig']['OriginAccessIdentity'])

    print("Distribution Id: " + distribution['Id'])
    print("Default Cache Behavior :" + distribution['DefaultCacheBehavior']['TargetOriginId'])

print("Certificate Source: " + distribution['ViewerCertificate']['CertificateSource'])
if (distribution['ViewerCertificate']['CertificateSource'] == "acm"):
    print("Certificate: " + distribution['ViewerCertificate']['Certificate'])
    print("")
    print("----------------------------")
    print("")
else:    
  print("Error - No CloudFront Distributions Detected.")
