envVar=input("Enter the Cloud Platform Name : ")
if envVar=='aws' or envVar=='AWS':
   print("This is 'Amazon Web Services' ")
elif envVar=='azure' or envVar=='AZURE':
   print("This is 'Microsofts Azure Cloud Services' ")
elif envVar=='gcp' or envVar=='GCP':
   print("This is 'Googles Cloud Services' ")
else :
   print("This is 'Others Cloud Services' ")