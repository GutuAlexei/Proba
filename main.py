import re
import string
translator = str.maketrans('', '', string.punctuation)

def read_file(name):
    with open(name, "r") as file:
        return file.read()

def fara_punctuatie(text):
    return text.translate(translator)

def elimin_spatii_multiple(text):
    return re.sub(' +', ' ', text)

text=read_file("nume.txt")
text1 = fara_punctuatie(text)
text2= elimin_spatii_multiple(text1)
print(text2)