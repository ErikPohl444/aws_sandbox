import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    result = client.put_item(
        TableName='RetailSales',
        Item={
            'CustomerID': {
                'S': '001'
            },
            'Product': {
                'S': 'Mangoes'
            },
            'Quantity': {
                'N': '100'
            },
            'Address': {
                'S': '101 Prestige Tranquility'
            }
        }
    )
    print(result)