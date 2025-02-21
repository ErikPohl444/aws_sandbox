import json
import boto3

client = boto3.client('s3')


def lambda_handler(event, context):
    result = client.list_buckets()
    print(result)
    print("BUCKETS")
    for bucket in result['Buckets']:
        print(bucket['Name'], bucket['CreationDate'])
