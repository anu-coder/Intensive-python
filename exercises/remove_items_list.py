# Modify/Remove items in a list at particular indices

def remove_items(numbers, indices):
    '''Remove items from a list at particular indices.

    >>> lst = [0, 4, 3, 2, 1]
    >>> remove_items(lst, [1, 4, 100])
    >>> lst
    [0, 3, 1]
    '''

    len_nums = len(numbers)
    # take care of negative indices
    indices = list(map(lambda i: i if i >=0 else len_nums + i, indices))
    # repeated indices, finally sort them to avoid wrong popping.
    indices = sorted(set(indices))

    pop_count = 0
    for i in indices:
        if i < len_nums:
            numbers.pop(i-pop_count)
            pop_count += 1


def main():
    lst = [0, 4, 3, 2, 1]
    print(lst)
    remove_items(lst, [2, 1, 1, 0, 6, -1])
    print(lst)


if __name__ == '__main__':
    main()