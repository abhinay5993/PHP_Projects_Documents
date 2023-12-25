import sys
sys.path.append(".")
# we can also use sys.path.insert(1,'absolute / relative path of root module/folder where .py files present')
from PFDbatch2.day8 import linear_search_fun as lst_fl

envVar=input("Enter the Cloud Platform Name : ")
if envVar=='aws' or envVar=='AWS':
   print("This is 'Amazon Web Services' ")
elif envVar=='azure' or envVar=='AZURE':
   print("This is 'Microsofts Azure Cloud Services' ")
elif envVar=='gcp' or envVar=='GCP':
   print("This is 'Googles Cloud Services' ")
else :
   print("This is 'Others Cloud Services' ")

lst_env=['kkk','qa-aut','maven','app']
keyDat='maven'
res=lst_fl.linear_search(lst_env,keyDat)
print(res)