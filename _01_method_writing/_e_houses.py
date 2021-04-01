"""
Have the turtle draw a row of houses.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle
import random

def draw_house(height):
    turt.pendown()
    turt.left(90)
    if height == "small":
        h = 60
    elif height == "medium":
        h = 120
    elif height == "large":
        h = 250
    turt.forward(h)
    turt.left(90)
    if height == "large":
        draw_flat_roof()
    else:
        draw_pointy_roof()
    turt.forward(h)
    turt.left(90)
    turt.forward(100)

    turt.color("green")
    turt.width(15)
    turt.forward(100)
    turt.penup()
    turt.color("black")
    turt.width(1)

def draw_pointy_roof():
    turt.right(45)
    turt.forward(70.7106782)
    turt.left(90)
    turt.forward(70.7106782)
    turt.left(45)

def draw_flat_roof():
    turt.forward(100)
    turt.left(90)

if __name__ == '__main__':
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.

    turt = turtle.Turtle()
    turt.penup()
    turt.goto(-250, -250)
    turt.pendown()

    for i in range(4):
        draw_house(height="medium")
        turt.forward(100)

