list_of_nums = []
j = 0
n = int(input("Enter the range for your loop"))

for i in range(n):
    num = int(input("Enter the number"))
    list_of_nums.append(num)

least = list_of_nums[0]
second = list_of_nums[0]

while(j < len(list_of_nums)):
    if list_of_nums[j] == least or list_of_nums[j] == second:
        j = j + 1
    elif list_of_nums[j] < least:
        second = least
        least = list_of_nums[j]
        j += 1
    elif list_of_nums[j] > second and (list_of_nums[j] - least) <= (list_of_nums[j] - second):
        second = list_of_nums[j]
        j += 1
    elif list_of_nums[j] < second and list_of_nums[j] > least:
        second = list_of_nums[j]
        j += 1
    else:
        j += 1
print(least)
print(second)