import os as os

file_dir = os.path.dirname(__file__)
file_name = "Cheesesauce.txt"
f = open(os.path.join(file_dir, file_name), "w")
f.write("First line\n")
input_list = ['1\t', '3\t', '5\n']
f.writelines(input_list)
f.close()




"""file_dir = os.path.dirname(__file__)
file_name = "testfile"
f = open(os.path.join(file_dir, file_name), "r")
line1 = f.read()
print(line1)"""

