import sys
import importlib
import import_helper

if len(sys.argv) > 2:
    if 'maze' in sys.argv[2]:
        obs = import_helper.dynamic_import('maze.{}'.format(sys.argv[2]))
    else:
        sys.argv.append('obstacles')
        obs = import_helper.dynamic_import('maze.obstacles')
else:
    sys.argv.append('obstacles')
    obs = import_helper.dynamic_import('maze.obstacles')        

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = obs.min_y, obs.max_y
min_x, max_x = obs.min_x, obs.max_x

grid = []

def maze_to_array(goal):
    """
    Converts maze to 2D array of 0 and "B" for obstacle
    1 for starting point, converts edge to goal x,y, 
    each cell represents 5x5 of the maze\n
    :args:
        str: edge to set as goal
    :Returns:
        list(list): 2D array representation of maze
        tuple: array y,x of goal/edge
    """
    edges = ["top","bottom","left","right"]

    if  goal.lower() not in edges or goal.lower() == "top":
        goal = (0,max_y)
    elif goal.lower() in edges and goal == "bottom":
        goal = (0,min_y)
    elif goal.lower() in edges and goal == "left":
        goal = (min_x,0)
    elif goal.lower() in edges and goal == "right":
        goal = (max_x,0)
    
    grid = [[ 0 for row in range(min_x,max_x+1)] for col in range(min_y,max_y+1)]
    set_goal = False
    
    for ind_y,val_y in enumerate(range(min_y,max_y+1)):
        for ind_x,val_x in enumerate(range(min_x,max_x+1)):
            if obs.is_position_blocked(val_x,val_y):
                grid[ind_y][ind_x] = "B"
            if (val_x,val_y) == (position_x,position_y):
                grid[ind_y][ind_x] = 1
            if (val_x,val_y) == goal and set_goal is False:
                goal = (ind_y, ind_x)
                set_goal = True
                
    return grid, goal


def solve_maze(edge):
    """
    breadth-first search hybrid binary tree search.
    adds 1 to each cell searched from current cell till
    goal has total number of steps, takes goal steps and 
    -1 step till back at start, appending y,x to path,
    Always returns shortest path.\n
    Args:
        edge (tuple): y,x of goal/edge\n
    Returns:
        list(tuple): movement direction, amount of steps moved
    """
    global grid

    grid, goal = maze_to_array(edge)
    step = 0

    while grid[goal[0]][goal[1]] == 0:
        step += 1
        find_path(step)

    i,j = goal[0], goal[1]
    step = grid[i][j]
    path = [(i, j)]
    
    while step > 1:
        if i > 0 and grid[i-1][j] == step-1:
            i, j = i-1, j
            path.append((i, j))
            step -=1
            
        elif j > 0 and grid[i][j - 1] == step-1:
            i, j = i, j-1
            path.append((i, j))
            step -=1
            
        elif i < (len(grid)-1) and grid[i + 1][j] == step-1:
            i, j = i+1, j
            path.append((i, j))
            step -=1
            
        elif j < (len(grid[i])-1) and grid[i][j + 1] == step-1:
            i, j = i, j+1
            path.append((i, j))
            step -= 1
    
    return x_y_to_direction(path)


def x_y_to_direction(path):
    """
    takes list(y,x) of path and converts to
    direction and amount of steps\n
    Args:
        path (list(tuple)): y,x of each step of solution\n
    Returns:
        list(list): (str)direction, (int)amount of steps
    """
    direction = []

    while len(path) > 1:
        y,x = path[-1]
        path.pop()
        y2,x2 = path[-1]

        if y < y2:
            if len(direction) > 0:
                if direction[-1][0] == "N":
                    direction[-1][1] += 1
                else:
                    direction.append(["N",1])
            else:
                direction.append(["N",1])

        if y > y2:
            if len(direction) > 0:
                if direction[-1][0] == "S":
                    direction[-1][1] +=1
                else:
                    direction.append(["S",1])
            else:
                direction.append(["S",1])

        if x < x2:
            if len(direction) > 0:
                if direction[-1][0] == "E":
                    direction[-1][1] +=1
                else:
                    direction.append(["E",1])
            else:
                direction.append(["E",1])

        if x > x2:
            if len(direction) > 0:
                if direction[-1][0] == "W":
                    direction[-1][1] += 1
                else:
                    direction.append(["W",1])
            else:
                direction.append(["W",1])
    
    return direction


def find_path(step):
    """
    takes current step and adds 1 to all valid
    neighboring cells.\n
    Args:
        step (int): number of steps
    """
    global grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == step:
                if i > 0 and grid[i-1][j] == 0 and grid[i-1][j] != "B":
                    grid[i-1][j] = step + 1
                if j > 0 and grid[i][j-1] == 0 and grid[i-1][j] != "B":
                    grid[i][j-1] = step + 1
                if i < (len(grid)-1) and grid[i+1][j] == 0 and grid[i-1][j] != "B":
                    grid[i+1][j] = step + 1
                if j < (len(grid[i])-1) and grid[i][j+1] == 0 and grid[i-1][j] != "B":
                    grid[i][j+1] = step + 1


def display_obstacles():
    """
    prints out obstacles if any
    """
    importlib.reload(obs)
    if obs.get_obstacles() != []:
        print("There are some obstacles:")
        for ob in obs.get_obstacles():
            print("- At position {0},{1} (to {2},{3})".format(ob[0], ob[1], ob[0] + 4, ob[1] + 4))


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: (tuple): True,0 if allowed, return false, 1 if blocked by obstacle
                        else false, 0 out of range
    """
    if obs.is_path_blocked(position_x,position_y,new_x,new_y):
        return (False, 1)
    return (min_x <= new_x <= max_x and min_y <= new_y <= max_y, 0)


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: (tuple): True,0 if allowed, return false, 1 if blocked by obstacle
                        else false, 0 out of range
    """
    global position_x, position_y

    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    is_allowed = is_position_allowed(new_x, new_y)

    if is_allowed[0]:
        position_x = new_x
        position_y = new_y
        return is_allowed
        
    return is_allowed

