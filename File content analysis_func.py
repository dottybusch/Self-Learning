import os
from collections import Counter
def new_file(file_name):
    new_file = open(file_name + ".txt", mode="w+")
    new_file.write(input("Enter content for your new file: "))
    new_file.close()

def read_file(file_name):
    read_file = open(file_name + ".txt", mode="a+")
    read_file.seek(0)
    return read_file.read()

def split_text(file_name):
    content = read_file(file_name)
    return content.lower().split()

def display_result(file_name):
    print("Text to analyze:")
    print("_________________")
    print("\n")
    print(read_file(file_name))
    print("\n")
    print("Analysis:")
    print("__________")
    print("\n")
    for key, value in dict(Counter(split_text(file_name)).most_common()).items():
        print(key + ": " + str(value))



file_name = input("Enter a file name: ")
new_file(file_name)
read_file(file_name)
display_result(file_name)
