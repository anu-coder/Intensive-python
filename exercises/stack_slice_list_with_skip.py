# Link: https://t.ly/dKKx8
from random import shuffle
from flatten_lists import flatten
# Shuffle in pairs (1,2),(4,5),(7,8)
def shuffle_in_pairs(lst: list, ipairs: list, include_other_indices=True):
    shfld_lst = []
    i_in_pairs = []
    for ipair in ipairs:
        i_in_pairs += list(ipair)
        shfld_lst += [[lst[i] for i in ipair]]

    if include_other_indices:
        for i, item in enumerate(lst):
            if i not in i_in_pairs:
                shfld_lst.append(item)

    shuffle(shfld_lst)
    return(flatten(shfld_lst))


if __name__ == '__main__':


    lst = ['a_1','a_n1','a_s1',
           'b_2','b_n2','b_s2',
           'c_3','c_n3','c_s3']
    print(lst)

    ipairs = [(1,2),(4,5),(7,8)]
    print(ipairs)

    shfld_lst = shuffle_in_pairs(lst, ipairs, include_other_indices=False)
    print(shfld_lst)

    # lst with every 2nd element of the shuffled list
    shfld_lst_every_2nd = shfld_lst[::2]
    print(shfld_lst_every_2nd)

    # new_lst with elements not in shfld_lst_every_2nd
    new_lst = [item for item in lst if item not in shfld_lst_every_2nd]
    print(new_lst)
