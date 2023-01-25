from sys import argv
script, file_name = argv

file = open(file_name)

file_content = file.read()

print(file_content)

file.close()