def find_first_vowel(S: str) -> str:
    """ Return the first vowel in each word of a string.

    >>> find_first_vowel("The sky's the limit")
    'e, e, i'
    """
    vowels = ['a', 'e', 'i', 'o', 'u']

    words = S.split(' ')
    res = []
    for w in words:
        for l in w:
            if l in vowels:
                res.append(l)
                break
            else: continue


    res = ', '.join(res)
    return(res)


def main():
    print(find_first_vowel("The sky's the limit"))


if __name__ == '__main__':
    main()
