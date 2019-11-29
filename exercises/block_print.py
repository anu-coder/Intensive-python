# Suppress print output from a function
import contextlib
import sys


class DummyFile(object):
    def write(self, x): pass

@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = DummyFile()
    yield
    sys.stdout = save_stdout


def main():
    def add_one(n):
        try:
            res = n + 1
        except Exception as e:
            res = 'NA'
            print(e)

        return(res)

    # nostdout is working fine, even when an exception is encountered inside
    # the func
    with nostdout():
        add_one('1')

    print('This should print!')


if __name__ == "__main__":
    main()
