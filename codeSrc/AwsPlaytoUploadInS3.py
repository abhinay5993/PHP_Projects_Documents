import boto3 as bt3
import AwsS3ManagerUtils as awsUtils

s3Obj=bt3.resource('s3')
print("\nShow all modules from boto3 object : \n",dir(s3Obj))

getBucketName=awsUtils.showAllS3Bukets(s3Obj)
strFilePath="codeSrc/myExecLogger.log"
strFileKeyName="local_exec_logData.log"
# "aws_s3_uploads/{}".format(strFileKeyName)
#awsUtils.uploadFileToS3Buket(s3Obj,getBucketName,strFilePath,"aws_s3_uploads/"+strFileKeyName)

awsUtils.showListOfAllS3BucketFiles(s3Obj,getBucketName)