    #Hilda Rocio Martin - 06/13/19 - Exercise 7.4 (spiral.py).
    # Write a script that asks the user to enter an angle. Then use turtle to draw 128 lines, each line is separated by the given angle
    # and each line is slightly bigger than the last.
#modulo
import turtle
from turtle import Turtle, Screen
# Program inputs
screen = Screen()
angle = None
# This loop opens a gui that ask the user for input
while not angle:
    angle = screen.numinput('Select Angle', 'Enter an angle:', minval=1)
# declaring objects
obj=turtle.Turtle()
obj.speed(50)

# Function to draw the spiral at a given angle
def drawspiral():
    for x in range(128): # The program draws 128 lines
        obj.forward(x) # Moves the object forward
        obj.right(angle) # To the right at an angle

drawspiral()
turtle.done()
