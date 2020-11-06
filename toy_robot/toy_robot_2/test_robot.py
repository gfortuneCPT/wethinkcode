from sys import stdout,stdin
import  unittest
from robot import *
from unittest.mock import patch
from io import StringIO



class   Testrobot(unittest.TestCase):

    def test_check_list_in_list(self):
        """
        check correct return for commands in list
        """
        com = ["OfF","Help","OFF"]
        not_in_com = ["random","fly","stuff"]
        com_list = ["off","help"]
        for i in com:
            self.assertEqual(check_in_list(i,com_list), True)
        for j in not_in_com:
            self.assertEqual(check_in_list(j,com_list), False)

    
    def test_help_command(self):
        """
        test correct output of help command
        """
        correct = """I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\n"""
        out = help_list()
        self.assertEqual(out[:98],correct)


    def test_move(self):
        """
        test correct movement command and steps return
        """
        movement = move("forward 5")
        self.assertTrue(int(movement[1]) == 5)
        self.assertEqual(movement[0], "forward")

    
    def test_change_position_fwd10(self):
        """
        test correct posision variable update for forward
        with different starting direction
        """
        position = change_position([0,0,0], ["forward", "10"])
        self.assertEqual(position, [10,0,0])
        position = change_position([0,0,90], ["forward", "10"])
        self.assertEqual(position, [0,10,90])
        position = change_position([0,0,180], ["forward", "10"])
        self.assertEqual(position, [-10,0,180])
        position = change_position([0,0,270], ["forward", "10"])
        self.assertEqual(position, [0,-10,270])
        

    def test_change_position_bck10(self):
        """
        test correct position variable update for back move
        with different starting direction
        """
        position = change_position_back([0,0,0], ["back", "10"])
        self.assertEqual(position, [-10,0,0])
        position = change_position_back([0,-10,90], ["back", "10"])
        self.assertEqual(position, [0,-20,90])
        position = change_position_back([10,0,180], ["back", "10"])
        self.assertEqual(position, [20,0,180])
        position = change_position_back([0,10,270], ["back", "10"])
        self.assertEqual(position, [0,20,270])


    def test_change_position_sprint_5(self):
        """
        test correct position variable update for sprint move
        """
        position = change_position([0,0,0], ["sprint", "5"])
        self.assertEqual(position, [5,0,0])
        position = change_position([0,0,90], ["sprint", "5"])
        self.assertEqual(position, [0,5,90])
        position = change_position([0,0,180], ["sprint", "5"])
        self.assertEqual(position, [-5,0,180])
        position = change_position([0,0,270], ["sprint", "5"])
        self.assertEqual(position, [0,-5,270])


    def test_move_is_valid_True_False(self):
        """
        test correct return if move is valid
        test for out of bounds
        """
        move = move_is_valid([0,0,90],["forward", "10"])
        self.assertTrue(move == True)
        move = move_is_valid([0,0,90],["forward", "300"])
        self.assertTrue(move == False)


    def test_sprint_5(self):
        """
        test correct sprint position update
        """
        sp = sprint(5,[0,0,90])
        self.assertEqual(sp,[0,15,90])