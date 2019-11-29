from .extract_digits import extract_digits

def is_armstrong(number):
    """ Return True if the sum of the cubes of the digits in the number
        is equal to the number itself, else return False.

    >>> is_armstrong(153)
    True
    """

    int_digits, float_digits = extract_digits(number)

    sum_cubes = sum(map(lambda x: x**3, int_digits+float_digits))

    if sum_cubes == number:
        return(True)
    else:
        return(False)



# Do not make changes to the code below
# Function used in main() to print
# what each function returns vs. what it's supposed to return

def test(returned, expected):
    if returned == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{0} returned: {1} expected: {2}'.format(
        prefix, repr(returned), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('add_cubes')
    test(is_armstrong(153), True)
    test(is_armstrong(370), True)
    test(is_armstrong(407), True)
    test(is_armstrong(150), False)


if __name__ == '__main__':
    main()
