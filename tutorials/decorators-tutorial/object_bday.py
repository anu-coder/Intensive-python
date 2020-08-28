'''
Log the time as an attribute when the instance is created
'''
import time

def object_bday(cls):

    def modcls(*args, **kwargs):
        o = cls(*args, **kwargs)
        o._created_at = time.ctime()

        return(o)

    return(modcls)


if __name__ == "__main__":
    @object_bday
    class Foo:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    f = Foo(1, 2)
    print(f._created_at)
