
'''Hilda Rocio Martin - 06/24/19 - Exercise 7.1 (shapes.py).
Write a program that prompts the user for either “circle” or “rectangle” or “square” then
reads in either the radius or width and height or the side length of the shape as floating point
numbers. If a radius is given, the program should print the shape’s circumference and area.
For a rectangle, print the perimeter and area.'''
#import modulo
import math
# User inputs
user_input = input("Enter circle, rectangle, or square: ")

# Conditions
if  user_input == 'circle': # Is the input is this shape it follows the conditions in this loop.
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2*math.pi*radius # Operation for circumference.
    area = math.pi*math.pow(radius,2) # Operation for area
    # Print the results
    print("The circumference of the circle is: ",circumference)
    print("The area of the circle is: ", area)
    raise SystemExit  # Exit
# Process repeats for the rest of the shapes
if  user_input == 'rectangle' :
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    perimeter = 2*(width+height)
    area = height*width
    print("The perimeter of the rectangle is: ", perimeter)
    print("The area of the rectangle is : ",area)
    raise SystemExit  # Exit
if  user_input == 'square':
    length = float(input("Enter the side length of the square: "))
    perimeter = 4*length
    area = math.pow(length,2)
    print("The perimeter of the square is: ", perimeter)
    print("The area of the square is : ", area)

    raise SystemExit # Exit
else: # If the user enters other than the requested shape names is displays a message.
    print("Shape not recognized")
