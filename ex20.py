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

# So this basically 'rewinds' an open file back to whatever position defined in seek
# 0 in this case - or - the first byte of the file
def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())

# This would be the input file passed into the script and open the file
current_file = open(input_file)

print("First let's print the whole file:\n")

# Now that the file is open, print it out to the screen - stdout
print_all(current_file)

print("Now let's rewind, kind of like tape.")

# Now we call rewind and go back to the 0th position in our file
rewind(current_file)

print("Let's print three lines:")

# the current line in the input file - 1st line in this case
current_line = 1
print_a_line(current_line, current_file)

#Increase the current line by 1 and print it (i.e. print line 2)
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# Again, Increase by one line and print it out (i.e. line 3 now)
current_line += 1
print_a_line(current_line, current_file)
