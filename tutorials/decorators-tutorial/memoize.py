"""Example of a decorator that memoizes based on a function's arguments.
Note that if the args aren't hashable, or if kwargs is set, this cache
doesn't really work well.  (See memoize_pickle.py for how to handle that.)

From Reuven Lerner's "Practical Decorators" talk at PyCon 2019.
Reuven's courses, books, and newsletter are at https://lerner.co.il/
"""

def memoize(func):
    cache = {}

    def modfunc(*args, **kwargs):
        if args not in cache:
            print(f'Caching NEW value for {func.__name__}{args}')
            cache[args] = func(*args, **kwargs)
        else:
            print(f'Using OLD value for {func.__name__}{args}')

        return(cache[args])

    return(modfunc)


if __name__ == "__main__":
    @memoize
    def add(x, y):
        return(x+y)

    print(add(1, 1))
    print(add(1, 1))
