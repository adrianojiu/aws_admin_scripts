# Example how list instance by AWS cli.
# AWS Cli required.

# Simple list
aws ec2 describe-instances \
    --instance-ids i-1234567890abcdef0

# List filered by type(t2.micro)
aws ec2 describe-instances \
    --filters Name=instance-type,Values=t2.micro

# List by type and AZ
aws ec2 describe-instances \
    --filters Name=instance-type,Values=t2.micro,t3.micro Name=availability-zone,Values=us-east-2c

# List based in tags
aws ec2 describe-instances \
    --filters "Name=tag-key,Values=Owner"

aws ec2 describe-instances \
    --filters "Name=tag-value,Values=my-team"

aws ec2 describe-instances \
    --filters "Name=tag:Owner,Values=my-team"

# Display/output specific values

aws ec2 describe-instances \
    --query 'Reservations[*].Instances[*].{Instance:InstanceId,Subnet:SubnetId,State:State}' \
    --output json

aws ec2 describe-instances \
    --filters Name=instance-type,Values=t2.micro \
    --query Reservations[*].Instances[*].[InstanceId] \
    --output text

# List IP name ans instanceID.
# Values=* gets all instances, you can put instance name if you want.
aws --profile profile-dev --region us-east-1 ec2 describe-instances --filters "Name=tag:Name,Values=*" --output text --query 'Reservations[*].Instances[*].[PrivateIpAddress,InstanceId,Tags[?Key==`Name`].Value]'