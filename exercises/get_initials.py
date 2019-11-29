# Write a program that takes a full name, prints the initials of the first,
# middle, and last name. If the middle name is “NA”, then the program
# should print only the initials of the first and the last name.


def get_initials(name):
    """ Return initials of first, last and middle name.
    If the middle name is 'NA', return only the initials of the first and the last name.

    >>> get_initials("Alfred E. Newman")
    'A.E.N.'
    >>> get_initials("John NA Smith")
    'J.S.'
    """

    names_lst = name.split(' ')
    res = ''.join(list(map(lambda x: f'{x[0]}.' if x != 'NA' else '',
                           names_lst)))

    return(res)


def main():
    print(get_initials("Alfred NA Newman"))


if __name__ == '__main__':
    main()
