import json
import boto3

client = boto3.client('ec2', region_name='us-west-1')

def lambda_handler(event, context):
    resule = client.start_instances(
        InstanceIds=[
        'i-0b31142ad55475081'
    ]
)