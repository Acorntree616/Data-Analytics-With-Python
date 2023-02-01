from sys import argv

if len(argv)==4:
    print("This script is named {}".format(argv[0]))
    print("  The value of argument 1 is: {}".format(argv[1]))
    print("  The value of argument 2 is: {}".format(argv[2]))
    print("  The value of argument 3 is: {}".format(argv[3]))

elif len(argv)!=4:
    print("WARNING: Not enough variables!")
