# Python the hard way Joel Sheppard 2018
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL+C (^C).")
print("If you DO want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines of text.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("let's write these to a file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Lastly we close the file.")
target.close()
