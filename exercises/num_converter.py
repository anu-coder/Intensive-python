
def conv_to_num(x, num_type='asis'):
    '''Converts an object to a number if possible.
    num_type: int, float, 'asis'
    Defaults to floating point in case of ambiguity.
    '''
    import numbers

    is_num, is_str, is_other = [False]*3

    if isinstance(x, numbers.Number):
        is_num = True
    elif isinstance(x, str):
        is_str = True

    is_other = not any([is_num, is_str])

    if is_num:
        res = x
    elif is_str:
        is_float, is_int, is_char = [False]*3
        try:
            res = float(x)
            if '.' in x:
                is_float = True
            else:
                is_int = True
        except ValueError:
            res = x
            is_char = True

    else:
        if num_type == 'asis':
            funcs = [int, float] # TODO: Check __int__, __float__ attrs in x
                                 #       otherwise, it's unnecessary computation
                                 # Ans: Not really, since int and float, call
                                 # __int__ and __float__ methods.
        else:
            funcs = [num_type]

        for func in funcs:
            try:
                res = func(x)
                break
            except TypeError:
                continue
        else:
            res = x


    if is_num or is_str:
        if num_type != 'asis':
            return(num_type(res))
        else:
            if is_num:
                return(res)
            elif is_str: # For understanding/clarity checking is_str
                if is_int:
                    return(int(res))
                else:
                    return(res)

    return(res)

def main():
    class PsuedoNum:
        def __init__(self, value):
            self.value = value

        def __int__(self):
            return(int(self.value))

        def __float__(self):
            return(float(self.value))

        def __repr__(self):
            return(f'{self.__class__.__name__}(value={self.value})')


    n = PsuedoNum(5)
    print(n)
    print(conv_to_num(n))


if __name__ == "__main__":
    main()