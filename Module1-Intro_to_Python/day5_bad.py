from sys import argv
from os.path import exists

script, num1, num2, num2, num3, out_filename = argv

file_exists = exsits(out_filename)
print("Does the output file exist? {}".format(file_exists))
print("Writing output to {}".format(out_filename))

out_file = open(out_filename)
outdata = out_file
print("Waiting... Type the RETURN key to continue")
  input()

answer = (num1 + num2 + num2 + num3 + num4) / (len(argv) - 1)

out_file.write("{:.2f}\n".format(answer))
print("\a")
out_file.close()