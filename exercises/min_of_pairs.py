def min_of_pairs(number):
    """ Return a number built from the min of
        each pair of the digits of the input number.

    >>> min_of_pairs('84372216')
    '4321'
    """

    min_vals = []
    v1=v2=None
    for i, s in enumerate(number):
        v2 = v = int(s)
        if ((i - 1) % 2 == 0) and i != 0: # Even place entry
            min_vals.append(str(min(v1, v2)))
            v1 = None
        else:
            v1 = v

    res = ''.join(min_vals)
    return(res)





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
    print('min_of_pairs')
    test(min_of_pairs('84372216'), '4321')


if __name__ == '__main__':
    main()
