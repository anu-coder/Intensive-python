# Link: https://t.ly/5882b
# Print the version of the script

__version__ = '1.9.6'

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help='shows version'
    )
    args = parser.parse_args()

    if args.version:
        print(__version__)