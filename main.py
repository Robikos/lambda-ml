import json

def lambda_handler(event, context):
    param = event['parameter']
    return {
        'statusCode': 200,
        'body': json.dumps({'request parameter': param})
    }
