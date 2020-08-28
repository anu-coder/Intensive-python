# Define a function that does this:
# Given a list of strings, with each string having a student’s name and
# their grades, mutate the input list so the original string positions are
# replaced with their average grades. The function doesn’t need an explicit
# return statement.

from conv_to_num import conv_to_num


def conv_to_averages(lst):
    '''Mutates the input csv strings in a list in the following manner
    >>> reports = ['Anna, 50, 92, 80', 'Bill, 60, 70',
                   'Cal, 98.5, 100, 95.5, 98']
    >>> get_averages(reports)
    >>> reports
    [('Anna', 74.0), ('Bill', 65.0), ('Cal', 98.0)]
    '''

    for i, s in enumerate(lst):
        splitted = s.split(', ')
        name = splitted[0]
        avg = sum(conv_to_num(splitted[1:]))/len(splitted[1:])
        lst[i] = (name, avg)


    return(None)





def main():
    reports = ['Anna, 50, 92, 80', 'Bill, 60, 70', 'Cal, 98.5, 100, 95.5, 98']
    print(reports)
    conv_to_averages(reports)
    print(reports)


if __name__ == '__main__':
    main()
# [74.0, 65.0, 98.0]
