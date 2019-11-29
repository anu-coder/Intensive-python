# Context manager for changing to a certain directory an back
from contextlib import contextmanager
import os
@contextmanager
def change_dir(destination):
    '''
    changes to a directory, yields all the files, then changes back.
    '''
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield (f for f in filter(os.path.isfile, os.listdir()))
    finally:
        os.chdir(cwd)


print(os.getcwd())

with change_dir('/home/abhi') as files:
    exts = {}
    for f in files:
        ext = os.path.splitext(f)[1]
        try:
            exts[ext] += 1
        except KeyError:
            exts[ext] = 1

    print(os.getcwd())

print(os.getcwd())

print(exts)
