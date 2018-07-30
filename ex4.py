# Export all the things
# How many cars?  100
cars = 100
# How much space, in sq ft?, is in a car
space_in_car = 4.0
# How many drivers do we have?
drivers = 30
# How many passengers do we have?
passengers = 90
# How may cars in our fleet will be idle?
cars_not_driven = cars - drivers
# How many cars will be driven?  Hint is the same as drivers
cars_driven = drivers
# Let's use some math to figure out how many people can fit in each car
carpool_capacity = cars_driven * space_in_car
# Let's divide passengers by cars_driven and know the avg passengers per car
average_passengers_per_car = passengers / cars_driven

# Now let's print out all the things

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "carpool people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
