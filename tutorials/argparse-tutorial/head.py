# Link: https://t.ly/5882b
# Mimic the head command of linux

def head(filepath, n=None):
    # LINK: Stackoverflow: Read first N lines; https://t.ly/8XX62
    # TODO: if n is greater than number of lines, stop appending
    # TODO: if n is None, just use readlines()
    #       (? More efficient than iterating?)
    # TODO: lines should not contain newline character at the end.
    # TODO: Check performance differences.

    with open(filepath, 'r') as f:

        if n is None:
            lines = f.read().splitlines()

        else:
            lines = []
            for i in range(n):
                try:
                    line = next(f)
                except StopIteration:
                    break
                else:
                    # TODO: use regex.
                    if line[-1] == '\n':
                        line = line[:-1]

                    else:
                        line = line
                    lines.append(line)

    return(lines)




if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Print out the first n lines of a text file.'
    )

    parser.add_argument(
        'file',
        help='Input file'
    )
    parser.add_argument(
        '-n', default=None, type=int, help='number of lines to read.'
    )

    args = parser.parse_args()
    lines = head(args.file, args.n)
    for line in lines:
        print(line)