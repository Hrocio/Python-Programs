def all_have_value(lst):  # Test values in the list.
    for value in lst:
        if value == '-':
            return False
    return True


def all_equal(lst):  # Test equal values.
    take_value = lst[0]
    for value in lst:
        if value == '-' or value != take_value:
            return False
    return True


def select_row(array, row):  # Select a row.
    return array[row]


def select_col(array, col):  # Select column.
    column = []
    for row in array:
        column.append(row[col])
    return column


def run_tests():  # Test each function defined in this module.
    passed = 0
    failed = 0
    tests = [
        (all_have_value, [1, 2, 3, 4, 5], True),
        (all_have_value, ['c', 'a', 't'], True),
        (all_have_value, ['-', '-'], False),
        (all_equal, [1, 1, 1, 1, 1], True),
        (all_equal, ['-', '-'], False),
        (all_equal, ['python', 'python'], True),
        (select_row, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [4, 5, 6]),
        (select_row, [[1, 1, 3], [1, 1, 4]], 0, [1, 1, 3]),
        (select_row, [[1], [2], [3], [4]], 3, [4]),
        (select_col, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, [1, 4, 7]),
        (select_col, [[1, 1, 3], [1, 1, 3]], 2, [3, 3]),
        (select_col, [[5, 4, 3, 2, 1]], 3, [2])
            ]
    # Detailed error message whenever a function fails a test.
    counter = 0
    for test in tests:
        if len(test) == 4:
            f = (test[0])
            result = f(test[1], test[2])
            expected = test[3]
            counter += 1
            print("on# ", counter, ", result = ", result, ", expected = ",
                  expected)
            if result == expected:
                passed += 1
            else:
                failed += 1
                # f.__name__ is the function's name
                # Select_row.__name__ is the string "select_row"
                print("Function {}, argument {}, {}".format(f.__name__,
                                                            test[1], test[2]))
                print("Expect {}, return {}".format(expected, result))
        else:
            f = (test[0])
            result = f(test[1])
            expected = test[2]
            counter += 1
            print("on # ", counter, ", result = ", result, ", expected = ",
                  expected)
            if result == expected:
                passed += 1
            else:
                failed += 1
                # f.__name__ is the function's name
                # for example, select_row.__name__ is the string "select_row"
                print("Function {}, argument {}".format(f.__name__,
                                                        test[1]))
                print("Expected {}, but returned {}".format(expected, result))
    print("\nPassed {} out of {} tests.".format(passed,
                                                passed + failed))


def main():  # Run test.
    run_tests()

if __name__ == "__main__":
    main()
