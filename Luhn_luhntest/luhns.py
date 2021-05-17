def validate(number):
    """Function called validate that takes in a card number and validates it.
    It should not print anything nor accept user input.
    """
    total = 0
    for i in range(len(number)):
        if i % 2 == 0:
            num = int(number[i]) * 2
            if num >= 10:
                total += (num // 10) + (num % 10)
            else:
                total += num
        else:
            total += int(number[i])
    # If total modulus 10 is equal to 0, the card is valid.
    return total % 10 == 0


def main():
    """the main function implements the validate function with Luhn’s
    Algorithm for validating credit cards.
    It asks the user to enter a credit card number and tell the
    user whether it is valid or not.
    """
    number = input('Enter a 16 digit credit card number: ')
    if validate(number):
        print(number + " is valid")
    else:
        print(number + " is invalid")
# Calling main.
if __name__ == "__main__":
        main()
