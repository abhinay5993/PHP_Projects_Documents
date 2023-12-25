set_1 = {1,1,1,1,1,2,2,2,2,3,3,4,45,4,34,3,2}
set_2 = {1,1,1,1,45,6,6,7,7,8,4,3,3}
print(set_1.intersection(set_2))
print(set_1.union(set_2))

list_of_envs = ["dev","stg","prd","tst","qa","qa","dev"]
print(list_of_envs)
list_of_envs = list(set(list_of_envs))
print(list_of_envs)