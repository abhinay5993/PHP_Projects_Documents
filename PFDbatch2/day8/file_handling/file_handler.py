file_obj = open('my_file.txt','w') #open
file_obj.write('') #process
file_obj.close() #close

try:
    file_obj_new = open('my_new_file2.txt','r') #open
except FileNotFoundError:
    print("error handled")
    file_obj_new = open('my_new_file2.txt','w+') #open
    file_obj_new.read() #process
finally:
    file_obj_new.close() #close

print("this code should run")