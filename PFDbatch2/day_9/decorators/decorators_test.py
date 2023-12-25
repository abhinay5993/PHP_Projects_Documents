def convert_upper(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs).upper() #processing
    return wrapper

@convert_upper
def show_word(word,word2,word3):
    return word

print(show_word("this"))


def remove_punctuations(func):
    def wrapper():
        return func().replace(",","")
    return wrapper

@remove_punctuations
def take_sentence():
    sent = input("Enter a sentence")
    return sent

print(take_sentence())