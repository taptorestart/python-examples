import os
import logging
import boto3
from botocore.exceptions import ClientError

from dotenv import load_dotenv

load_dotenv()
AWS_ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('SECRET_ACCESS_KEY')
REGION_NAME = 'ap-northeast-2'


def upload_file_to_s3(bucket, filename, object_name):
    s3_client = boto3.client(
        service_name='s3', region_name=REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    try:
        response = s3_client.upload_file(filename, bucket, object_name)
    except ClientError as e:
        logging.error(e)
    return object_name


if __name__ == '__main__':
    bucket = 'taptorestart-test-s3'
    filename = 'hello_world.txt'
    object_name = 'hello_world_in_s3.txt'
    uploaded_file = upload_file_to_s3(bucket=bucket, filename=filename, object_name=object_name)
