"""
- open() (done)
- do operations on file (done)
- close() (done)
"""

file_obj = open("credentials.txt",'r')
creds = file_obj.readlines()
file_obj.close()


for cred in creds:
    print(cred.split("=")[1])
