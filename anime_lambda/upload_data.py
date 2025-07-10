import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')
table = dynamodb.Table('anime')

with open('./anime.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    try:
        table.put_item(Item=item)
    except Exception as e:
        print(f'Failed to upload {item['title']}: {e}')