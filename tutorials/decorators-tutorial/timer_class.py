'''
Add timer to a function (Decorator using a class)
'''
import time

class Timer:

    def __init__(self, func):
        self.func = func


    def __call__(self, *args, **kwargs):
        start = time.time()
        rv = self.func(*args, **kwargs)
        elapsed = time.time() - start
        print(f'Elapsed time for {self.func.__name__} is {elapsed:.2f}s')
        return(rv)



if __name__ == "__main__":
    @Timer
    def slow_add(x, y):
        time.sleep(1)
        return(x+y)

    slow_add(1, 2)