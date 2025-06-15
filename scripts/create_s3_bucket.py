import boto3
from botocore.exceptions import ClientError

# craete s3 client
s3 = boto3.client('s3', region_name='ap-northeast-1')

# name bucket
bucket_name = 'minimal-data-pipeline-bocchan-20250615'

try:
    # LocationConstraint is mandatory in Tokyo region
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-1'}
    )

    print(f"Created bucket named {bucket_name}")
    print(response) # confirm response from AWS
except ClientError as e:
    print(f"Failed to create bucket. Reason : {e.response['Error']['Message']}")