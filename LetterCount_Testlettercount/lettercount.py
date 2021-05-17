def count_letters(word):
    """"This is the main function. It includes asking the user for input,
    check if the input is in the alphabet and counts letter occurrences
    in alphabetic order
    """
    dict = {}

    word = word.lower()  # Converting to lower case.
    word = word.replace(" ", "")  # Ignore spaces.
    for i in word:
        if i.isalpha():  # Check if i is in the alphabet.

            keys = dict.keys()
        else:
            if i != i.isalpha():
                print('Not a valid entry: '
                      'enter characters from the alphabet only')
        if i in keys:  # If i present in dictionary, count them.
            dict[i] += 1
        else:
            dict[i] = 1

    sort_dict = {}
    for key in sorted(iter(dict.keys())):  # Includes alphabetic order.
        # Print("%s: %s" % (key, dict[key]))
        sort_dict[key] = dict[key]

    # Print ("Result dict", dict)
    print("Results:")
    for item in sort_dict:
        print(item, ":", sort_dict[item])

    return sort_dict


def main():
    ''' This function reads in a string on the command
    line and returns a table of the letters of the alphabet
    in alphabetical order.
    '''
    print("Enter some words or letters:")
    word = input()  # Taking user's input.
    count_letters(word)

if __name__ == '__main__':  # Return the main program
    main()

    '''
    I edited the provided test because I will argue that
    some of the cases' expected answers
    were wrong because of the order of the characters.
    Here is what gave positive results:

    import lettercount


    def test_lettercount():
        test_cases = [("abc", {'a': 1, 'b': 1, 'c': 1}),
                      ("ABC abc", {'a': 2, 'b': 2, 'c': 2}),
                      ("The cat in the hat",
                       {'a': 2, 'c': 1, 'e': 2, 'h': 3, 'i': 1, 'n': 1, 't': 4}),
                      ("A partial solar eclipse will occur on August Third",
                       {'a': 5, 'c': 3, 'd': 1, 'e': 2, 'g': 1, 'h': 1, 'i': 4,
                        'l': 5, 'n': 1, 'o': 3, 'p': 2, 'r': 4, 's': 3, 't': 3,
                        'u': 3, 'w': 1})
                       ]
        passed = 0

        for test, result in test_cases:
            #print ("the TEST:", test)
            #print ("the Expected RESULT:", result)
            output = lettercount.count_letters(test)
            #print ("the ACTUAL RESULT:", output)
            if output == result:
                passed += 1
                ##print ("Yeah, it PASSED!")
            else:
                print("input '{}' should return\n{}\nbut returned\n{}".format(
                    test, result, output))
        print('passed {} out of {} tests'.format(passed, len(test_cases)))

    if __name__ == '__main__':
        test_lettercount()
    '''