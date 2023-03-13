import os
import boto3

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
   message = "Hello from AWS Lambda!"
   encoded_string = message.encode("utf-8")
   file_name = "hello.txt"
   s3_path = "test/" + file_name
   dynamodb.Table(os.environ['DYNAMODB_TABLE_NAME']).put_item(Item={'ID': '12345','content':message})
   s3.Bucket(os.environ['S3_BUCKET_NAME']).put_object(Key=s3_path, Body=encoded_string)
   response = {
      'statusCode': 200,
      'body': 'success!',
      'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
      },
   }
   return response