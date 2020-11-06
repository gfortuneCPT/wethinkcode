import turtle
import tkinter as tk
import importlib
from turtle import pen
import world.basic_maze as obs

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# initial position and state
s = turtle.Screen()
s.setworldcoordinates(min_x-125,min_y-25,max_x+125,max_y+25)
t = turtle.Turtle()
t.pen(fillcolor="red", pencolor="blue", pensize=3, speed=10)
t.shapesize(1.5, 1.5, 1)
t.setheading(90)

# reload obstacles
importlib.reload(obs)


def change_direction():
    """
    change turtle direction, update facing direction on screen
    """
    if directions[current_direction_index] == 'forward':
        t.setheading(90)
    elif directions[current_direction_index] == 'right':
        t.setheading(0)
    elif directions[current_direction_index] == 'back':
        t.setheading(270)
    elif directions[current_direction_index] == 'left':
        t.setheading(180)


def draw_border():
    """
    draw red border representing max and min of world
    """
    border = turtle.Turtle(visible=False)
    border.pen(fillcolor="red", pencolor="red", pensize=5, speed=0)
    border.penup()
    border.goto(min_x, min_y)
    border.pendown()
    border.goto(min_x, max_y)
    border.goto(max_x,max_y)
    border.goto(max_x,min_y)
    border.goto(min_x,min_y)


def display_obstacles():
    """
    draws obstacles on to screen, if any
    """
    importlib.reload(obs)
    if obs.get_obstacles() != []:
        obstacles = obs.get_obstacles()
        for ob in obstacles:
            
            border = turtle.Turtle(visible=False)
            border.pen(fillcolor="red", pencolor="red", pensize=1, speed=0)
            border.penup()
            border.goto(ob[0], ob[1])
            border.pendown()
            border.begin_fill()
            border.goto(ob[0], (ob[1]+4))
            border.goto((ob[0]+4), (ob[1]+4))
            border.goto((ob[0]+4), ob[1])
            border.goto(ob[0], ob[1])
            border.end_fill()

 
def show_position(robot_name):
    """
    Updates position on screen
    Args:
        robot_name (str): Robot Name
    """
    t.goto(position_x, position_y)
    change_direction()


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit or blocked
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    if obs.is_path_blocked(position_x,position_y,new_x,new_y):
        return (False, 1)
    return (min_x <= new_x <= max_x and min_y <= new_y <= max_y, 0)


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps: (int): number of steps
    :return: True if the position was updated, else False
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

# draw border on import
draw_border()