import boto3

import datetime
import random

s3 = boto3.resource('s3')
bucket = "sthreebucket-hogehoge"

def index(event, context):
    dt = datetime.datetime.now()
    text = ""
    for i in range(10):
        num = str(random.randint(0, 100))
        text += num + " "

    key = "{0:%Y-%m-%d-%H-%M-%S}.txt".format(dt)

    obj = s3.Object(bucket, key)
    obj.put(Body=text.encode())

    return {
        "statusCode": 200,
        "body": text
    }