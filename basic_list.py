"""
Program: basiclist.py
Author:  Spencer Cress
Date: 06/21/2020

Functions for Basic List Assignment
"""
def get_input():
    """
    :returns: A string, that should be a number
    """
    x = input("Please input a number: ")
    return x


def make_list():
    """
    :returns: a list of three numbers
    :raises ValueError: given non-numeric input
    """
    my_list = []

    for n in range(1, 4):
        try:
            x = get_input()
            x = int(x)
            my_list.insert(0, x)
        except:
            ValueError
    return my_list



if __name__ == '__main__':
    pass
