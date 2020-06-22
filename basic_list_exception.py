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
    :raises ValueError: given non-numeric input or input that is less than 1 or greater than 50
    """
    my_list = []

    for n in range(1, 4):
        try:
            x = get_input()
            x = int(x)
            if x < 1:
                raise ValueError from None
            if x > 50:
                raise ValueError from None
            my_list.insert(0, x)
        except ValueError:
            raise ValueError from None
    return my_list


if __name__ == '__main__':
    make_list()
