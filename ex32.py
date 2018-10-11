# =============================================
##  Joel Sheppard - Learn Python3 the hard way
##  Example 32 - Loops and Lists
# =============================================

# Things in my predetermined List
the_count = [1, 2, 3, 4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This loops goes through the list and prints the list item
for number in the_count:
    print(f"This is count {number}")

# Same - go through the list and print the list item
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# Mixed List print
for i in change:
    print(f"I got {i}")

# Let's build a list up from scratch
elements = []
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append i
    elements.append(i)
    # reverse list
    elements.reverse()
    # sort and reverse i - same but different (and dumb, lol)
    elements.sort(reverse=True)

# Let's print them out
for i in elements:
    print(f"Element was: {i}")
