from sys import setdlopenflags, stdout,stdin
from types import CodeType
import  unittest
import  mastermind as mm
from unittest.mock import patch
from io import StringIO

from mastermind import take_turn


class   TestCreateCode(unittest.TestCase):
    def test_code(self):
        """
        Test Creat_code() output:
        test_for_duplicate: if length is correct, code uses a set len will be incorrect on duplicates
        """
        for i in range(100):
            code = mm.create_code()
            # Test Length of Code
            self.assertAlmostEqual(len(code),4)
            for i in code:
                self.assertTrue(0<i<9)
            # Test for duplicates
            self.assertTrue(len(code) == len(set(code)))


    def test_correctness(self):
        """
        Test if correct bool is returned when all correct and 1 correct
        """
        check = mm.check_correctness(10,4)
        self.assertTrue(check == True)
        check = mm.check_correctness(10,1)
        self.assertTrue(check == False)
    

    @patch("sys.stdin", StringIO("12345\n1234\n"))
    def test_get_user_input_incorrect(self):
        """ 
        Test handling incorrect length digit input
        """
        self.assertEqual(mm.get_answer_input(), [1 ,2 ,3 ,4 ])
    

    @patch("sys.stdin", StringIO("sfdg\nas\n4567"))
    def test_get_user_input_str_input(self):
        """ 
        Test correct handling of string input of correct length
        and incorrect length
        """
        self.assertEqual(mm.get_answer_input(), [4, 5, 6, 7])
    
    
    @patch("sys.stdin", StringIO("1467\n1234"))
    def test_take_turn(self):
        """
        Test correct return of digits in correct places and incorrect places
        and then all correct digits in correct places
        """
        # 1 correct
        code = [1,2,3,4]
        take_turn_tuple = take_turn(code)
        self.assertEqual(take_turn_tuple[0], 1)
        self.assertEqual(take_turn_tuple[1], 1)

        # all correct
        code = [1,2,3,4]
        take_turn_tuple = take_turn(code)
        self.assertEqual(take_turn_tuple[0], 4)
        self.assertEqual(take_turn_tuple[1], 0)


