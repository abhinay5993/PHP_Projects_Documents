'''
Created on 11-Mar-2022

@author: abhi
'''

def computeHashOfString(inpdata):
    hashval=(ord(inpdata[0])*100)+ord(inpdata[1])
    return hashval

print("\nHash value : ",computeHashOfString(input("\nEnter Data : ")))
        