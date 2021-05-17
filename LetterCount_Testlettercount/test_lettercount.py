"""
This test assumes your function is named `count_letters`.
This function must take a string and return a dictionary.
"""

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