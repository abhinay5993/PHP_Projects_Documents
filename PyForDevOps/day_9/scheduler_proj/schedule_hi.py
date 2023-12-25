import schedule
import time
import s3_project 
import boto3

s3_obj = boto3.resource('s3')
def say_hi():
    print("hi batch 1 PFD")

schedule.every(5).seconds.do(s3_project.show_buckets,s3_obj)

while True:
    schedule.run_pending()
    time.sleep(1)