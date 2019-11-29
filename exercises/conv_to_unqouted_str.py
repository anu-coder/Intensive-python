# Convert a string such that it is not surrounded by quotes.



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


if __name__ == "__main__":
    s = "''asas'''"
    res = unquoted_str(s)
    print(res)
