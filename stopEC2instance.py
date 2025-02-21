import json
import boto3

client = boto3.client('ec2', region_name='us-west-1')

def lambda_handler(event, context):
    result = client.stop_instances(
        InstanceIds=[
        'i-0ee3356f39e6bd613'
    ]
)
