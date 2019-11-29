# TODO: Think of different rules to combine entries from the two dicts.

def join_dicts(dict1, dict2):
    """ Return dict1 after extending it with dict2

    >>> join_dicts({1:'a', 2:'b', 3:'c'}, {1:'d', 2:'e'})
    {1: ['a', 'd'], 2: ['b', 'e'], 3: 'c'}
    """
    d = dict1.copy()

    for k, v in dict1.items():
        try:
            d[k] = [v, dict2[k]]
        except KeyError:
            pass


    return(d)




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



# Do not make changes to the code below
# Calls the above functions with interesting inputs.
def main():
    print('join_dicts')
    test(join_dicts({1:'a', 2:'b', 3:'c'}, {1:'d', 2:'e'}),
                    {1: ['a', 'd'], 2: ['b', 'e'], 3: 'c'})


if __name__ == '__main__':
    main()
