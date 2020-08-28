# Implementation of a context manager
import os
try:
    os.remove('output.txt')
except FileNotFoundError:
    pass

# from contextlib import contextmanager

class contextmanager:

    def __init__(self, gen):
        self.gen = gen

    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self

    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        return(next(self.gen_inst))


    def __exit__(self, exc_type, exc_val, traceback):
        next(self.gen_inst, None)
        del self.args, self.kwargs, self.gen_inst



@contextmanager
def open_file(filepath, mode):
    try:
        f = open(filepath, mode)
        yield f
    finally:
        f.close()

with open_file('output.txt', 'w') as f:
    f.write(f'This message was written using {__file__}')
