# =================================
##  Joel Sheppard - ex38
## Learn Python3 the Hard way
## Working more with Lists!
# =================================

# ten_things = "Apples Oranges Crows Telephone Light Sugar"
#
# print("Wait, there are not 10 things in that list.  Let us fix that!")
#
# stuff = ten_things.split(' ')
# more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
#
# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print("Adding: ", next_one)
#     stuff.append(next_one)
#     print(f"There are {len(stuff)} items now!!")
#
# print("There we go: ", stuff)
#
# print("Let's do some things with stuff.")
#
# print(stuff[1])
# print(stuff[-1]) # fancy shit!
# print(stuff.pop())
# print(' '.join(stuff)) #What??
# print('#'.join(stuff[3:5]))

#=========== Some practice doing things to Lists ===============#

my_list = "Man Woman Animals Sun Sky Planets UFO"
print(my_list)
add_list = ["Cars", "Plants", "Trains", "Boats", "Fish", "Weather"]

print(add_list)
add_list.reverse()
print(add_list)

worker = my_list.split(' ')

while len(worker) != 12:
    add_stuff = add_list.pop()
    print("Adding: ", add_stuff)
    worker.append(add_stuff)
    print(f"There are {len(worker)} things in the list now!")


print (worker)
