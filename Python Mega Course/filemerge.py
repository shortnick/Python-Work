#! python3

import datetime

"""This is a script to merge text files."""


filename=datetime.datetime.now()

def create_file(xyz):
    with open(filename.strftime("%y-%m-%d-%H-%M-%S"), "w") as file:
        file.write(xyz)

def open_file(x):
    with open(x, 'r') as file:
        content = file.read()
        return content

first = open_file('file1.txt')
second = open_file('file2.txt')
third = open_file('file3.txt')

output = first + "\n" + second + "\n"+ third
create_file(output)
