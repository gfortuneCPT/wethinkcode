# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ")
    shape =shape.lower()
    shape_selection  = ["pyramid", "square", "triangle", "diamond", "paralellogram", "rectangle"]

    while shape not in shape_selection:
        shape = input("Shape?: ")
    
    return shape


# TODO: Step 1 - get height (it must be int!)
def get_height():
    
    while True:
        try:
            height = input("Height?: ")
            height = int(height)
            break
        except ValueError:
            return get_height()
            
    if height < 0 or height > 80:
        return get_height()
    else:   
        return height
        

# TODO: Step 2
def draw_pyramid(height, outline):
    if outline != True:
        for i in range(1, height + 1):
            print(" " * (height - i) + "*" * i + "*" * (i-1))
    else:
        for i in range(1, height + 1):
            if i == 1:
                print(" " * ((height - i)) + "*")
            elif i == (height):
                print(" " * (height -1 - i) + "*" * i + "*" * (i-1))
            else:    
                print(" " * (height - i) + "*" + " " * (i-1) + " " * (i-2) + "*")


# TODO: Step 3
def draw_square(height, outline):
    if outline != True:
        for i in range(height):
            print("*" * height)
    else:
        for i in range(height):
            if i == 0:
                print("*" * height)
            elif i == (height)-1:
                print("*" * height)
            else:
                print("*" + " " * (height-2) + "*")


# TODO: Step 4
def draw_triangle(height, outline):
    if outline != True:
        for i in range(1, height + 1):
            print("*" * i)
    else:
        for i in range(1,height+1):
            if i == 1:
                print("*" * 1)
            elif i == height:
                print("*" * i)
            else:
                print("*" + " " * (i-2) + "*")


def draw_diamond(height, outline):
    if outline != True:

        for i in range(1, height + 1):
            print(" " * (height - i) + "*" * i + "*" * (i-1))
        i = height -1
        
        while i > 0:
            print(" " * (height - i) + "*" * i +  "*" * (i-1))
            i -= 1
    else:

        for i in range(1, ((height//2) + 1)):
            if i == 1:
                print(" " * (height - i) + "*")
            else:    
                print(" " * (height - i) + "*" + " " * (i-1) + " " * (i-2) + "*")
        i = (height//2) -1

        while i > 0:
            if i == 1:
                print(" " * (height - i) + "*")
            else:    
                print(" " * (height - i) + "*" + " " * (i-1) + " " * (i-2) + "*")
            i -=1

def draw_parallelogram(height, outline):
    if outline != True:
        for i in range(height):
            print(" " * (height-i) + "*" * (height*2))
    else:
        for i in range(height):
            if i == 0:
                print(" " * (height-i) + "*" * (height*2))
            elif i == (height)-1:
                print(" " * (height-i) + "*" * (height*2))
            else:
                print(" " * (height-i) + "*" + " " * ((height*2)-2) + "*")

def draw_rectangle(height, outline):
    if outline != True:
        for i in range(height):
            print("*" * (height*4))
    else:
        for i in range(height):
            if i == 0:
                print("*" * (height*4))
            elif i == (height)-1:
                print("*" * (height*4))
            else:
                print("*" + " " * ((height*4)-2) + "*")

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "diamond":
        draw_diamond(height, outline)
    elif shape == "paralellogram":
        draw_parallelogram(height, outline)
    elif shape == "rectangle":
        draw_rectangle(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (Y/N):")
    if  outline == "y" or outline == "Y":
        return True
    else:
        return False

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

