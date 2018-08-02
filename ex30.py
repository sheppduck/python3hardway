# =============================
# Joel Sheppard
# Learn Python 3 the Hard way
# Ex 30 else and if
# =============================

people = 20
cars = 30
trucks = 15

# cars and people
if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We should NOT take the cars!")
else:
    print("We can't decide.")

# trucks and cars
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks?")
else:
    print("We still can't decide")

# people and trucks
if people > trucks:
    print("Alright, let's take the trucks.")
else:
    print("Fine, let's stay home then.")
