'''
Sort one list according to the 2nd list
'''


def sort_lst1(lst: list, by: list):
    return([x for _, x in sorted(zip(by, lst))])

# TODO: Create a proper function from scratch for this


if __name__ == "__main__":
    l1 = [1, 9, 0, -5]
    l2 = [4, 3, 2, 1]

    print(sort_lst(l1, l2))