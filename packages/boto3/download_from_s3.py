import os
import boto3

from dotenv import load_dotenv

load_dotenv()
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
REGION_NAME = "ap-northeast-2"


def download_from_s3(bucket, object_name, filename):
    s3_client = boto3.client(
        service_name="s3",
        region_name=REGION_NAME,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    with open(filename, "wb") as f:
        s3_client.download_fileobj(bucket, object_name, f)
    return filename


if __name__ == "__main__":
    filename = "hello_world_from_s3.txt"
    bucket = "taptorestart-test-s3"
    object_name = "hello_world_in_s3.txt"
    download_from_s3(bucket, object_name, filename)
