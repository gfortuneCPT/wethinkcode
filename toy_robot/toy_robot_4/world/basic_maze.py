import random
from random import randint

min_y, max_y = -100, 100
min_x, max_x = -50, 50


"""
Psuedo Algorithm
1. Start at the NE cell
2. Add the current cell to the run set
3. Randomly chose to continue east, or stop
4. If you continue east
    - Remove the edge between the current cell and the cell to the east. The is the current cell now.
    - Go to 2
5. Else
    - Choose a cell in the run set and remove an edge to the north
    - Remove all cells from the run set
    - The next cell in the row becomes the current cell
    - Go to 2.
6. Continue until all rows are complete
"""

def generate_maze_grid():
    """
    docstring
    """
    grid = []
    for y in range(min_y,max_y+1,5):
        for x in range(min_x,max_x,5):
            grid.append((x,y))
    return grid


def generate_maze():
    """
    docstring
    """
    remove_obs = [(-5, 0), (0, 0), (5, 0)]
    run = []

    grid = [obs for obs in generate_maze_grid() if obs[1] != max_y]
    
    cell = (min_x, max_y-10)

    y_range = range(min_y, max_y-9,10)
    y_range = y_range[::-1]
    n_or_e = [5,0]

    for y in y_range:
        for x in range(min_x, max_x):
            cell = (x,y)
            run.append(cell)
            if random.choice(n_or_e) != 5:
                remove_obs.append((x+5,y))
            else:
                north = random.choice(run)
                north = (north[0],north[1]+5)
                remove_obs.append(north)
                # north = (north[0]-5,north[1]+5)
                # remove_obs.append(north)
                north = (north[0]+5,north[1])
                remove_obs.append(north)
                
                run.clear()

    return [obs for obs in grid if obs not in remove_obs]



def get_obstacles():
    """
    gets list of obstacles, removes (0,0) obstacle/starting point, removes duplicate obstacles
    Returns:
        list: list of obstacles 
    """
    global obstacles

    if (0,0) in obstacles:
        return [ob for ob in obstacles if ob != (0,0)]
    print(obstacles)
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

        if x in range(obs[0], obs[0]+4) and y in range(obs[1], obs[1]+4):
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

obstacles = generate_maze()
