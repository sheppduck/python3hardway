# Joel Sheppard ex. 13b

from sys import argv

# I think this bool thing below is useless
# I tested answering w/o a boolean response and
# The input was accepted and printed back out to stdout

label = bool

print("What script would you like to run?", end=' ')
script = input()

print("The POD has no Vulnerabilies:", end=' ')
label = input()

print("The test case that was executed was:", end=' ')
test = input()

print("The test results were?", end=' ')
result = input()

print(f"{script}")
print (f"{test}")
print(f"{result}")

print(f"{label}")
