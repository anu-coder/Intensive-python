# Sorted random floating numbers

import random

def generate_floats(start, end, how_many):
    """ Return a list of sorted random floats in the (start, end) range.

    >>> generate_floats(3, 6, 5)
    >>> ['4.125', '4.622', '4.835', '4.981', '5.364']
    """
    res = [0]*how_many
    for i, _ in enumerate(res):
        r = random.random()
        rand_num = round((end-start)*r + start, 3)
        res[i] = str(rand_num)


    return(res)



def main():
    print(generate_floats(3, 6, 5))


if __name__ == '__main__':
    main()
