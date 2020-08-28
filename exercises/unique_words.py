# Words in a string that occur exactly once

def unique_words(text, method='A'):
    """ Return a set of the words in text that occur exactly once.

    unique_words("The boy jumped over the other boy")
    >>> {'jumped', 'other', 'over'}
    """


    if method == 'A':

        seen = {}
        words = text.split(' ')

        for w in words:
            w = w.lower()
            try:
                seen[w] += 1
            except KeyError:
                seen[w] = 1

        # NOTE: sorted results in a list, so need to convert to set again
        #       as per the output requested in doc.
        res = set(sorted({k for k, v in seen.items() if v == 1}))

    elif method == 'B':
        from exercises.counting_list_items import count_items
        words = [w.lower() for w in text.split(' ')]
        res = set(sorted({k for k, v in count_items(words).items() if v == 1}))



    return(res)



def main():
    print(unique_words("The boy jumped over the other boy", method='B'))


if __name__ == '__main__':
    main()
