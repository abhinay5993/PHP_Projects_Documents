list_of_env = ["dev","stg","prd","test","qa"]

key = "testing"
is_found = False
for env in list_of_env:
    if env == key:
        is_found = True

if is_found:
    print("Found")
else:
    print("Not Found")