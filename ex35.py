# =================================
##  Joel Sheppard - ex35
## Learn Python3 the Hard way
## Let's access elements in a list
# =================================
from sys import exit

def gold_room():
    print("This room is full of gold.  How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number would ya?!")

    if how_much < 50:
        print("Nice, you're not greedy, you win!!!")
        exit(0)
    else:
        dead("You greedy SOB!!!")

    def bear_room():
        print("There is a bear here.")
        print("The bear has a bunch of honey.")
        print("The fat bear is in front of another door.")
        print("How are you going to move that bear?")
        bear_moved = False

        ## Break time - 1 hour of code done today
