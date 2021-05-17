'''Hilda Rocio Martin - 06/24/19 - Exercise 7.3 (polygons2.py).
Write a program that takes in an integer. If the integer is less than 3, print a message and exit.
Otherwise, draw a shape with as many sides as the user’s input.'''

 # Import modulo
import turtle
from turtle import Turtle, Screen

# Program inputs
screen = Screen()
sides = None
length = None
error = None
# This loop opens a gui that ask the user for input.
while not sides:
    sides = screen.numinput('Select Number of Sides', 'Enter the number of sides to draw a polygon', minval=1)
# If the input is smaller than 3 it warns the user and exit the screen.
if sides < 3:
    error =screen.numinput('Select Number of Sides', 'Invalid number of sides, click "Cancel"', minval= 1 )
    raise SystemExit  # Exit

while not length: # A warning is included in case of the length is too long for the size of the screen.
    length = screen.numinput("Select Length", "Enter side length "
                            "\n(If the length is bigger than 100 and the sides more than 8, it might not fit the screen):"
                             , minval=1)


# Draw the shape with the number of sides from the user.
for i in range(int(sides)):
  turtle.color('red') #color of the pen.
  turtle.forward(length) #It moves forward the indicated length.
  turtle.left(360/sides) # To the left at an angle.


turtle.done()
