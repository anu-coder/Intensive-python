# Find factorials of a list of numbers

def factorialize(numbers):
    """ Return factorials of a list of numbers.

    >>> factorialize([1, 2, 3, 4, 5])
    >>> [1, 2, 6, 24, 120]
    """

    res = list(map(fact, numbers))

    return(res)


def fact(n):
    if n == 0:
        return(1)
    else:
        return(n*fact(n-1))


def main():
    print(factorialize(range(1, 6)))


if __name__ == '__main__':
    main()
