import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):

    code = event['pathParameters']['code']

    response = table.get_item(
        Key={'shortcode': code}
    )

    item = response.get('Item')

    if not item:
        return {
            'statusCode': 404,
            'body': 'URL not found'
        }

    # Increment clicks
    table.update_item(
        Key={'shortcode': code},
        UpdateExpression='SET clicks = clicks + :inc',
        ExpressionAttributeValues={
            ':inc': 1
        }
    )

    return {
        'statusCode': 301,
        'headers': {
            'Location': item['original_url']
        }
    }