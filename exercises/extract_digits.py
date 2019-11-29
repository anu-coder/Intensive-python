# Extract digits of a number

from .conv_to_num import conv_to_num

def extract_digits(n, method='A'):
    '''Extract digits of a number in the following manner.

    >>> extract_digits(1234.5678)
    >>> [[1, 2, 3, 4], [5, 6, 7, 8]]
    '''

    if method == 'A':

        if type(n) is float:
            int_digits, float_digits = [list(lst) for lst in str(n).split('.')]
        elif type(n) is int:
            int_digits, float_digits = list(str(n)), []


    elif method == 'B':
        pass


    res = conv_to_num([int_digits, float_digits])


    return(res)





def main():
    print(extract_digits(1234))


if __name__ == '__main__':
    main()