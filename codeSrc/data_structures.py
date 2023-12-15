names = list()
doc_lit=dir(names)
print("\nShow all functions : "+str(doc_lit))

for docIt in doc_lit:
    print("\nList Items status : ",docIt.__doc__)
    print("\nType of Items status : ",type(docIt))

names.append("Soumojit")
names.append("Sudipto")
names.append("Himanshu")
print(names[1])

cloud_platforms = ["aws","gcp","azure"]

for i in cloud_platforms:
    if i == "aws":
       print("\nValue of i : ",i)
       pass
    print("\nValue of i : ",i)