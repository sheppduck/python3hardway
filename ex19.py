# Joel Sheppard Python 3 the Hard Way
# Ex 19

# Cheese and Crackers
# The below is a function, in this case used to pass variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of Crackers")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

# Below we're passing in integers to cheese_count (20) and boxes_of_crackers (30)
print("We can just give functions numbers directly:")
cheese_and_crackers(20, 30)

# Next we explicitly set the variable and a value for each
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Now some basic math
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# and lastly, combining variables and integers
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def buds_and_bowls(bud_count, num_of_bowls):
    print(f"You have {bud_count} buds!")
    print(f"You own {num_of_bowls} bowls?!?!?!?  That's less than me!  :P")
    print("that's enough for a sick ass party!!")
    print("Grab the buds! \n")

print("Let's give the vars numbers...")
buds_and_bowls(10, 2)
