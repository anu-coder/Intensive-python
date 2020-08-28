# Pick words of certain length from a string, but ignore punctuation
# TODO: Using re.

def find_words_of_length(number, text):
    """ Remove punctuation from text, then return words of length number.

    >>> find_words_of_length(4, "this is a string with some four-letter words.")
    >>> ['this', 'with', 'some']
    """

    words = text.split(' ')
    puncs = '.!?'
    res = []

    cur_count = 0
    for w in words:
        if w != '':
            for p in puncs:
                w = w.replace(p, '')

            if len(w) == 4:
                res.append(w)


    return(res)


def main():
    print(find_words_of_length(4,
                              "this is a string with some four-letter words."))



if __name__ == '__main__':
    main()
