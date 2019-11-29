"""
Read from a text file named cities.txt with capitals and countries:

Aberdeen, Scotland
Adelaide, Australia
Algiers, Algeria


Write to another text file named cities_out.txt these contents numbered:

1: Aberdeen, Scotland
2: Adelaide, Australia
3: Algiers, Algeria

"""

def add_prefix(l, i):
    '''Function to format a string.
    l: input string
    i: row number
    '''
    return(f'{i+1}: {l}')  # NOTE: No need to convert to raw string.


def copy_to_file(infile, outfile, line_formatter, mode='w'):
    '''Copies the content of one file to another,
    and adds a prefix defined by the prefix argument (function).
    '''
    with open(infile, 'r') as f1, open(outfile, mode) as f2:

        lines = f1.readlines()
        num_lines = len(lines)
        for i, l in enumerate(lines):
            l = line_formatter(l, i+1)
            f2.write(l)



def main():
    copy_to_file('data/cities.txt', 'output/cities_out.txt',
                 line_formatter=add_prefix)


if __name__ == '__main__':
    main()
