"""Math functions for calculator."""


def my_reduce(func, p_list):
    total = p_list[0]
    for item in  p_list[1:]:
        toatl = func(total, item)
    return total 


def add(arg_list):
    """Return the sum of the integers in input list."""

    return reduce(lambda x, y: x + y, arg_list)

def subtract(arg_list):
    """Return the result of the first number subtracte the next ones."""

    return reduce(lambda x, y: x - y, arg_list)


def multiply(arg_list):
    """Multiply the all inputs together."""

    return reduce(lambda x, y: x * y, arg_list)


def divide(arg_list):
    """Divide the first input by the next ones, returning a floating point."""

    # Need to turn at least one argument to float for division to
    # not be integer division

    return reduce(lambda x, y: float(x) / y, arg_list)


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
