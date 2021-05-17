# Importing statement to make use of the code in collatz.py
from collatz import collatz_len
# Declaring variables
maxi = 1
number = 1
# Conditions
for i in range(1, 1000000):
    Length = collatz_len(i)
    if Length > maxi:
        maxi = Length
        number = i
    print('Longest chain:{}. Sequence length:{}.'.format(number, maxi))
    break
# Variable is set to "__main__"
if __name__ == "__main__":
    n = int(input('Enter a starting number: '))
    print(' Length of Collatz sequence:', collatz_len(n))
