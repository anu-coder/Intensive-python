# Swapping list elements


def swap_elements(lst: list):
    """ Return the list after swapping the biggest integer in the list
    with the one at the last position.

    >>> swap_elements([3, 4, 2, 2, 43, 7])
    >>> [3, 4, 2, 2, 7, 43]
    """
    lst = lst.copy()

    max_num = lst[0]
    i_max = 0


    i=0
    for n in lst:
        if n >= max_num:
            max_num = n
            i_max = i

        i += 1

    lst[-1], lst[i_max] = lst[i_max], lst[-1]

    return(lst)


def main():
    print(swap_elements([3, 4, 65, 2, 65, 7, 54]))


if __name__ == '__main__':
    main()