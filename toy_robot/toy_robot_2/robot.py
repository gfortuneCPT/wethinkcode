def get_name():
    """Get Input for Robot Name"""
    return input("What do you want to name your robot? ")


def greeting():
    """Prints Greeting followed by robot name"""
    print("{}: Hello kiddo!".format(r_name))


def switch_off():
    """Shutdown message"""
    print("{}: Shutting down..".format(r_name))


def get_input():
    """Get command input"""
    return input("{}: What must I do next? ".format(r_name))


def check_in_list(com, com_list):
    """Check if command is in list of commands
    Args:
        com (str): command
        com_list (list): list of valid commands
    Returns:
        bool: True, if in list else False
    """
    if  com.lower() not in com_list:
        return False
    else:
        return True


def help_list():
    """Returns each command and information on each command"""
    help_dict = {"off " : "Shut down robot", 
                 "help" : "provide information about commands",
                 "forward" : "Move n steps forward, 'forward n'",
                 "back" : "Move n steps backwards, 'back n'",
                 "right" : "Rotate right 90 degrees",
                 "left" : "Rotate left 90 degrees",
                 "sprint" : "Move n+(n-1) steps forwards"}
                 
    out = "I can understand these commands:\n"
    for i in help_dict:
        out +="{} - {}\n".format(i.upper(), help_dict.get(i))
    return out


def change_position(pos,command):
    """Takes current position and command, changes x or y
       depending on current direction. Returns list with x,y,direction"""
    x = pos[0]
    y = pos[1]
    direction = pos[2]
    if  command[0] == "forward" or command[0] == "sprint":
        if direction == 90:
            y += int(command[1])
        elif direction == 180:
            x -= int(command[1])
        elif direction == 270:
            y -= int(command[1])
        elif direction == 0 or direction == 360:
            x += int(command[1])
    return  [x,y,direction]


def change_position_back(pos,command):
    """Takes current position and command, changes x or y
       depending on current direction. Returns list with x,y,direction"""
    x = pos[0]
    y = pos[1]
    direction = pos[2]

    if direction == 90:
        y -= int(command[1])
    elif direction == 180:
        x += int(command[1])
    elif direction == 270:
        y += int(command[1])
    elif direction == 0 or direction == 360:
        x -= int(command[1])
    return  [x,y,direction]


def change_direction(pos, command):
    """Takes current position (list x,y,direction) and command as arguments
        if command is left or right function returns the new direction in degrees"""
    direction = pos[2]
    if command == "right":
        direction -= 90
        if direction < 0:
            direction = 270
    elif command == "left":
        direction += 90
        if direction > 360:
            direction = 90
    return direction


def move(com):
    """Takes in the command and splits it to a list where the first ellemnet is the command
        and the next element is the amount of steps to move. returns the list"""
    move = com.lower().split(sep=" ")
    return  move


def move_is_valid(position, movement):
    """Returns true of false if the move will be out of the safe zone"""
    position = change_position(position,movement)
    if  -100 < position[0] < 100 and -200 < position[1] < 200:
        return True
    else:
        return False


def sprint(steps, position):
    """Takes in integer of steps, current position, and prints
        each step for the amount of steps. Returns new position"""
    for i in range(steps):
        position = change_position(position,["forward",steps-i])
        print(" > {} moved forward by {} steps.".format(r_name,(steps-i)))
    return position


r_name = ""
def robot_start():
    """This is the entry function, do not change"""
    state = True
    position = [0,0,90]
    com_list = ["off", "help", "forward", "right", "left", "sprint"]
    global r_name

    r_name = get_name()
    greeting()

    while state == True:
        com = get_input()
        if "forward" in com.lower().split(sep=" "):
            movement = move(com)
            if  move_is_valid(position, movement) == True:
                position = change_position(position,movement)
                print(" > {} moved {} by {} steps.".format(r_name,movement[0],movement[1]))
            else:
                print("{}: Sorry, I cannot go outside my safe zone.".format(r_name))
            print(" > {} now at position ({},{}).".format(r_name,position[0],position[1]))
            
        elif "sprint" in com.split(sep=" "):
            movement = move(com)
            if  move_is_valid(position, movement) == True:
                position = sprint(int(movement[1]),position)
            else:
                print("{}: Sorry, I cannot go outside my safe zone.".format(r_name))
            print(" > {} now at position ({},{}).".format(r_name,position[0],position[1]))
        
        elif "back" in com.lower().split(sep=" "):
            movement = move(com)
            if  move_is_valid(position, movement) == True:
                position = change_position_back(position,movement)
                print(" > {} moved {} by {} steps.".format(r_name,movement[0],movement[1]))
            else:
                print("{}: Sorry, I cannot go outside my safe zone.".format(r_name))
            print(" > {} now at position ({},{}).".format(r_name,position[0],position[1]))
            
        elif check_in_list(com.lower(), com_list) == False:
            print("{}: Sorry, I did not understand '{}'.".format(r_name,com))

        elif com.lower() == "right" or com.lower() == "left":
            movement = com.lower()
            print(" > {} turned {}.".format(r_name,movement))
            position[2] = change_direction(position,movement)
            print(" > {} now at position ({},{}).".format(r_name,position[0],position[1]))

        elif com.lower() == "off":
            switch_off()
            state = False

        elif com.lower()  == "help":
            print(help_list())
    pass


if __name__ == "__main__":
    robot_start()
