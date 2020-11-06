# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------

import random

min_y, max_y = -50, 50
min_x, max_x = -25, 25

#   list of obstacles
obstacles = [(random.randint(min_x, max_x), random.randint(min_y, max_y)) 
            for i in range(random.randint(0,10))]


def get_obstacles():
    """
    gets list of obstacles, removes (0,0) obstacle/starting point, removes duplicate obstacles
    Returns:
        list: list of obstacles 
    """
    global obstacles

    if (0,0) in obstacles:
        return [ob for ob in obstacles if ob != (0,0)]

    return list(dict.fromkeys(obstacles))


def is_position_blocked(x,y):
    """
    checks if x,y is in same range as and x,y of an obstacle +4x and y
    Args:
        x (int): position value x
        y (int): position value y
    Returns:
        bool: True, if x,y is in range and False if not
    """
    global obstacles

    for obs in obstacles:

        if x in range(obs[0], obs[0]+5) and y in range(obs[1], obs[1]+5):
            return True

    return False


def is_path_blocked(x1,y1, x2, y2):
    """
    checks for each value in range x1,y1 -> x2,y2, if an obstacle is that range
    swops x,x2 if x1 larger than x2 for acurate range() useage
    Args:
        x1 (int): start x value
        y1 (int): start y value
        x2 (int): destination x value
        y2 (int): destination y value
    Returns:
        bool: True if path is blocked by an obstacle else False
    """
    global obstacles

    if x1 == x2:
        for i in range(min(y1, y2),(max(y1,y2)+1)):
            if is_position_blocked(x2, i):
                return True
    elif y1 == y2:
        for i in range(min(x1,x2),(max(x2,x1)+1)):
            if is_position_blocked(i, y2):
                return True
    return False