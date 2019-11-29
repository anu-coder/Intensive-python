# Link: https://t.ly/5882b
# Greet multiple users if provided

from greet_and_show_time import greet

_ALPHABETS = 'abcdefghijklmnop'

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Greet multiple users and show the time if requested.'
    )

    parser.add_argument(
        '-n',
        metavar='name',
        dest='names',
        action='append',
        help='provide name(s) to greet.'
    )

    parser.add_argument(
        '-t', '--time',
        dest='show_time',
        action='store_true',
        help='show time'
    )

    args = parser.parse_args()
    names, show_time = args.names, args.show_time

    for name in names[:-1]:
        greet(name, show_time=False)

    greet(names[-1], show_time=show_time)