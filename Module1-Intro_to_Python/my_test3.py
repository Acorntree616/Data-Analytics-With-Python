import MyNumber as mn
from sys import argv

script, x = argv

number = mn.MyNumber(int(x))
number.print()