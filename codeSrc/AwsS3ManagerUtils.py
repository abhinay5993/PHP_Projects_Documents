def showAllS3Bukets(s3Obj):
    getBuketName=""
    for bks in s3Obj.buckets.all():
        getBuketName=bks.name
        print("\nList of buckets : ",bks.name)
    return getBuketName


def uploadFileToS3Buket(s3Obj,bucketName,filePath,keyName):
    fileData=open(filePath,"rb")
    s3Obj.Bucket(bucketName).put_object(Key=keyName,Body=fileData)
    fileData.close()
    print("\nFile uploaded successfully!!..")


def showListOfAllS3BucketFiles(s3Obj,bucketName):
    print(f"\nThe files in s3 bucket '{bucketName}' is : ")
    for objItems in s3Obj.Bucket(bucketName).objects.all():
        print("\nList of Items : ",objItems.key)


#s3 bucket creation using boto
def createBucketByUserDefName(s3Obj,bucketName):
    s3Obj.create_bucket(
                        Bucket=bucketName,CreateBucketConfiguration={ 'LocationConstraint': 'us-east-2' }
                        )
    print(f"New bucket crated with '{bucketName}' this name.")


#passing a single list/Tuple with *args
def decorateConvertToUpper(passedFunc):
    def wrapper(*args):
        return passedFunc(*args).upper()
    return wrapper

#passing a single dictionary with **args
def decorateRemoveCommaAndAddSpaces(passedFunc):
    def wrapper(**args):
        return passedFunc().replace(","," ")
    return wrapper

