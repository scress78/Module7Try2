"""
Program: sort_and_search_list.py
Author:  Spencer Cress
Date: 06/21/2020

This program contains the functions sort_list and search_list for
Search and Sort List Assignment
"""


def sort_list(x):
    """
    :parameter x: a list to be sorted
    :returns: A sorted list
    """
    x.sort()
    return x


def search_list(x, y):
    """
    :parameter x: a list to be searched
    :parameter y: the item to be searched for in the list
    :returns: the index of the item in the list, if it is in the list; otherwise -1 if it isn't.
    """
    try:
        z = x.index(y)
    except ValueError:
        z = -1
    return z

