cars = 100
drivers = 30
space_in_a_car = 4.0
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = space_in_a_car * cars_driven
average_passengers_per_car = passengers/cars_driven

# the "=" is used for naming things or declaring things
# whereas "==" is used for comparison or testing if two variables have the same value

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "---------------------------"

print "Using substitution with the % character"
print
print
print "There are %d cars available today." % cars