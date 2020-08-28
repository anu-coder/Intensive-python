# Sort a list according to a certain rule


def rule_sort(lst):
    '''Sorts the list according to the following rule:
    Proceed swapping the number with the next number until the next number
    is smaller than or equal to the current, else swap it with it's original place.

    >>> rule_sort([1, 3, 2, 1])
    [1, 2, 3, 4]
    '''
    lst = lst.copy()

    n1=n2=None
    i_first_swap = None
    swapped = False
    i=0
    for n in lst:
        n2 = n
        if (n1 and n2) and (n1 > n2):
            if not swapped:
                swapped = True
                i_first_swap = i
            lst[i-1], lst[i] = lst[i], lst[i-1]
        elif i != 0:
            lst[i_first_swap], lst[i] = lst[i], lst[i_first_swap]

        n1 = n

        i += 1

    return(lst)


def main():
    print(rule_sort([1, 3, 2, 1]))



if __name__ == '__main__':
    main()