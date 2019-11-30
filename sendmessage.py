import boto3
import random
import json

sqs = boto3.resource('sqs')
queueName = "hogehoge-queue"


def index(event, context):
    queue = sqs.get_queue_by_name(QueueName=queueName)  # キューを取得

    message = ""  # 送信するメッセージ

    for i in range(10):
        num = str(random.randint(0, 100))
        message += num + " "

    print(message)

    queue.send_message(MessageBody=json.dumps({ "message": message })) # メッセージの送信

    return message
