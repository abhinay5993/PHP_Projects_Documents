"""
This program will take 2 numbers and find its sum
"""
def sum_of_two(): #creation
    a = int(input("enter 1st number"))
    b = int(input("enter 2nd number"))

    c = a + b
    print("addition is: ",c)

def diff_of_two(): #creation
    a = int(input("enter 1st number"))
    b = int(input("enter 2nd number"))

    c = a - b
    print("subtraction is: ",c)

def check_list_elements():
    list_of_nos = [1,2,3,4,5]
    for i in list_of_nos:
        if i %2 == 0:
            print("even")
        else:
            print("odd")    