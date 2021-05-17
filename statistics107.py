# Function to find the maximum element in the list.
def maxi(elements):
    max_element = 0
    if len(elements) > 0:
        max_element = elements[0]
    for i in elements:
        if i > max_element:
            max_element = i
    return max_element


def mini(elements):  # Function to find the minimum element in the list.
    min_element = 0
    if len(elements) > 0:
        min_element = elements[0]
    for i in elements:
        if i < min_element:
            min_element = i
    return min_element


def suma(elements):  # Function to find the sum of elements in the list.
    sum_element = 0
    for i in elements:
        sum_element = sum_element + i
    return sum_element


def odds(elements):  # Function to find the odd elements in the list.
    odd_elements = []
    for i in elements:
        if i % 2 != 0:
            odd_elements.append(i)
    return odd_elements


def evens(elements):  # Function to find the even elements in the list.
    even_elements = []
    for i in elements:
        if i % 2 == 0:
            even_elements.append(i)
    return even_elements


def every_other(elements):  # Function to find every other element.
    every_other_elements = []
    for i in range(0, len(elements)):
        if i % 2 == 0:
            every_other_elements.append(elements[i])
    return every_other_elements


def every_other_odd(elements):  # Function to find every other odd element.
    return every_other(odds(elements))


def every_other_even(elements):  # Function to find every other even element.
    return every_other(evens(elements))


def run_tests():  # Test each function defined in this module.
    passed = 0
    failed = 0
    tests = [
        (suma, [1, 2, 3], 6),
        (suma, [], 0),
        (suma, [-1, 0, 1], 0),
        (suma, [10000, 1000, 100, 10, 1], 11111),
        (maxi, [3, 2, 1, 2, 3], 3),
        (maxi, [-1, 4, -2, 10, 1, 5], 10),
        (mini, [3, 2, 1, 2, 3], 1),
        (mini, [-1, 4, -2, 10, 1, 5], -2),
        (odds, [1, 2, 3, 4], [1, 3]),
        (odds, [1, 100, 45, 23, 10, 2, 4, 13], [1, 45, 23, 13]),
        (odds, [], []), (evens, [1, 2, 3, 4], [2, 4]),
        (evens, [1, 100, 45, 23, 10, 2, 4, 13], [100, 10, 2, 4]),
        (evens, [], []), (every_other, [1, 2, 3, 4], [1, 3]),
        (every_other, [1, 100, 45, 23, 10, 2, 4, 13], [1, 45, 10, 4]),
        (every_other, [], []),
        (every_other_odd, [1, 2, 3, 4], [1]),
        (every_other_odd, [1, 100, 45, 23, 10, 2, 4, 13], [1, 23]),
        (every_other_odd, [], []),
        (every_other_even, [1, 2, 3, 4], [2]),
        (every_other_even, [1, 100, 45, 23, 10, 2, 4, 13], [100, 2]),
        (every_other_even, [], []),
            ]
    # Print a detailed error message whenever a function fails a test.
    counter = 0
    for test in tests:
        f = (test[0])
        result = f(test[1])
        expected = test[2]
        counter += 1
        print("#", counter, ", result = ", result, ", expected = ", expected)
        if result == expected:
            passed += 1
        else:
            failed += 1
            print("Function {}, given argument {}".format(f.__name__, test[1]))
            print("Expected {}, but returned {}".format(expected, result))
    print("\nPassed {} out of {} tests.".format(passed, passed + failed))


def main():  # Run the test.
    run_tests()

if __name__ == "__main__":
    main()
