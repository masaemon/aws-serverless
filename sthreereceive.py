import boto3

s3 = boto3.client('s3')

def index(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"] #バケットの名前
    key = event["Records"][0]["s3"]["object"]["key"] #保存したファイルの名前
    response = s3.get_object(Bucket=bucket, Key=key) #バケットの中にあるオブジェクトの取得
    body = response['Body'].read().decode("utf-8") #ファイルの中の情報を取得してutf-8にデコードする
    print(body)
    return body