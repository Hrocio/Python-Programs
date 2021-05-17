def word_palindrome(word):
    '''Function which return reverse of a string. It also works with numbers.
    any string containing just one letter is by default a palindrome.
    '''
    if len(word) < 2:  # Can be less than 2.
        return True
    if word[0] != word[-1]:  # Comparing input string with the reverse string.
        return False
    return word_palindrome(word[1:-1])


def main():
    '''This function determines whether the user's input is a palindrome.
    the string is taken as an input, reversed, and then tested.
    '''
    user_input = (input("Enter a word: "))
    # It ignores if its uppercase or lowercase.
    if word_palindrome(user_input.upper()) == 1:
            print(user_input, 'is a palindrome')
    else:
            print(user_input, 'is not a palindrome')

if __name__ == '__main__':  # Main.
        main()
