# User inputs
positive_int = input('Enter positive integer: ')
user_input = int(positive_int)
# Conditions
if user_input < 0:
    print('Not a positive number!')
i = 0
# Loop to determine if number is divisible by 3, 5, or noth
while i >= 0:
    for i in range(1, user_input + 1):

        if (i % 5) == 0 and (i % 3) == 0:
            result = 'FizzBuzz'
            print(i, '{}'.format(result))
            i = i + 1

        elif (i % 3) == 0:
            result = 'Fizz'
            print(i, '{}'.format(result))
            i = i + 1

        elif (i % 5) == 0:
            result = 'Buzz'
            print(i, '{}'.format(result))
            i = i + 1

        else:
            print(i)
            i = i + 1
    break
