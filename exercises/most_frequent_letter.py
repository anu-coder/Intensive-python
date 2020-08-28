def find_most_frequent_letter(text):
    """ Return the most frequent letter in text.
    Whitespace should be ignored.
    If two letters have the same frequency, print both arranged alphabetically.

    >>> find_most_frequent_letter("This is a super long long long string. Please help count me")
    >>> [('e', 5), ('l', 5), ('n', 5), ('s', 5)]
    """

    counts = {}
    for l in text:
        if l != ' ':
            try:
                counts[l] += 1
            except KeyError:
                counts[l] = 1

    sorted_counts = sorted(counts.items(), key=lambda kv: kv[1])
    max_count = sorted_counts[-1][1]

    res = []
    count = max_count
    i = -1
    while count == max_count:
        res.append(sorted_counts[i])
        i -= 1
        count = sorted_counts[i][1]


    return(sorted(res))

# Do not make changes to the code below
# Function used in main() to print
# what each function returns vs. what it's supposed to return

def test(returned, expected):
    if returned == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{0} returned: {1} expected: {2}'.format(prefix, repr(returned), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('find_most_frequent_letter')
    test(find_most_frequent_letter("This is a super long long long string. Please help count me"),
    [('e', 5), ('l', 5), ('n', 5), ('s', 5)])


if __name__ == '__main__':
    main()
