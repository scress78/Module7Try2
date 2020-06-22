"""
Program: sort_and_search_array.py
Author:  Spencer Cress
Date: 06/21/2020

This program contains the functions sort_array and search_array for
Search and Sort List Assignment
"""
import array as arr


def sort_array(x):
    """
    :parameter x: a list to be cast into an array, cast back into a list, sorted and then output
    :returns: A sorted list
    """
    try:
        my_array = arr.array('i', x)
    except ValueError:
        raise ValueError from None

    my_other_list = []
    for a in my_array:
        my_other_list.append(a)
    my_other_list.sort()
    return my_other_list
    pass
    # this array WILL include a return, that return will be the sorted list.
    # I'm doing it this way because it makes sense to me to have a return
    # since we eventually need a test to pass. It doesn't work for me without a return


def search_array(x, y):
    """
    :parameter x: a list to be searched
    :parameter y: the item to be searched for in the list
    :returns: the index of the item in the list, if it is in the list; otherwise -1 if it isn't.
    """
    try:
        my_search_array = arr.array('i', x)
    except ValueError:
        raise ValueError from None
    my_list_search_array = []
    for a in my_search_array:
        my_list_search_array.append(a)
    try:
        z = my_list_search_array.index(y)
    except ValueError:
        z = -1
    return z
    pass


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


def get_input():
    """
    :returns: A string, that should be a number
    """
    x = input("Please input a number: ")
    return x


if __name__ == '__main__':
    # x = make_list()
    # sort_array(x)
    y = make_list()
    search_array(y, 15)
