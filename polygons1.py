    # Hilda Rocio Martin - 06/13/19 - Exercise 7.3 (polygons.py).
    # Ask the user to enter a positive integer. Then consecutively draw shapes with 3, 4, 5, 6, and 7 sides
    # where the side length of each is the user’s input.

#Modulo
import turtle
from turtle import Turtle, Screen

# Program inputs
screen = Screen()
length = None
# This loop opens a gui that ask the user for input
while not length:
    length = screen.numinput("Select Length", "Enter side length no bigger than 100:", minval=1)


# Pick up the pen and go to that location then puts down the pen
turtle.penup()
turtle.goto(-6*length, 0) # This is the coordinates on the screen
turtle.pendown()

# Draw three sides(triangle)
for i in range(3):
  turtle.color('red') #color of the pen
  turtle.forward(length) #It moves forward the indicated length
  turtle.left(120) #The angle is 120 because 360/3 = 120

turtle.penup()
turtle.goto(-4.5*length, 0)
turtle.pendown()

# The process repeats for the rest of the shapes.
# Draw four sides(square)
for i in range(4):
  turtle.color('blue')
  turtle.forward(length)
  turtle.left(90)

turtle.penup()
turtle.goto(-3*length, 0)
turtle.pendown()

# Draw five sides(pentagon)
for i in range(5):
  turtle.color('yellow')
  turtle.forward(length)
  turtle.left(72)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Draw six sides(hexagon)
for i in range(6):
  turtle.color('green')
  turtle.forward(length)
  turtle.left(60)

turtle.penup()
turtle.goto(4*length, 0)
turtle.pendown()
# Draw seven sides(heptagon)
for i in range(7):
  turtle.color('purple')
  turtle.forward(length)
  turtle.left(51.4)

turtle.done()

