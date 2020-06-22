"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY

This program tests a function that prints 'Hello World'
as output.  The function is then called.
"""
import unittest
import unittest.mock as mock
from fun_with_collections import basic_list as topic1
from unittest.mock import patch


class MyTestCase(unittest.TestCase):

    @patch('fun_with_collections.basic_list.get_input', return_value='6')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [6, 6, 6])


if __name__ == '__main__':
    unittest.main()
