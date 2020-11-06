import importlib
import  unittest
import sys
import world.text.world as world
import maze.obstacles as obs
from unittest.mock import patch
from io import StringIO

from world.text.world import solve_maze


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
        obs.obstacles =[(2,2)]
        
        
        self.assertEqual(world.is_position_allowed(2,1), (True, 0))
        self.assertEqual(world.is_position_allowed(3,3), (True, 0))
        self.assertEqual(world.is_position_allowed(300,330), (False, 0))


    def test_maze_to_grid_goal_top(self):
        """
        Test correct maze to array conversion, check correct goal
        and length of array and length of array element
        """
        obs.min_x, obs.max_x = -25, 25
        obs.min_y, obs.max_y = -25, 25
        obs.obstacles = [(0,10)]

        grid, goal = world.maze_to_array("top")

        self.assertEqual(len(grid), 101)
        self.assertEqual(len(grid[1]), 51)
        self.assertEqual(goal, (100,25))


    def test_y_x_to_direction_with_obs(self):
        """
        Test correct return of directions, when obstacle in path
        """

        obs.min_x, obs.max_x = -25, 25
        obs.min_y, obs.max_y = -25, 25
        obs.obstacles = [(0,10)]
        importlib.reload(world)

        directions = solve_maze("top")
        self.assertEqual(directions, [['W', 1], ['N', 15],['E', 1], ['N', 10]])


    def test_y_x_to_direction_no_obs(self):

        """
        Test correct return of directions, when no obstacle in path
        """

        obs.min_x, obs.max_x = -25, 25
        obs.min_y, obs.max_y = -25, 25
        obs.obstacles = [(0,10)]
        importlib.reload(world)

        directions = solve_maze("bottom")
        self.assertEqual(directions, [['S',25]])
    

    def test_solve_maze_no_obs(self):

        """
        Test correct return of directions, when no obstacle in path, 
        correct return after consecutie runs
        """
        obs.min_x, obs.max_x = -25, 25
        obs.min_y, obs.max_y = -25, 25
        obs.obstacles = []
        importlib.reload(world)

        directions = solve_maze("right")
        self.assertEqual(directions, [['E',25]])
        directions = solve_maze("left")
        self.assertEqual(directions, [['W', 25]])
    

    def test_solve_maze_obs(self):

        """
        Test correct return of return of directions with obs,
        correct return after multiple runs
        """
        obs.min_x, obs.max_x = -25, 25
        obs.min_y, obs.max_y = -25, 25
        obs.obstacles = [(5,0)]
        importlib.reload(world)

        directions = solve_maze("right")
        self.assertEqual(directions, [['S', 1], ['E', 25], ['N', 1]])
        directions = solve_maze("left")
        self.assertEqual(directions, [['W', 25]])