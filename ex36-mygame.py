

# =================================
##  Joel Sheppard - ex36
## Learn Python3 the Hard way
## Make my own game based on ex35
# =================================
from sys import exit

def hurricane():
    print("There's a hurricane coming!  Are you staying (0) or leaving (1)?")

    choice = input("$> ")
    if "0" in choice or "1" in choice:
        plans = int(choice)
    else:
        oh_snap("Please type either staying or leaving, thanks!")

    if plans != 0:
        print("So you're staying?!! Good luck, we're outta here!!!!")
        exit(0)

def snake_house():
    print("OMG!  There's a giant SNAKE floating in here!!")
    print("The Snake is swimming at you!!")
    print("There's a window open to your right.")
    print("How will you get the Snake out the window?")
    snake_gone = False

    while True:
        choice = input("#> ")

        if choice == "grab it":
            oh_snap("OMG!  The Snake bites you in the face!!!")
        elif choice == "push it" and not snake_gone:
            print("The snake is gone, woot!!")
            print("We're safe now.")
            snake_gone = True
        else:
            print("IDK What you're trying to say, please type either 'grab it' or 'push it, thanks!'")

def yeti():
    print("I am the great YETI!!")
    print("I'm here to fuck with your mind!!")
    print("Do you flee for your life or remain and go insane?")

    choice = input("%> > ")

    if "flee" in choice:
        start()
    elif "insane" in choice:
        oh_snap("Oh dear, that's unfortunate.")
    else:
        yeti()

def oh_snap(why):
    print(why, "this is WHY...")
    exit(0)

def start():
    print("You just woke up in a strange hotel room in Las Vagas...")
    print("You jump up and there's a dead body in the bed with you!")
    print("You run to the door and you can go either right or left.")
    print("Which way do you go - left or right?")

    choice = input(">> > ")

    if choice == "left":
        snake_house()
    elif choice == "right":
        yeti()
    else:
        oh_snap("You can't fuck with us, you're dead Mother Fucker!!!!!!")


start()
