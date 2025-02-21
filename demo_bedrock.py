import json
import boto3

client = boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    print(event)
    prompt = event['prompt']
    response = client.invoke_model(
        body=json.dumps({
            "prompt": prompt,
            "max_tokens": 20,
            "temperature": 0.9
        }),
        modelId='cohere.command-text-v14',
        accept='application/json',
        contentType='application/json'
    )
    return_response = json.loads(response['body'].read())
    return {
        'statusCode': 200,
        'body': return_response
    }
