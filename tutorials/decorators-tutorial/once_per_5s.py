'''
Allow a function to run only once per 5s
'''
import time

class CalledTooOftenError(Exception):
    message = 'The function was called too often.'

def once_per_5s(func):
    last_run = 0

    def modfunc(*args, **kwargs):
        nonlocal last_run
        elapsed = time.time() - last_run
        if elapsed < 5:
            raise CalledTooOftenError()

        rv = func(*args, **kwargs)
        last_run = time.time()
        return(rv)

    return(modfunc)


if __name__ == "__main__":

    @once_per_5s
    def compute_intensive():
        time.sleep(1)
        return(0)

    print(compute_intensive())
    time.sleep(4)
    print(compute_intensive())
