import re
import string
translator = str.maketrans('', '', string.punctuation)

def read_file(name):
    with open(name, "r") as file:
        return file.read()

text=read_file("nume.txt")
fara_punctuatie = text.translate(translator)
print(out)