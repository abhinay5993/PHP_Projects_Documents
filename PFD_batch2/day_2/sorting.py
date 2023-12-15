"""
Bubble sort
"""
list_of_num=[1,1,2,3,-1,4,-2,0,56,89,5]

for i in range(len(list_of_num)):
    for j in range(len(list_of_num)):
        if list_of_num[i] < list_of_num[j]:
            temp = list_of_num[i]
            list_of_num[i] = list_of_num[j]
            list_of_num[j]=temp

print(list_of_num)