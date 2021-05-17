'''Hilda Rocio Martin - 06/24/19 - Exercise 7.2 (calculator.py).
Write a small calculator that can compute arcsin, arccos, arctan and square root of a number.
Use math.sqrt(), math.asin(), math.acos(), and math.atan().'''
# import modulo
import math
# User Input for a function to calculate.
operation=input("What operation would you like compute? arcsin (a), arccos (c), arctan (t) or square root (s):")
# Conditions
if operation == 'a': # Selects the function.
    user_number = float(input("Enter a number between -1 to 1: ")) # Warns the user of the conditions for the function.
    if (user_number <= 1 and user_number >= -1):
        print("The arcsin of", user_number, "is: ", math.asin(user_number), "Radians") # It gives the answer in radians.
    else:
        print("The value you enter should be between -1 to 1") # Tells the user an invalid value was entered.
#The process repeats for one of the four options.
if operation == 'c':
    user_number = float(input("Enter a number between -1 to 1: "))
    if (user_number <= 1 and user_number >= -1):
        print("The arccos of", user_number, "is: ", math.acos(user_number),"Radians")
    else:
        print("The value you enter should be between -1 to 1")
if operation == 't':
    user_number = float(input("Enter a number: "))
    print("The arctan of", user_number, "is: ", math.atan(user_number), "Radians")

if operation == 's':
    user_number = float(input("Enter a non-negative number: "))
    if(user_number >= 0):
        print("The square root of", user_number, "is: ",math.sqrt(user_number))
    else:
        print("The value you enter should be non-negative")




