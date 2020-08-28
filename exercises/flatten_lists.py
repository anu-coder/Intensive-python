# Also see Link: https://t.ly/Gkk00

def flatten(nested_lst):
    """ Return a list after transforming the inner lists
        so that it's a 1-D list.

    >>> flatten([[[],["a"],"a"],[["ab"],[],"abc"]])
    ['a', 'a', 'ab', 'abc']
    """
    if not isinstance(nested_lst, list):
        return(nested_lst)

    res = []
    for l in nested_lst:
        if not isinstance(l, list):
            res += [l]
        else:
            res += flatten(l)


    return(res)


# Do not make any changes to the code below
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
    print('flatten')
    test(flatten([[[],["a"],"a"],[["ab"],[],"abc"]]),
                 ['a', 'a', 'ab', 'abc'])
    # test(flatten([['a'], 'b']), ['a', 'b'])


if __name__ == '__main__':
    main()
