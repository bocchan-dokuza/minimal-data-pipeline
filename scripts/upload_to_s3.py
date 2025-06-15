import boto3 
from botocore.exceptions import ClientError

# create S3 client
s3 = boto3.client('s3')

# information for upload file
local_file_path = 'data\superstore_cleaned.csv' # name of local file
bucket_name = 'minimal-data-pipeline-bocchan-20250615' # name of bucket
s3_key = 'superstore/superstore_cleaned' # path in s3

try:
    # Upload file
    s3.upload_file(local_file_path, bucket_name, s3_key)
    print('Complete')
except ClientError as e:
    print(f"Failed to upload:{e.response['Error']['Message']}")