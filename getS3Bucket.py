import json
import boto3

client = boto3.client('s3')

def lambda_handler(event, context):
    result = client.get_object(Bucket='udemy-bucket-eap-sec-8-bucket-1', Key='revisedbucket1data.Json.json')
    ret_res = json.loads(result['Body'].read().decode('utf-8'))
    return {
        'statusCode': 200,
        'body': ret_res
    }
