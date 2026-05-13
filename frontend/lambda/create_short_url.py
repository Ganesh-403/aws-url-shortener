import boto3
import json
import random
import string
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):

    body = json.loads(event.get('body', '{}'))
    original_url = body.get('url')

    if not original_url:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'URL required'})
        }

    # Generate random shortcode
    code = ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=6
        )
    )

    # Store in DynamoDB
    table.put_item(
        Item={
            'shortcode': code,
            'original_url': original_url,
            'clicks': 0
        }
    )

    base_url = os.environ.get('BASE_URL')

    return {
        'statusCode': 200,
        'body': json.dumps({
            'short_url': f'{base_url}/{code}',
            'code': code
        })
    }