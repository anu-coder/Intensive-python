def get_names(lsts, method='A'):
    """ Return a list of lists containing strings separated at a newline character.

    >>> get_names(['Mike','Angela','Bill','\n','Robert','Pam','\n'])
    [['Mike', 'Angela', 'Bill'], ['Robert', 'Pam']]
    """

    if method == 'A':
        res = []
        lst = []
        for w in lsts:
            if w != '\n':
                lst.append(w)
            elif lst:
                res.append(lst)
                lst = []

    else:
        raise(NotImplementedError)




# Do not make any changes to the code below
# Function used in main() to print
# what each function returns vs. what it's supposed to return

def test(returned, expected):
    if returned == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{0} returned: {1} expected: {2}'.format(prefix, repr(returned), repr(expected)))


# Do not make any changes to the code below
# Calls the above functions with interesting inputs.
def main():
    print('get_names')
    test(get_names(['Mike','Angela','Bill','\n','Robert','Pam','\n'], method='A'),
        [['Mike', 'Angela', 'Bill'], ['Robert', 'Pam']])


if __name__ == '__main__':
    main()
