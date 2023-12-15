import boto3
from aws_wrapper import show_buckets,upload_file,list_files,create_bucket

s3_obj = boto3.resource('s3')
file_path='my_test_upload_file.txt'
show_buckets(s3_obj)
#upload_file(s3_obj,'pfd-batch-2-shubham',file_path,'my_test_upload_file.txt')
list_files(s3_obj,'pfd-batch-2-shubham')
create_bucket(s3_obj,'pfd-batch-2-shubham-new')