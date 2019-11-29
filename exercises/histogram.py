'''
Make a histogram in pure python
'''

def count_items(lst: list)->dict:
    count = {}
    for i in lst:
        try:
            count[i] += 1
        except KeyError:
            count[i] = 1

    return(count)

def _gen_rand_lst(min: int, max: int, lst: list)-> list:
    '''
    Generates a list containing random numbers having
    minimum frequency <min> and maximum frequency <max>
    '''
    import random # NOTE: Inside bc not required for "main" functionality

    rand_lst = []
    for i in lst:
        rand_lst += [i]*random.randint(min, max)

    return(rand_lst)

def _num_digits(i: int):
    '''
    Returns the number of digits in an integer
    '''
    import math
    if i != 0:
        return(round(math.log(abs(i))) + 1)
    else:
        return(0)

def print_histogram(lst: list, mode='horizontal')-> None:
    '''
    Prints out a vertical/horizontal histogram
    '''
    count = count_items(lst)
    # TODO: padding width variable substitution in f or format string
    #       see my stackoverflow question https://t.ly/dKXjA
    num_width = _num_digits(max(count.keys()))

    for i, count in count.items():
        print(f'{i:{num_width}}:', '*'*count)






if __name__ == "__main__":
    lst = _gen_rand_lst(1, 10, range(20))

    print(lst, count_items(lst), sep='\n')
    print()
    print_histogram(lst)
