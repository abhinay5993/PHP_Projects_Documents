num1 = float(input("Enter num 1"))
num2 = float(input("Enter num 2"))

opr = input("Enter operator")
output=None
if opr == "+":
    output=num1+num2

if opr == "-":
    output=num1-num2

if opr == "*":
    output=num1*num2

print("your calculation is: ",output)
#error hu mai
if num1 < 3:
    print("num1 is less than 3")
elif num1 == 3:
    print("num1 is equal to 3")
else:
    print("num1 is greater than 3")