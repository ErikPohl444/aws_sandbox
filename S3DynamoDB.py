import json
import boto3

client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    response = client.get_object(
        Bucket='udemys3bucket123',
        Key='DynamoDB_Samplefile.json'
    )
    json_data = json.loads(response['Body'].read().decode('utf-8'))
    print(json_data)
    print(type(json_data))
    table = dynamodb.Table('RetailSalesv2')
    table.put_item(
        Item=json_data
    )


