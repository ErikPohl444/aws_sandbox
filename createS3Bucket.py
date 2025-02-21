import json
import boto3
client = boto3.client('s3')

def lambda_handler(event, context):
    create_s3bucket = client.create_bucket(
        Bucket='udemydemoeap010725',
        CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'
        }
    )
    print(create_s3bucket)
