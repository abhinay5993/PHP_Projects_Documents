def show_buckets(s3_obj):
    for bucket in s3_obj.buckets.all():
        print(bucket.name)

def upload_file(s3_obj,bucket_name,file_path,key_name):
    file_data = open(file_path,'rb') #open
    s3_obj.Bucket(bucket_name).put_object(Key=key_name,Body=file_data) #processed
    file_data.close() #close
    print("file uploaded sucessfully")

def list_files(s3_obj,bucket_name):
    print(f"The files in {bucket_name} are:")
    for object in s3_obj.Bucket(bucket_name).objects.all():
        print(object.key)

def create_bucket(s3_obj,bucket_name):
    s3_obj.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={
    'LocationConstraint': 'eu-west-1'})
    print(f"bucket {bucket_name} created successfully")