import json

def index(event, context):
    body = json.loads(event["Records"][0]["body"])
    message = body["message"]
    print(message)
    return message