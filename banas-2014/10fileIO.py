import random
import sys
import os

print('\n')

test_file = open("file.txt", "wb")
print(test_file.mode)
print(test_file.name)

test_file.write(bytes("Write me into the file\n1", "UTF-8"))

test_file.close()

test_file = open("file.txt", "r+")

text_in_file = test_file.read()
print(text_in_file)

# os.remove("./test.txt")

print('\n')
