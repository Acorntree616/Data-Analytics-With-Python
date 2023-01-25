from sys import argv
script, file_name, destination_file = argv

file = open(file_name)
file_dest = open(destination_file, "w")
file_content=file.read()
file_dest.write(file_content)
file.close()
