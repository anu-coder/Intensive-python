'''
Improve the repr of a class
'''

def fancy_repr(self):
    return f"I'm a {type(self).__name__}, with vars {vars(self)}"

def better_repr(c):
    c.__repr__ = fancy_repr
    return(c)


if __name__ == "__main__":
    @better_repr
    class Foo:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    f = Foo(1, 2)
    print(f)
