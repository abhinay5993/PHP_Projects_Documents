"""
This script checks if 
My Cloud Environment is Amongst folowing
- AWS
- Azure
- GCP

"""

cloud_env = input("Enter Cloud Environment")
service = input("Enter the service")
print(dir(cloud_env))
if cloud_env.lower() == "aws":
    print("you are in AWS")
    if service == "ec2":
        print("you are in AWS EC2")
    else:
        print("you are in AWS but in other service")

elif cloud_env.lower() == "azure":
    print("you are in Azure")
elif cloud_env.lower() == "gcp":
    print("you are in GCP")
else:
    print("you are not using any of the cloud services")
