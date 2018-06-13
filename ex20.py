#Joel Sheppard Learn Python 3 the Hard way
# ex. 20

# Import the argv module from the sys library
from sys import argv

# See below, its saying basically when executing this script, you need
# script name and the input file parse/read from.
script, input_file = argv

# I think this function is setting up to print out what is read in from the
# input_file
def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
