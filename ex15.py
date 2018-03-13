# Python the hard way Joel Sheppard 2018

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's our file {filename}: ")
print(txt.read())
txt.close()
# Close the open file object

print("Type the filename again please:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
# Close the open file object
txt.close()
