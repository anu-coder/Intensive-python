# Link: https://t.ly/5882b
# Generate character sequence

class StartingCharacterHasGreaterUnicodeError(Exception):
    pass

def char_seq(c1, c2):
    o1, o2 = ord(c1), ord(c2)
    if o1 < o2:
        seq = ' '.join([chr(o) for o in range(ord(c1), ord(c2)+1)])
        return(seq)
    else:
        raise(
    StartingCharacterHasGreaterUnicodeError
    )



if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description=(
            'Generate a sequence of alphabets from starting to '
            'ending alphabet'
    )
    )

    parser.add_argument(
        'chars', type=str, nargs=2, metavar='c',
        help='starting and ending character')

    # NOTE: This needs to be done even if you don't want the args
    #       otherwise --help won't work.
    args = parser.parse_args()

    try:
        c1, c2 = args.chars
        print(char_seq(c1, c2))
    except (TypeError, StartingCharacterHasGreaterUnicodeError) as e:
        if isinstance(e, TypeError):
            msg = 'Arguments must be characters!'
        elif isinstance(e, StartingCharacterHasGreaterUnicodeError):
            msg = 'The starting character should precede the ending character'

        print(msg)
        print('-'*50)
        parser.print_help()
        sys.exit(1)
