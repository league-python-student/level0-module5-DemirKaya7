"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle


if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    t = turtle.Turtle()
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    def drawSqare():
        for i in range(4):
            t.forward(100)
            t.left(90)

    def drawTriangle():
        for i in range(3):
            t.forward(100)
            t.left(120)

    def drawCircle():
        for i in range(360):
            t.forward(1)
            t.left(1)
    #   3. Ask the user for the for a shape to draw.
    shapeToDraw = simpledialog.askstring(title="Shape", prompt="What shape to draw?")
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    if shapeToDraw == "Square":
        drawSqare()
    elif shapeToDraw == "Triangle":
        drawTriangle()
    elif shapeToDraw == "Circle":
        drawCircle()
    else:
        print("Enter something else - Square, Triangle, or Circle")
