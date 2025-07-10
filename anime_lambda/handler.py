import boto3
import os
import json
import simplejson as json




dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')
table = dynamodb.Table('anime')


def lambda_handler(event, context):
    path = event.get('path','')
    http_method = event.get('httpMethod', 'GET')

    if http_method != 'GET':
        return {'statusCode': 405, 'body': 'Method not allowed'}
    
    if path == '/anime':
        response = table.scan()
        items = response.get('Items', [])
        return {
            'statusCode': 200,
            'body': json.dumps(items, use_decimal=True)

        }
    elif path.startswith('/anime/'):
        anime_id = path.split('/')[-1]
        response = table.get_item(Key={'id': anime_id})
        item = response.get('Item')
        if item:
            return {
                'statusCode': 200,
                'body': json.dumps(item, use_decimal=True)
            }

        return {
            'statusCode': 400,
            'body': 'Anime not found'
        }
    
    return {'statusCode': 400, 'body': 'Not found'}