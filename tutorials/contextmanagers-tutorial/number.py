class Number:

    def __init__(self, string):
        self.string = string

    @property
    def value(self):
        return(int(self.string))

    def __enter__(self):
        return(self.value)

    def __exit__(self, exc_type, exc_val, traceback):
        pass


with Number('5') as i:
    print(i+1)
