import json
import boto3

client = boto3.client('ec2', region_name='us-west-1')

def lambda_handler(event, context):
    result = client.run_instances(
        ImageId='ami-0aa117785d1c1bfe5',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1
    )
    print(result['Instances'][0]['InstanceId'])

