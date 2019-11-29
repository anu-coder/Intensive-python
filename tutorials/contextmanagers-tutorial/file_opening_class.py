import os

try:
    os.remove('output.txt')
except FileNotFoundError:
    pass


class OpenFile:

    def __init__(self, filepath, mode):
        self.filepath = filepath
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filepath, self.mode)
        return(self.file)

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with OpenFile(f'output.txt', 'w') as f:
    f.write(f'This message written using {__file__}\n')