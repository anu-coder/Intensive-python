# Helper functions

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


def unquoted_str(s: str):
    '''Converts a string into an unquoted string'''
    # TODO: use regex

    # NOTE: Not requiring an s argument, as it seems cleaner
    #       and also unneccesary if function is just for
    #       internal consumption.
    def quotedAt(at):
        quotes = ["'", '"']
        if at == 'start':
            i = 0
        elif at == 'end':
            i = -1

        return(True if s[i] in quotes else False)

    # NOTE: Avoiding unneccessary function calls
    #       by checking if s[0] == s[-1]
    while s[0] == s[-1] and quotedAt('start') and quotedAt('end'):
        s = s[1:-1]

    return(s)