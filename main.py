import re

def read_file(name):
    with open(name, "r") as file:
        return file.read()

text=read_file("nume.txt")
print(text)