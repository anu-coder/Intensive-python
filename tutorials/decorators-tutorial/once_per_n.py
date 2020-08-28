'''
Allow a function to run only once per n seconds
'''

from helpers import CalledTooOftenError
import time


def once_per_n(n):
    def normaldeco(func):
        last_run = 0
        def modfunc(*args, **kwargs):
            nonlocal last_run
            elapsed = time.time() - last_run
            if elapsed < n:
                raise CalledTooOftenError()

            rv = func(*args, **kwargs)
            last_run = time.time()

            return(rv)

        return(modfunc)
    return(normaldeco)


if __name__ == "__main__":

    @once_per_n(5)
    def compute_intensive():
        time.sleep(1)
        return(0)

    print(compute_intensive())
    time.sleep(4)
    print(compute_intensive())
