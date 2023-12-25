
def check_string_case():
    word = input("enter the word")

    if word.islower():
        print("the input is in lower case")
    elif word.isupper():
        print("the input is in upper case")
    else:
        print("the input is in mixed case")
