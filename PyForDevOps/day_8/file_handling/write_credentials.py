try:
    file_obj = open("credentials_new.txt",'r')
    file_obj.read()
except:
    file_obj = open("credentials_new.txt",'w')
    file_obj.write("username=admin\npassword=admin")
finally:       
    file_obj.close()