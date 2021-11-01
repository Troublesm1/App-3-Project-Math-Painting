from canvas import Canvas
from shapes import Rectangle, Square

#Get canvas width and height from the user interface
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(int(input("Enter canvas height: "))

#Make a dictionary of color codes and prompt for color
colors = {"white": (255,255,255), "black" : (0,0,0)}
canvas_color = input("Enter canvas color (white or black): ")

#Create a canvas with the user data
canvas = Canvas(canvas_width=width, canvas_height=height, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw? Enter quit to quit. ")
    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type .lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green should the rectangle have? "))
        blue = int(input("How much blue should the rectangle have? "))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)
