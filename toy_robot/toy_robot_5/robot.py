import sys

# show obstacles and world objects
if len(sys.argv) > 1 and sys.argv[1] == "turtle":
    import world.turtle.world as world
else:
    import world.text.world as world


# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right',
                 'left', 'sprint', 'replay', 'silent', 'reversed', 'mazerun']

# command history
history = []

#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.

def add_to_history(command):
    """Appends valid commands to the list history
    :Args:
        command (str): string entered as command
    """
    global history
    valid_list = ['forward', 'right', 'back', 'left', 'sprint']
    command_list = split_command_input(command)
    
    if command_list[0] in valid_list:
        history.append(command.lower())
    

def replay(robot_name, flag):
    """Replays commands from history with args
    :Args:
        robot_name (str): robot name 
        flag (str): Flags for options. str(silent),str(reversed) and range(int seperated with "-")
    :Returns:
        Bool:  + Output to print flags used
    """
    
    flag_list = flag.split(" ")
    int_in_flags = "".join([element for element in flag_list if is_int(element)])
    range_in_flags = [element for element in flag_list if element.count("-") == 1]
    
    changed_history = history[:]
    reverse = False
    message = ""
    num_commands = len(history)

    if "silent" in flag_list and "reversed" in flag_list:
        flag = True
        reverse = True
        message = " in reverse silently"
    elif "silent" in flag_list:
        flag = True
        message = " silently"
    elif "reversed" in flag_list:
        reverse = True
        changed_history = history[::-1]
        message = " in reverse"
        
    if not int_in_flags and len(range_in_flags) > 0:
        range_in_flags = range_in_flags[0].split("-")
        changed_history = changed_history[int("-"+range_in_flags[0]):int("-"+range_in_flags[1])]
        num_commands = len(changed_history)
    if not range_in_flags and len(int_in_flags) > 0:
        changed_history = changed_history[int("-"+int_in_flags):]
        num_commands = len(changed_history)

    if reverse == False:
        [handle_command(robot_name,i,flag) for i in changed_history]
    else:
        [handle_command(robot_name,i,flag) for i in changed_history]
    
    return True, " > {0} replayed {1} commands{2}.".format(robot_name, num_commands, message)


def mazerunner(robot_name, edge="top"):
    """
    takes steps to solve maze and converts to movement commands
    if no edge is specified
    default="top"\n
    :Args:
        robot_name (str): name of robot
        edge (str, optional): specify edge to run to. Defaults to "top".\n
    :Returns:
        Bool, str: True, message to print out on competion
    """
    output(robot_name,"starting maze run..")
    
    compass = ["N", "E", "S", "W"]
    path = world.solve_maze(edge)
    
    if not edge:
        edge = "top"

    for move in path:
        # Check direction before forward movement
        while compass[world.current_direction_index] != move[0]:
            # Left and Right decision logic
            if (compass.index(move[0])) < world.current_direction_index:
                handle_command(robot_name, "left")
            elif (compass.index(move[0])) > world.current_direction_index:
                handle_command(robot_name, "right")
        # Moves forward 
        handle_command(robot_name,"forward {}".format(move[1]))

    return True, "{0}: I am at the {1} edge.".format(robot_name, edge)


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """
    global history
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)
    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_flags(flag):
    """
    Returns True if args in command is valid flags for replay func
    parses flags for int for range seperated by "-", valid silent and revesed flags
    Args:
        flag (str): flags and range to be passed to replay
    Returns:
        bool: True if range is valid and within history range, True if flags have correct syntax
        else: False
    """
    valid_flag = ["silent", "reversed", "reversed silent", "top", "bottom", "left", "right"]
    flag_list = flag.split(" ")
    int_in_flags = "".join([element for element in flag_list if is_int(element)])
    range_in_flags = [element for element in flag_list if element.count("-") == 1]
    
    if not int_in_flags and len(range_in_flags) > 0:
        range_in_flags = range_in_flags[0].split("-")
        if int(range_in_flags[0]) > int(range_in_flags[1]) and int(range_in_flags[0]) <= len(history):
            return True
    
    if not range_in_flags and len(int_in_flags) > 0:
        if int(int_in_flags) <= len(history):
            return True
    
    if  flag in valid_flag:
        return True
    
    return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    (command_name, arg1) = split_command_input(command.lower())
    valid_list = ['forward', 'back', 'sprint']
    if command_name in valid_list and arg1 == "":
        return False
    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1) or valid_flags(arg1))


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replay previous commands, use flags and range
MAZERUN - solves maze to specified edge
"""

def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    is_allowed = world.update_position(steps)

    if is_allowed[0]:
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        if is_allowed[1] == 0:
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
        else:
            return True, ''+robot_name+': Sorry, there is an obstacle in the way.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    is_allowed = world.update_position(-steps)

    if is_allowed[0]:
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        if is_allowed[1] == 0:
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
        else:
            return True, ''+robot_name+': Sorry, there is an obstacle in the way.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    
    world.current_direction_index += 1
    if world.current_direction_index > 3:
        world.current_direction_index = 0
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    
    world.current_direction_index -= 1
    if world.current_direction_index < 0:
       world.current_direction_index = 3
    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """
    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def handle_command(robot_name, command, flag=False):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    (command_name, arg) = split_command_input(command)
    
    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command_name == 'replay':
        (do_next, command_output) = replay(robot_name, arg)
    elif command_name == 'mazerun':
        (do_next, command_output) = mazerunner(robot_name, arg)

    if flag != True:
        print(command_output)
        world.show_position(robot_name)
    return do_next


def robot_start():
    """This is the entry point for starting my robot"""
    global history
    
    history = []
    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    output(robot_name, "Loaded {}.".format(sys.argv[-1]))

    world.position_x = 0
    world.position_y = 0
    world.current_direction_index = 0

    world.display_obstacles()

    command = get_command(robot_name)
    add_to_history(command)
   
    while handle_command(robot_name, command):
        command = get_command(robot_name)
        add_to_history(command)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()