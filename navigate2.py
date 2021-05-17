# Import modulo.
import turtle
myTurtle = turtle.Turtle()


def left(degrees):  # Prompt user for degrees to moved to the left.
    myTurtle.left(int(degrees))


def right(degrees):  # Prompt user for degrees to moved to the right.
    myTurtle.right(int(degrees))


def forward(amount):  # Draw a line with a length.
    myTurtle.forward(amount)


def stop():  # Stop the program.
    print('Stopping the program')

my_list = []
choice = "waiting"
while choice != "stop":  # Loop.
    # Enter a choice.
    choice = input("Enter directions- left, right, forward, or stop:")
    print("choice:", choice)
    if choice == "left" or choice == "right":
        degrees = input('Enter the degrees:')
        choice = choice + ":" + str(degrees)
    elif choice == "forward":
        length = input('Enter the length:')
        choice = choice + ":" + str(length)
    elif choice == "stop":
        print("Stopping list entry")
    my_list.append(choice)
print("The List:", my_list)

for i in range(len(my_list)):  # Conditions.
    entry = my_list[i]
    parts = entry.split(":")
    print(parts)
    if len(parts) > 1:
        action = parts[0]
        amount = int(parts[1])
        if action == "left":
            left(amount)
        elif action == "right":
            right(amount)
        elif action == "forward":
            forward(amount)
    else:
        print("ALL DONE!", my_list)  # Draw the lines.
