def get_longest_name(a_list, method='A'):
    """ Return '******' if the input list is [], [''], or a list containing
        names of equal length.
        Else, return the name that is greater in length than any other name
        in the list.

    >>> get_longest_name(["Candide", "Jessie", "Kath", "Amity", "Raeanne"])
    ['Candide', 'Raeanne']
    >>> get_longest_name(["Jessie", "Kath", "Amity", "Raeanne"])
    'Raeanne'
    >>> get_longest_name(["Jessie", "Kath", "Amity"])
    'Jessie'
    """
    placeholder = '******'
    if (not a_list) or a_list == ['']:
        return(placeholder)


    if method == 'A':
        max_count = cur_count = 0
        i_max = [0]

        for i, w in enumerate(a_list):
            cur_count = len(w)
            if cur_count > max_count:
                max_count = cur_count
                i_max = [i]
            elif cur_count == max_count:
                i_max += [i] # NOTE: this is extending of lists


        # Possible computation gains,by not calling len
        # as we just iterated over a loop,
        # but that matters more in C not python.
        if len(i_max) == len(a_list):
            return(placeholder)
        else:
            res = [a_list[i] for i in i_max]
            return(res)

    elif method == 'B':
        pass



def main():
    print(get_longest_name(["Candide", "Jessie", "Kath", "Amity", "Raeanne"]))
    print(get_longest_name(["Jessie", "Kath", "Amity", "Raeanne"]))
    print(get_longest_name(['ABC', 'DEF']))
    print(get_longest_name(['']))
    print(get_longest_name([]))


if __name__ == '__main__':
    main()
