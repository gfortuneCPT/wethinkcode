from sys import stdout,stdin
import  unittest
from robot import *
from unittest.mock import patch
from io import StringIO


class   Testrobot(unittest.TestCase):

    del history[:]
    def test_add_to_history(self):
        """
        Test append to history list
        """
        add_to_history("forward 10")
        self.assertEqual(history, ["forward 10"])


    def test_replay_silent(self):
        """
        Test correct output for silent flag
        """
        self.assertEqual(replay("HAL","silent"), (True, " > HAL replayed 1 commands silently."))

    
    def test_replay_reversed(self):
        """
        Test correct output for revered flag
        """
        self.assertEqual(replay("HAL","reversed"), (True, " > HAL replayed 1 commands in reverse."))

    
    def test_replay_silent_revered(self):
        """
        Test correct output for silent and reverse flag
        """
        self.assertEqual(replay("HAL","silent reversed"), (True, " > HAL replayed 1 commands in reverse silently."))

    
    def test_replay_silent_reversed_basic_range(self):
        """
        Test correct output for silent and reversed range flag
        """
        add_to_history("forward 10")
        self.assertEqual(replay("HAL"," 2 silent reversed"), (True, " > HAL replayed 2 commands in reverse silently."))


    def test_replay_silent_reversed_range(self):
        """
        Test correct output for silent flag
        """
        add_to_history("forward 10")
        add_to_history("forward 10")
        self.assertEqual(replay("HAL"," 3-1 silent reversed"), (True, " > HAL replayed 2 commands in reverse silently."))


    def test_valid_flags(self):
        """
        Test if for range, silent and reversed flag entered
        """
        self.assertEqual(valid_flags("2 silent revresed"), True)
        self.assertEqual(valid_flags("3-1 silent revresed"), True)
        self.assertEqual(valid_flags("3-4 silent revresed"), False)
        self.assertEqual(valid_flags("3--1 silent revresed"), False)