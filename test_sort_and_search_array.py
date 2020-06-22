"""
Program: test_sort_and_search_array.py
Author:  Spencer Cress
Date: 06/21/2020

Tests for the two functions in search and sort array assignment
"""

import unittest
import array as arr
from fun_with_collections.sort_and_search_array import search_array
from fun_with_collections.sort_and_search_array import sort_array


class MyTestCase(unittest.TestCase):
    def test_sort_array(self):
        """Test search_list function for valid output of item not in list"""
        self.assertEqual(sort_array([6, 4, 9, 10]), [4, 6, 9, 10])

    #def test_search_list_found(self):
        """Test search_list function for valid output of item in list"""
     #   self.assertEqual(search_array([6, 4, 9, 10], 9), 2)

    #def test_search_array_not_found(self):
        """Test search_list function for valid output of item not in list"""
    #    self.assertEqual(search_array([6, 4, 9, 10], 15), -1)





if __name__ == '__main__':
    unittest.main()
