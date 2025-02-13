import boto3
import os

s3 = boto3.client('s3')

def upload_to_s3(file_path, bucket_name):
    file_name = os.path.basename(file_path)
    s3.upload_file(file_path, bucket_name, "backups/" + file_name)
    print(f"✅ Backup uploaded to S3: {file_name}")
