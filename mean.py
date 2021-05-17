    # Hilda Rocio Martin - 06/13/19 - Exercise 7.2 (mean.py).
    # Write a program that accepts 10 ﬂoating point numbers from the user
    # and prints the running average after each number is entered.

# Print a statement for the user to read and follow
print("Enter ten numbers to calculate their average. Enter 0 to stop: ")
# Declaring variables
count = 0
sum = 0.0
number = 1
# This is the loop where the user is asked to enter ten numbers and stops when the users enters 0
while number != 0:#It checks if the value on the left of the operator is not equal to the one on the right
    number = float(input("Enter a number: ")) # User's input and converts the users input into a float number
    sum = sum + number # Adds the user's input
    count = count + 1 # Adds and assigns

if count == 0: # Conditions
    print("Enter a number")
else:
    print("Average of the numbers you entered is: ", sum / (count - 1)) # String and average calculation

    # Live Run
    # (base) C:\Users\hilda\.PyCharmCE2019.1\config\scratches>python3 _mean.py
    # Enter ten numbers to calculate their average value. Enter 0 to stop:
    # Enter a number: 23
    # Enter a number: 7.8
    # Enter a number: 89.03
    # Enter a number: 6.45
    # Enter a number: 7.2
    # Enter a number: 9
    # Enter a number: 5
    # Enter a number: 3
    # Enter a number: 111.055
    # Enter a number: 44
    # Enter a number: 0
    # Average of the numbers you entered is:  30.553499999999996