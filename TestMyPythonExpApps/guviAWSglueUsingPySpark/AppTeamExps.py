'''Import Everyting from math'''
from math import *
print("\nPi Val : ",pi)
print("\nReq Val : ",3**5)

def myDistinctFuncTest(*dataVals):
    myLi=[]
    print("\nUsing '*' for any numbers of arguments ")
    for di in dataVals:
        if di in 'app' :
            myLi.append(di)
    return myLi

tap=myDistinctFuncTest("app","qa","app","AL_tech")
print(tap)

cirAreaVarAnnoFun=lambda r:pi*r*r
cirPeriVarAnnoFun=lambda r:2*pi*r

print("\nArea of Circle : ",cirAreaVarAnnoFun(5))
print("\nPerimeter of Circle : ",cirPeriVarAnnoFun(10.52))

def findGcdOfTwoNums(num,num2):
    if num2==0:
       return num
    else:
        return findGcdOfTwoNums(num2,num%num2)

num=int(input("\nEnter 1st Num : "))
num2=int(input("\nEnter 2st Num : "))
print("\nGCD of two numbers : ",findGcdOfTwoNums(num, num2))


 