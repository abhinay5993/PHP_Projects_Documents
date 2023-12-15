import builtins

cloud_envs = ["aws","azure","gcp"]

try:
    print(cloud_envs[200])
    raise Exception("This is a new exception")
except Exception as e:
    print("exception handled : ",e)
finally:
    print("I will execute anyways")

print("This code should run")

try:
    print(cloud_envs[200])
    a = 10
    b = 0
    c = a/b
except ZeroDivisionError as e:
    print("1",e)
except IndexError as e:
    print("2",e)

lst_dat=dir(builtins)
print("\nNumber of builtins : ",len(lst_dat))

# for bils in lst_dat:
#     print("\nItems of builtins : ",bils.__doc__)
