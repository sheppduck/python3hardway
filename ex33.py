# =============================
##  Joel Sheppard - ex33
## Learn Python3 the Hard way
# =============================
from sys import argv

i = 0
numbers = []
var1 = 6
#incr = input()

#
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)

#=============================================
# Convert while loop above to a function that can be called
# and replace 6 in the i < 6 with a variable
# def prn_loop(my_num):
#     while i < var1:
#         return "At the top of i is {i}"
#         numbers.append(i)
#         i - i + 1
#         return "Numbers now: "(numbers)
#         return "At the bottom i is {i}"
#     return "The numbers: "
#     for num in numbers:
#         return(num)

#=============================================
# Add another variable for '1' so one can pass in the increment
# in the i - i + 1 incrementer
#=============================================
# def prn_loop(my_num):
#     while i < var1:
#         return "At the top of i is {i}"
#         numbers.append(i)
#         i - i + (incr)
#         return "Numbers now: "(numbers)
#         return "At the bottom i is {i}"
#     return "The numbers: "
#     for num in numbers:
#         return(num)

#=============================================
# try to make a for loop out of the crap above
#=============================================
for i in range(0, 6):
    print(f"At the top of i is {i}")
    numbers.append(i)
    print(f"Number now: ", numbers)
