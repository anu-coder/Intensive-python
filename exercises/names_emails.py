'''
Create a textfile named test.txt with these two lines in it:
Oleg, oserdyuk@aligngeneral.com
Tomash, tbarbarasz@aligngeneral.com
'''

# TODO: Make a general case of n entries in each row.

def get_contacts(filename):
    """ Return names and emails extracted from the textfile.

    >>> get_contacts('test.txt')
    (['Oleg', 'Tomash'], ['oserdyuk@aligngeneral.com', 'tbarbarasz@aligngeneral.com'])
    """

    with open(filename, 'r') as f:
        contents = f.readlines()


    names, emails = [], []
    num_lines = len(contents)
    for i, l in enumerate(contents):
        # remove newline character at the end
        if i != num_lines -1:
            l = l[:-1] # NOTE: newline \n is 1 character space

        name, email = l.split(', ')

        names.append(name), emails.append(email)


    res = (names, emails)
    return(res)




    # your code here



# Do not make any changes to the code below
# Function used in main() to print
# what each function returns vs. what it's supposed to return

def test(returned, expected):
    if returned == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{0} returned: {1} expected: {2}'.format(prefix, repr(returned), repr(expected)))


# Do not make any changes to the code below
# Calls the above functions with interesting inputs.
def main():
    print('get_contacts')
    test(get_contacts('data/names_emails.txt'), (['Oleg', 'Tomash'],
                     ['oserdyuk@aligngeneral.com', 'tbarbarasz@aligngeneral.com']))


if __name__ == '__main__':
    main()
