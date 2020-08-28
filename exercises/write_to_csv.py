"""
country = ['Togo', 'Nauru', 'Palestine, State of', 'Malawi']

Write the above list to a CSV file,
each item in a row, without an empty line between rows.

To see what the output should look like,
you could go to https://i.stack.imgur.com/uusgN.png

"""

def write_to_csv(filename, lines):
    num_lines = len(lines)

    with open(filename, 'w') as f:
        for i, l in enumerate(lines):
            l = "%r"%l # Convert a string to raw string
            f.write(l)
            if i != num_lines - 1:
                f.write('\n')



def main():
    country = ['Togo', 'Nauru\n', 'Palestine, State of', 'Malawi']
    write_to_csv('output/write_to_csv.txt', country)



if __name__ == '__main__':
    main()