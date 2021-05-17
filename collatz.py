# Determining the length of one sequence
def collatz_len(n):
    # Variables
    lon = 0
    # Conditions in the loop
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        lon = lon + 1
    return lon + 1
# Variable is set to "__main__"
if __name__ == "__main__":
    n = int(input('Enter a starting number: '))
    print('Length of Collatz sequence:', collatz_len(n))
