# Sort various objects by a key in python
from operator import itemgetter, attrgetter

# dictionaries (see https://t.ly/kAY9)
d = {'c': 1, 'a':2 , 'b': 0}
print(d)
d_sorted = dict(sorted(d.items(), key=lambda kv: kv[0])) # by key
print(d_sorted) # by key
d_sorted = dict(sorted(d.items(), key=itemgetter(1))) # by value
print(d_sorted)

# One list by square of another
lst1 = [1, 2, 3]
lst2 = [-2, 1, 0]

lst_of_tup = sorted(zip(lst1, lst2), key=lambda kv: kv[1]**2)
lst1_n, lst2_n = list(zip(*lst_of_tup))
print(lst1_n, lst2_n, sep='\n')

# A list of lists by specified index
lst = [['Rash', 4, 28], ['Varsha', 2, 20], ['Nikhil', 1, 20], ['Akshat', 3, 21]]
print(sorted(lst, key=lambda x: x[1]))
print(sorted(lst, key=itemgetter(1)))
## Sort by multiple keys
print(sorted(lst, key=itemgetter(2, 0, 1)))
print(sorted(lst, key=lambda x: (x[2], x[0], x[1])))

# objects

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def _get_attr_str(self, attrs):
        attr_str = ', '.join([f'{attr}={self.__getattribute__(attr)}'
                              for attr in attrs])
        return(attr_str)

    def __repr__(self):
        attr_str = self._get_attr_str(['name', 'age', 'salary'])
        return(f'{self.__class__.__name__}({attr_str})')


e1 = Employee('Babita', 25, 40000)
e2 = Employee('Animesh', 23, 30000)
e3 = Employee('Chetan', 30, 50000)

staff = [e1, e2, e3]
print(staff)

print(sorted(staff, key=lambda e: e.__getattribute__('salary')))
print(sorted(staff, key=attrgetter('age')))
