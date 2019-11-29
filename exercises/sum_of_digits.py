# Adding the digits of a number with certain fun rules.


def sum_of_digits(number):
    """ Returns the sum of the digits of a number.
    If it's a true floating point number then, subtract subsequent digits
    decimal scaled by 10^(neg of decimal place).


    >>> sum_digits(1234)
    10
    >>> sum_digits(1234.5678)
    9.4322
    >>> sum_digits(1234.0)
    10.0
    """

    res = 0
    num = str(number)
    has_decimal = False
    i_decimal = 0
    for n in num:
        if n != '.':
            if not has_decimal:
                res += int(n)
            else:
                i_decimal += 1
                res -= (10**(-i_decimal-1))*int(n)
        else:
            has_decimal = True


    return(res)


def main():
    print(sum_of_digits(1234.0))


if __name__ == '__main__':
    main()
