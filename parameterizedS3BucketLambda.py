import json
import boto3

client = boto3.client('s3')

def lambda_handler(event, context):
    result = client.get_object(Bucket=event["bucket"], Key=event["key"])
    ret_res = json.loads(result['Body'].read().decode('utf-8'))
    return {
        'statusCode': 200,
        'body': ret_res
    }