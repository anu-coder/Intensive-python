# Context manager function for file opening and closing

from contextlib import contextmanager
import os

try:
    os.remove('output.txt')
except FileNotFoundError:
    pass


@contextmanager
def open_file(filepath, mode):
    try:
        f = open(filepath, mode)
        yield f
    finally:
        f.close()


with open_file(f'output.txt', 'w') as f:
    f.write(f'This message was written using {__file__}\n')
