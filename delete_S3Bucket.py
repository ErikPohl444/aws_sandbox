import json
import boto3

client = boto3.client('s3')


def lambda_handler(event, context):
    result = client.delete_bucket(Bucket='udemydemoeap010625')
    print(result)