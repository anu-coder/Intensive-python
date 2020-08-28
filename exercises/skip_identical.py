def skip_identical(lst, return_str=False):
    """ Print output as shown below.

    list_description = [('name1','species','description','country','n/a'),
                        ('name1','species','description','country','plasmid1'),
                        ('name1','species','description','country','plasmid2')]

    >>> skip_identical(list_description)
    name1 species description country n/a
                                      plasmid1
                                      plasmid2
    """

    seen = {}
    res = ''
    for t in lst:
        for w in t:
            if not seen.get(w, False):
                if return_str:
                    res += w + ' '
                else:
                    print(w, end=' ')

            else:
                if return_str:
                    res += ' '*len(w) + ' '
                else:
                    print(' '*len(w), end=' ')

            seen[w] = True # NOTE: Check in case this is some heavy computation
                           #       other than just assigning True to the value.

        if return_str:
            res += '\n'
            return(res)
        else:
            print()





def main():
    list_description = [('name1','species','description','country','n/a'),
                        ('name1','species','description','country','plasmid1'),
                        ('name1','species','description','country','plasmid2')]

    print(skip_identical(list_description, return_str=False))


if __name__ == '__main__':
    main()