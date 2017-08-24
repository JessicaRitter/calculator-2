"""Math functions for calculator."""


def add(lst):
    """Return the sum of the list of integers."""
    num_sum = 0

    for num in lst:
        num_sum += num

    return int(num_sum)


def subtract(lst):
    """Return the second number subtracted from the first."""
    num1 = lst[0]
    new_lst = lst[1:]

    new_lst_sum = add(new_lst)

    return int(num1 - new_lst_sum)


def multiply(lst):
    """Multiply a list of inputs together."""

    num_prod = 1

    for num in lst:
        num_prod = num_prod * num

    return int(num_prod)


def divide(lst):
    """Divide the first input by the second, returning a floating point."""
    num1 = float(lst[0])
    new_lst = lst[1:]

    for num in new_lst:
        num1 = (num1 / num)

    return num1


def square(lst):
    """Return the list with the inputs squared."""

    squared_lst = []

    for num in lst:
        squared_lst.append(num * num)

    return squared_lst


def cube(lst):
    """Return the list with the inputs cubed."""
    cubed_lst = []

    for num in lst:
        cubed_lst.append(num * num * num)

    return cubed_lst


def power(lst):
    """Returns the product of the numbers to the next numbers power."""

    num_prod = lst[0] ** lst[1]

    for num in lst[2:]:
        num_prod = num_prod ** num

    return num_prod


def mod(lst):
    """Return the % of a list of numbers."""
    num_mod = lst[0] % lst[1]

    for num in lst[2:]:
        try:
            num_mod = num_mod % num
        except ZeroDivisionError:
            print "There should not be any zeros in the list, bro."
            break
    return num_mod


def add_mult(lst):
    """Add num1 to num2, then multiply by rest of numbers in the list."""

    num_sum = lst[0] + lst[1]

    for num in lst[2:]:
        num_sum = num_sum * num

    return num_sum


def add_cubes(lst):
    """Cubes num1 and num2, then adds them."""
    lst = cube(lst)
    lst = add(lst)

    return lst
