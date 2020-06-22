"""
Program: functions.py
Author:  Spencer Cress
Date: 06/21/2020

Functions for Python File I/O with Tuples Assignment
"""

import os as os


def write_to_file(x):
    """
    :parameter x: A string to be appended onto student_info
    :returns: nothing. This function simply adds the argument to the end of student_info.txt
    """
    file_dir = os.path.dirname(__file__)
    file_name = "student_info.txt"
    f = open(os.path.join(file_dir, file_name), "a")
    f.writelines(x)
    # print("this ran")


def get_student_info(student_name=''):
    """
    :parameter student_name: the name of the student, assigned to their test scores
    :returns: nothing. This function accepts a student_name as an argument, then allows
    you to enter various test scores and calls write_to_file to append the test scores
    and student name to student_info.txt
    """
    continue_input = 0
    score_container = []
    test_scores_by_student = []
    test_scores_by_student.append(student_name)
    while continue_input == 0:
        scores = input("Input as many test scores as you'd like, enter -1 to quit.")
        if scores != '-1':
            score_container.append(scores)
        if scores == '-1':
            continue_input += 1
    test_scores_by_student.append(score_container)
    print(test_scores_by_student)
    write_to_file(test_scores_by_student[0])
    write_to_file(" "+str(test_scores_by_student[1])+"\n")


def read_from_file():
    """This function reads student_info.txt line by line"""
    file_dir = os.path.dirname(__file__)
    file_name = "student_info.txt"
    f = open(os.path.join(file_dir, file_name), "r")
    print("this Ran")
    line = f.readline()
    while line != "":
        print(line)
        line = f.readline()
    # or each_line in f.readline():
    #    print(each_line)


if __name__ == '__main__':
    get_student_info(student_name='Jeb')
    get_student_info(student_name='Barbara')
    get_student_info(student_name='George')
    get_student_info(student_name='Jill')
    read_from_file()
