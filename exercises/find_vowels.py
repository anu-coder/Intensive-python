# Define a function that takes a word as an argument, returns a list of
# truth values i.e., True for a vowel in the word, False for a non-vowel.

def find_vowels(word, method='A'):
    """ Return a list containing a True for a vowel in the word,
        a False for a non-vowel.

    >>> find_vowels('detestable')
    >>> [False, True, False, True, False, False, True, False, False, True]
    """
    vowels = ['a', 'e', 'i', 'o', 'u']

    if method == 'A':
        res = []
        for l in word:
            if l in vowels:
                res.append(True)
            else:
                res.append(False)

    elif method == 'B':
        res = list(map(lambda x: True if x in vowels else False, word))


    return(res)


def main():
    print(find_vowels('detestable', 'B'))


if __name__ == '__main__':
    main()