# How to try two things

def str_to_num(s: str):
    '''Converts to int if possible else converts to float if possible
    Returns back the string if not possible to convert to a number.
    '''
    # NOTE: These are not really funcs, but classes.
    funcs = [int, float]

    for func in funcs:
        try:
            res = func(s)
            break
        except ValueError:
            continue
    else:
        res = s

    return(res)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Convert a string to num')
    parser.add_argument(
        '-nums', dest='strings', type=str, nargs='*'
    )
    args = parser.parse_args()
    strings = args.strings

    for s in strings:
        print(repr(str_to_num(s)), end=' ')

    print()