from handler import lambda_handler

event = {
    'path': '/anime/aot-01',
    'httpMethod': 'GET'
}

response = lambda_handler(event, None)
print(response['statusCode'])
print(response['body'])


