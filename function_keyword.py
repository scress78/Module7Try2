"""
Program: function_keyword.py
Author:  Spencer Cress
Date: 06/21/2020

Function Keyword & Arbitrary Arguments Assignment
"""


def average_scores(*args, **kwargs):
    """
    :parameter args: scores for given class
    :parameter kwargs: (various) current student name+value, course+value, GPA+value
    :returns: A statement of student's name, GPA, course name and average for the course
    """
    # Use *args for average calculation
    x = sum(args)/len(args)
    keywords_container = []
    # for key, value in kwargs.items():
    #    print("%s == %s" % (key, value))
    # return print("Result: %s" % kwargs(0))
    for key, value in kwargs.items():
        keywords_container.append(key)
        keywords_container.append(value)
        # print(keywords_container)
    one = keywords_container[0]
    two = keywords_container[1]
    three = keywords_container[2]
    four = keywords_container[3]
    five = keywords_container[4]
    six = keywords_container[5]
    print("Result: "+one+" = "+two+" "+five+" = "+six+" "+three+" = "+four+" with current average "+str(x))


if __name__ == '__main__':
    average_scores(4, 3, 2, 4, studentname='Michelle', coursename='Python', GPA='3.2')
    average_scores(45, 30, 28, 49, studentname='Ed', coursename='Anger Management', GPA='4')
    average_scores(99, 99, 99, 103, studentname='Albert', coursename='Math', GPA='3.2')
