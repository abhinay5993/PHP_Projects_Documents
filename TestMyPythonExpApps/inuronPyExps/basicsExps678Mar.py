'''
Created on 12-Jun-2021

@author: abhinay
'''

print("\nWhile with Else")
i=1
while i<20:
         i=i+1
         if i%2==0:
             print("\nNum : ",i)
else:
    print("\nLoops Overs into Else")
    xData="Welcome to iNuron"
    co=0
    for j in range(0,xData.__len__()):
             print(xData[j],"<--- position --> ",co)
             co=co+1
    
    print("\nExtracted string Data Through Slice Operator and Steps-or-jump : ",xData[2:10:2])
    
n=10
for i in range(n,0,-1):
      for j in range(n-i):
            print(' ',end='')
      for j in range(2*i-1):
            print("*",end="")
      print()
      
print("================================")
l=10
while i<=l:
      i=i+1
      sc=0
      while sc<(l-i):
            print(" ",end='')
            sc=sc+1
            
      ns=2*i-1
      while ns>0:
            print("*",end='')
            ns=ns-1
      print()

tStr="AbhinayL "
print("\nRepeate : ",tStr*5)