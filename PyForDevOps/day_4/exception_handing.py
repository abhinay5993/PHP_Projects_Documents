import builtins

cloud_envs = ["aws","azure","gcp"]

try:
    print(cloud_envs[200])
    raise Exception("This is a new exception")
except:
    print("exception handled")
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


print(dir(builtins))

"""
[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+
"""