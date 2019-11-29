# Convert an entry (or it's constituent parts) to a number.
# TODO: implement similiar func conv_to, main_func, exception_func
# TODO: Explore a nested list, apply a func.
#       This func must be self-sufficient.

import numbers


def conv_to_num(entry, func=lambda x: x):
    '''Converts an entry (or it's contents in case of a list)
    to a number, when possible.

    >>> conv_to_num(['1', ['2.5', 'pizza'], []])
    [1, [2.5, 'pizza'], []]
    '''
    if isinstance(entry, numbers.Number):
        res = func(entry)
    elif isinstance(entry, str):
        # NOTE: try block two things. Sweet! :)
        for inner_func in [int, float]:
            try:
                res = func(inner_func(entry))
                break
            except ValueError:
                continue
        else:
            res = entry

    elif isinstance(entry, list):
        # NOTE: map can't be used with function args
        res = [conv_to_num(item, func=func) for item in entry]



    return(res)



def main():
    lst = ['1', ['2.5', 'pizza'], []]
    print(lst)
    print(conv_to_num(lst), lambda x: x)
    print(lst)



if __name__ == '__main__':
    main()
