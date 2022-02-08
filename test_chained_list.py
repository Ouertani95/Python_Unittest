#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testing the methods from ChainedList class
"""

__author__ = 'Mohamed Ouertani'

import unittest
import copy
from chained_list_class import ChainedList



class ChainedTest(unittest.TestCase):
    """Test case for testing ChainedList class methods"""

    def setUp(self):
        """Initializing tests"""
        self.liste = ChainedList()

    def test_is_empty(self):
        """Testing if a newly created ChainedList object is empty"""
        self.assertIsNone(self.liste.first_node)

    def test_is_not_empty(self):
        """Testing the addition of a new node to an empty ChainedList object"""
        self.liste.add_node(2)
        self.assertIsNotNone(self.liste.first_node)

    def test_unchanged(self):
        """Testing the add and remove methods"""
        list_before = copy.deepcopy(self.liste)
        self.liste.add_node(4)
        self.liste.remove_node(4)
        match = self.liste.is_matching(list_before)
        self.assertTrue(match)

    def test_is_last(self):
        """Testing the addition of the biggest value node at the end of a ChainedList object"""
        self.liste = ChainedList()
        self.liste.add_node(3)
        self.liste.add_node(-1)
        self.liste.add_node(15)
        self.liste.add_node(6)
        last_index = self.liste.length()-1
        #The Chained list elements could be indexed thanks to the __getitem__ method
        self.assertEqual(self.liste[last_index],15)


if __name__ == '__main__':
    unittest.main()
