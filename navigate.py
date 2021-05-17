# Import modulo
import turtle
myTurtle = turtle.Turtle()
# Loop with definitions, identifiers, and parameters
while True:
    # Prompt user for degrees to moved to the left
    def left():
        degrees = input('Enter the degrees:')
        myTurtle.left(int(degrees))
    # Prompt user for degrees to moved to the right

    def right():
        degrees = input('Enter the degrees:')
        myTurtle.right(int(degrees))
    # Draw a line length 100

    def forward():
        myTurtle.forward(100)

    # Stop the program
    def stop():
        print('Stopping the program')
    # Enter a choice
    choice = input("Enter directions- left, right, forward, or stop:")
    print("choice:", choice)
    # Conditions
    if choice == "left":
        left()
    elif choice == "right":
        right()
    elif choice == "forward":
        forward()
    elif choice == "stop":
        stop()
        raise SystemExit
    # An unidentified entry will exit the program
    if choice not in ("left", "right", "forward", "stop", int):
        print('Invalid entry - start over')
        raise SystemExit
