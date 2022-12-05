'''
Created on 14-Jul-2022

@author: abhi
'''
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
      print(dct[x][1], end="\n")
print("======================")
for it in "caratLane":
      if it=="L":
            break
      print(it, end="\t")
print("\n========= Break Example completed =============\n")
for it in "abhinayLqaSDET":
      if it=="y":
            continue
      print(it, end="\n")
print("========= Continue Example completed =============")