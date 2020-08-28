"""Example of a decorator that memoizes based on a function's arguments.
This version uses "pickle", along with both args and kwargs, for a more
robust solution than memoize.py.

From Reuven Lerner's "Practical Decorators" talk at PyCon 2019.
Reuven's courses, books, and newsletter are at https://lerner.co.il/
"""

import pickle

def memoize(func):
    cache = {}

    def modfunc(*args, **kwargs):
        t = (pickle.dumps(args), pickle.dumps(kwargs))

        if t not in cache:
            print(f"Caching NEW value for {func.__name__} "
                  f"with args: {args} and kwargs: {kwargs}")
            cache[t] = func(*args, **kwargs)

        else:
            print(f"Using OLD value for {func.__name__} "
                  f"with args: {args} and kwargs: {kwargs}")

        return(cache[t])

    return(modfunc)


if __name__ == "__main__":
    @memoize
    def add(x, y):
        return(x+y)


    print(add(1, 1))
    print(add(1, 1))
    print(add(x=1, y=1)) # TODO: Find a way to use OLD value here.
