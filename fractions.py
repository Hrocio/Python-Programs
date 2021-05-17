import math


def reduce(fraction1):
    """This function takes a fraction, reduces it, and returns the result.

    The math.gcd function is used here from the math modulo.
    """
    g = math.gcd(fraction1[0], fraction1[1])
    return int(fraction1[0] / g), int(fraction1[1] / g)


def add(fraction1, fraction2):
    """This function takes two fraction as tuples, adds them,
    and returns the result.
    """
    num = fraction1[0] * fraction2[1] + fraction1[1] * fraction2[0]
    dem = fraction1[1] * fraction2[1]
    return num, dem


def multiply(fraction1, fraction2):
    """This function takes two fractions as tuples, add them,
    multiplies them, and returns the result.
    """
    return fraction1[0] * fraction2[0], fraction1[1] * fraction2[1]


def divide(fraction1, fraction2):
    """This function takes two fractions as tuples, divides them,
    and returns the result.
    """
    return (fraction1[0] * fraction2[1]), (fraction1[1] * fraction2[0])


def main():
    """The functions add, multiply, reduce, and divide are
    used from this main function.
    The split function converts strings into tuples.
    """
    fract_one = tuple([int(x) for x in input("Enter a fraction>>>")
                      .split("/")])
    fract_two = tuple([int(x) for x in input("Enter a fraction>>>")
                      .split("/")])
    redu_one = reduce(fract_one)
    redu_two = reduce(fract_two)
    print("Reduced fraction to %d/%d and %d/%d" % (redu_one[0], redu_one[1],
                                                   redu_two[0], redu_two[1]))
    s = reduce(add(redu_one, redu_two))
    print("Sum of the fractions: %d/%d " % (s[0], s[1]))
    m = reduce(multiply(redu_one, redu_two))
    print("Multiplication of the fractions: %d/%d " % (m[0], m[1]))
    d = reduce(divide(redu_one, redu_two))
    print("Division of the first by the second: %d/%d " % (d[0], d[1]))

# Calling main.
if __name__ == "__main__":
    main()
