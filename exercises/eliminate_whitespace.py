# Use regex to eliminate whitespace(s) between two specific words

def remove_spaces(text, word_one, word_two):
    """ Return text after removing whitespace(s) between two specific words.

    >>> remove_spaces("an app store app maker app    store", "app", "store")
    'an appstore app maker appstore'
    """

    lst1 = text.split(' ')
    lst2 = []

    w1=w2=None
    already_appended = False
    for w in lst1:
        w2 = w
        if w1 == word_one and w2 == word_two:
            lst2.append(w1+w2)
        elif ((w1 == word_one) and
             (w2 == '') and
             (not already_appended)):

            lst2.append(w1)
            already_appended = True
        else:
            lst2.append(w)
            w1 = w
            already_appended = False






    res = ' '.join(lst2)

    return(res)


def main():
    print(remove_spaces("an app store app maker app    store", "app", "store"))



if __name__ == '__main__':
    main()
