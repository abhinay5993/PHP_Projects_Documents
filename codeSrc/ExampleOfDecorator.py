from AwsS3ManagerUtils import *

@decorateConvertToUpper
def getTheUpdatedSentence():
    msg=input("\nEnter the input string : ")
    return msg

@decorateRemoveCommaAndAddSpaces
def getSingleSpacedSentence():
    msg=input("\nEnter the input string : ")
    return msg


print("\n ",getTheUpdatedSentence())
print("\n ",getSingleSpacedSentence())