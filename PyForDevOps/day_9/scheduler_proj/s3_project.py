
def show_buckets(s3_obj):
    for bucket in s3_obj.buckets.all():
        print(bucket.name)

def upload_to_s3(s3_obj,bucket_name,file_name,file_path):
    data = open(file_path,'rb')
    s3_obj.Bucket(bucket_name).put_object(Key=file_name,Body=data)
    data.close()
    print("File uploaded successfully")

