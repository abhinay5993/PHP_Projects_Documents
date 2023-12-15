server_1 = {
    "env":"dev",
    "server":"aws linux2",
    "ram":8096,
    "cpu":4,
    "active":True
}
server_2 = {
    "env":"prd",
    "server":"aws linux2",
    "ram":10240,
    "cpu":8,
    "active":False
}
env_details = [server_1,server_2]

for env in env_details:
    for key,value in env.items():
        if key=="active" and value==True:
            print(env.keys())
