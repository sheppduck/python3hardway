# How many people are there?
types_of_people = 10

# Set a variable for x and inject the types_of_people variable
x = f"There are {types_of_people} types of people."

# set binary to binary
binary = "binary"
# set do_not to don't
do_not = "don't"
#set up a new var and include binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# print out x
print(x)
# print out y
print(y)


print(f"I said: {x}")
print(f"I also said '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# Using the plus concatenate w and e into one long sentence
print(w + e)
