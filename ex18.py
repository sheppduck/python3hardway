# Joel Sheppard Learn Python 3 the Hard Way
# Ex 18

# this is like the argv scripts except funcs

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# okay, that *argsd is actually pointless, we could just do this
def print_two_again(arg1, arg2):
    print(f"arg1 {arg1}, arg2 {arg2}")

# this one just takes one argument

def print_one(arg1):
    print(f"arg1: {arg1}")

# ths one takes no args
def print_none():
    print ("I got nuttin'...")

print_two("Joel","Sheppard")
print_two_again("Joel","Sheppard")
print_one("First!")
print_none()
