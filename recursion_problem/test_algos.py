from sys import setdlopenflags, stdout,stdin
from types import CodeType
import  unittest
from super_algos import find_min, sum_all, find_possible_strings
from unittest.mock import patch
from io import StringIO



class   TestCreateCode(unittest.TestCase):

    def test_find_min_str_test(self):
        """Test return -1 if str in list"""
        test_lst=[4,6,8,7,4,5,2,3,1,"s"]
        self.assertEqual(find_min(test_lst), -1)
    

    def test_find_min_correct(self):
        """Test correct output even with negitive int"""
        test_lst = [8,9,5,2,3,55,45,56,48,-8]
        self.assertEqual(find_min(test_lst), min(test_lst))


    def test_find_min_empty(self):
        """Test return -1 on empty list as parameter"""
        self.assertEqual(find_min([]), -1)


    def test_sum_all_str_test(self):
        """Test return -1 if str in list"""
        test_lst=[4,6,8,7,4,5,2,3,1,"s"]
        self.assertEqual(sum_all(test_lst), -1)
    

    def test_sum_all_correct(self):
        """Test correct output even with negitive int"""
        test_lst = [8,9,5,2,3,55,45,56,48,-8]
        self.assertEqual(sum_all(test_lst), sum(test_lst))


    def test_sum_all_empty(self):
        """Test return -1 on empty list as parameter"""
        self.assertEqual(sum_all([]), -1)
    

    def test_find_possible_strings_empty(self):
        """Test return -1 on empty list as parameter"""
        self.assertEqual(find_possible_strings([],3),[])
    

    def test_find_possible_strings_int(self):
        """Test return empty list with int as input"""
        self.assertEqual(find_possible_strings([1,2],2), [])
        self.assertEqual(find_possible_strings(["A","B",2], 3), [])
    

    def test_find_possible_strings_correct(self):
        """Test correct return"""
        self.assertEqual(find_possible_strings(["A","B"],2),["AA","AB","BA","BB"])