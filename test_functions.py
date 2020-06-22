import os as os

file_dir = os.path.dirname(__file__)
file_name = "student_info.txt"
f = open(os.path.join(file_dir, file_name), "w")
x = "Student Name:\tStudent Phone:\tStudent Address:\t"
f.writelines(x)
