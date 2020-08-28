'''
Combining two decorators
'''
from object_bday import object_bday
from better_repr import better_repr

@object_bday
@better_repr
class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


f = Foo(1, 2)
print(f)