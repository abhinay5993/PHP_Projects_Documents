import boto3
from s3_project import upload_to_s3
s3_obj = boto3.resource('s3')


upload_to_s3(s3_obj,'python-for-devops-batch-1','secret.txt','my_secret_file.txt')