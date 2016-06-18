from sys import argv # adds modules to the script from the python module set. Keeps scripts small as you only import the modules that you need. 'argv' is the argument variable

script, first, second, third = argv # unpacks argv and assigns it to four variables to work with

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# NOTE: modules are also known as libraries
