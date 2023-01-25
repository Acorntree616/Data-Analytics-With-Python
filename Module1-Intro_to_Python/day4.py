#import the needed package (Argv)
from sys import argv
#argv unpacking into separate defined variables
script, age, weight, height = argv
#print and format "" defines the common string
print("Your weight is {}, your age is {} and your height is {}.".format(weight, age, height))