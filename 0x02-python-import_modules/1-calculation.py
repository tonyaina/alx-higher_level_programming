#!/usr/bin/python3

if __name__ == "__main__":

    """print mathematical calculations of addition,
    substration, multiplication and division quotient of 10 and 5."""

    from calculator_import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
