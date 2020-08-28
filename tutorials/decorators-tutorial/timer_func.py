'''
Add timer to a function [Decorator using a function]
'''
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f'Elapsed time for {func.__name__} is {elapsed:.2f}s')

        return(rv)

    return(wrapper)



if __name__ == '__main__':
    @timer
    def slow_add(x, y):
        time.sleep(1)
        return(x+y)

    slow_add(1, 2)