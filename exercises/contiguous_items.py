def contiguous_subarray(lst):
    """ Return the longest sub-array which consists of all 1’s.

    a_list = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0]
    >>> contiguous_subarray(a_list)
    4
    """

    cur_count = 0
    max_count = cur_count

    for i in lst:
        if i == 1:
            cur_count += 1
        else:
            if max_count < cur_count:
                max_count = cur_count

            cur_count = 0


    return(max_count)


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
    a_list = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0]
    print('contiguous_subarray')
    test(contiguous_subarray(a_list), 5)


if __name__ == '__main__':
    main()
