
# TODO: Decompose into functions
from typing import Sized

#Square
def move_square(size):
    """
    Prints moves to create a aquare of int(size)
    Args:
        size (int): Integer for size of square
    """

    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


def move_rectangle(length,width):
    """
    Prints moves to create rectangle of n length and n width
    Args:
        length (int): length of rectangle
        width (int): width of rectangle
    """

    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_circle(degrees,length):
    """
    Prints moves to create a circle
    Args:
        degrees (int): degrees of turn should be 1 degree
        length (int): forward move length should be 1
    """

    print("Moving in a circle")
    for i in range(360):
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")


def square_dancing(size):
    """
    Prints square dancing pattern
    Args:
        size (int): Size of each square
    """

    print("Square dancing - 3 squares of size {}".format(size))
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        move_square(size)


def move_crop_circles():
    """
    Prints 4 circles to form a crop circle
    """

    length = 20
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle(1,1)


# def do_dance: "Does all moves and combination moves"
def move():
    move_square(10)
    move_rectangle(20,10)
    move_circle(1,1)
    square_dancing(20)
    move_crop_circles()


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
