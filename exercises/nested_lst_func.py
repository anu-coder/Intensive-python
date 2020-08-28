# Apply a function on an arbitrary nested list
from .num_converter import conv_to_num

def apply_func(nested_lst, func):
    '''Apply a function on each item of a nested list.
    '''

    if not isinstance(nested_lst, list):
        return(func(nested_lst))

    nested_lst = nested_lst.copy()

    res = [apply_func(l, func) for l in nested_lst]

    return(res)


def main():
    lst = ['1', ['2.5', 'pizza'], []]
    print(lst)
    print(apply_func(lst, conv_to_num))
    print(lst)

if __name__ == "__main__":
    main()