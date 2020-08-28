# Number of consecutive spells of 1's greater than n.
# TODO: Add slice of positions to indicate when each spell happened.

def consecutive_spells(lst, n):
    '''Returns the number of such spells, and total spell length
    with consecutive 1's with spell length atleast n.


    >>> consecutive_spells([1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,1], n=3)
    >>> {'num_spells': 2, 'spell_length': 8}
    '''
    cur_count = 0
    num_spells = 0
    spell_length = 0

    for i in lst:
        if i == 1:
            cur_count += 1
        else:
            if cur_count >= n:
                num_spells += 1
                spell_length += cur_count

            cur_count = 0


    res = {'num_spells': num_spells, 'spell_length': spell_length}



    return(res)


def main():
    print(consecutive_spells([1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,1], n=3))


if __name__ == '__main__':
    main()
