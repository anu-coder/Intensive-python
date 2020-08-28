# Conv to num if possible
# TODO: My question on stackoverflow: https://t.ly/bbz8G
from helpers import str_to_num, unquoted_str

class Helper:
    @staticmethod
    def str_to_num(s):
        return(str_to_num(s))

    @staticmethod
    def unquoted_str(s):
        return(unquoted_str(s))


class StringNumber(Helper):

    def __init__(self, s):
        self.s = s

    @staticmethod
    def _hasQuotes(s):
        quotes = ["'", '"']
        for q in quotes:
            if q in s:
                return(True)

        return(False)

    @property
    def value(self):
        s = self.unquoted_str(self.s)
        if self._hasQuotes(s):
            return(self.s)

        return(self.str_to_num(s))

    def __repr__(self):
        return(f'{self.__class__.__name__}({repr(self.s)})')



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Convert a string to num')
    parser.add_argument(
        '-nums', dest='results', type=StringNumber, nargs='*'
    )
    args = parser.parse_args()
    results = args.results

    for r in results:
        print(repr(r.value), end=' ')
