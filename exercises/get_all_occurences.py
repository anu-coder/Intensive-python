# Get all occurences of an item in a list


def get_all_occurences(lst: list, item):
    '''Get the index of all occurences of an item in a list

    >>> get_all_occurences([1, 3, 2, 5, 1, 5, 9], 1)
    [0, 4]
    '''

    indices = []

    for i, elem in enumerate(lst):
        if elem == item:
            indices.append(i)

    return(indices)




def main():
    lst = [1, 3, 2, 5, 1, 5, 9]
    print(get_all_occurences(lst, 1))

if __name__ == '__main__':
    main()