import  unittest
import sys
import world.text.world as world
import world.obstacles as obs
from unittest.mock import patch
from io import StringIO


class   Testworld(unittest.TestCase):

    
    def test_display_obstacles(self):
        """
        Test correct return of obstacles print to sys.stdout
        """
        obs.random.randint = lambda a, b: 2
        
        import importlib
        importlib.reload(obs)

        output = StringIO()
        sys.stdout = output
        
        world.display_obstacles()
        
        sys.stdout = sys.__stdout__
        
        self.assertEqual(
        """There are some obstacles:\n- At position 2,2 (to 6,6)\n""",
         output.getvalue())



    def test_is_position_allowed(self):
        """
        Test correct return for obstacle block or out of range
        """
        obs.obstacles = [(0,2)]
       
        self.assertEqual(world.is_position_allowed(0,3), (True, 0))
        self.assertEqual(world.is_position_allowed(3,3), (True, 0))
        self.assertEqual(world.is_position_allowed(300,330), (False, 0))