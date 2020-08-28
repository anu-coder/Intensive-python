
from remove_items_list import remove_items

def get_min(numbers):
    """ Return a new list with the smallest value in the input list.
    Before returning the new list, remove the value from the original list.

    >>> nums = [3, 4, 1, 1]
    >>> get_min(nums)
    1
    >>> nums
    [3, 4]
    """

    min_val = numbers[0]
    i_mins = [0]
    for i, val in enumerate(numbers):
        if val < min_val:
            min_val = val
            i_mins = [i]
        elif (val == min_val) and (i != 0):
            i_mins += [i]

    remove_items(numbers, i_mins)

    return(min_val)


def main():
    lst = [-1, 0, 3, 4, 1, 1, -2, -2]
    print(lst)
    print(get_min(lst))
    print(lst)




if __name__ == '__main__':
    main()