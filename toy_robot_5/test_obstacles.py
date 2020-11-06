import  unittest
import maze.obstacles as obs


class   Testrobot(unittest.TestCase):

    
    def test_check_obstacles_not_empty(self):
        """
        Test obstacles not empty and if (0,0) not in obstacles
        """
        obs.obstacles = [(5,8)]

        self.assertTrue(len(obs.get_obstacles()) > 0)
        self.assertTrue((0,0) not in obs.get_obstacles())


    def test_check_obsyacles_lambda(self):
        """
        Test obstacles return empty list with randintb = 0
        no obstacle at (0,0)
        """
        obs.obstacles = [(0,0)]

        self.assertEqual(obs.get_obstacles(), [])

    
    def test_is_position_blocked(self):
        """
        Test correct obstacle detection and obstacle range
        """
        obs.obstacles = [(5,5)]

        self.assertEqual(obs.is_position_blocked(5,8), True)
        self.assertEqual(obs.is_position_blocked(5,5), True)
        self.assertEqual(obs.is_position_blocked(7,8), True)
        self.assertEqual(obs.is_position_blocked(4,8), False)
        self.assertEqual(obs.is_position_blocked(10,10), False)


    def test_is_path_blocked_true_basic(self):
        """
        Test correct return for blocked path:
        positive x and y
        """
        obs.obstacles = [(5,5)]

        self.assertEqual(obs.is_path_blocked(5,1,5,10), True)
        self.assertEqual(obs.is_path_blocked(1,5,10,5), True)
        self.assertEqual(obs.is_path_blocked(5,10,5,1), True)
        self.assertEqual(obs.is_path_blocked(10,5,1,5), True)


    def test_is_path_blocked_true_negative(self):
        """
        Test correct return for blocked path:
        negative y then x
        """
        obs.obstacles = [(5,5)]

        self.assertEqual(obs.is_path_blocked(5,-20,5,8), True)
        self.assertEqual(obs.is_path_blocked(-20,5,8,5), True)


    def test_is_path_blocked_false(self):
        """
        Test correct return for blocked path:
        no obstacle in path, Test corrrect range return
        """
        obs.obstacles = [(16,16)]

        self.assertEqual(obs.is_path_blocked(8,8,8,20), False)
        self.assertEqual(obs.is_path_blocked(10,11,10,20), False)