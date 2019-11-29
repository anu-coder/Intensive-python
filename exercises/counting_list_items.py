# Create a function that returns a dictionary of the items of a list
# and their counts.

def count_items(lst, sort_by='value'):
    """ Return counts of the list items. The default sorting is
    by the value of the occurences.

    >>> count_items(['one', 'two', 'two', 'three', 'three', 'three'])
    {'one': 1, 'two': 2, 'three': 3}
    """
    res = {}
    for item in lst:
        try:
            res[item] += 1
        except KeyError:
            res[item] = 1

    sort_by_index = {'item': 0, 'value': 1}

    res = dict(sorted(res.items(),
                      key=lambda kv: kv[sort_by_index[sort_by]]))

    return(res)



def main():
    print(count_items(['one', 'two', 'two', 'three', 'three', 'three'],
                      sort_by='item'))


if __name__ == '__main__':
    main()