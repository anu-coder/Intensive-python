# Convert the file into a specific format

from copy_to_file import copy_to_file, add_prefix

"""

Input file
line 1: value1
line 2: value2
line 3: value3
line 4: value4
line 5: value5

Output file
index_col: line_col: value_col
1: line 1: value1
2: line 2: value2
3: line 3: value3
4: line 4: value4
5: line 5: value5

"""

def main():
    infile = 'data/line_value.txt'
    outfile = 'output/line_value_out.txt'

    with open(outfile, 'w') as f:
        f.write('index_col: line_col: value_col:\n')

    copy_to_file(infile, outfile,
                 line_formatter=lambda l, i : add_prefix(l, i-1),
                 mode='a')


if __name__ == '__main__':
    main()
