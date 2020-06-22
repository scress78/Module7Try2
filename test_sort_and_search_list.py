"""
Program: test_sort_and_search_list.py
Author:  Spencer Cress
Date: 06/21/2020

Tests for the two functions in search and sort list assignment
"""

import unittest
from fun_with_collections.sort_and_search_list import search_list
from fun_with_collections.sort_and_search_list import sort_list


class MyTestCase(unittest.TestCase):
    def test_search_list_found(self):
        """Test search_list function for valid output of item in list"""
        self.assertEqual(search_list([6, 4, 9, 10], 9), 2)

    def test_search_list_not_found(self):
        """Test search_list function for valid output of item not in list"""
        self.assertEqual(search_list([6, 4, 9, 10], 15), -1)

    def test_sort_list(self):
        """Test search_list function for valid output of item not in list"""
        self.assertEqual(sort_list([6, 4, 9, 10]), [4, 6, 9, 10])



if __name__ == '__main__':
    unittest.main()
