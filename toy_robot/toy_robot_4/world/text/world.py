import importlib
import world.obstacles as obs

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


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

