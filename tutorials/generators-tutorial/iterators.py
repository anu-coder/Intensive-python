# How a simple for loop works
# sorta inside the hood


lst = [0, 1, 2, 3, 4, 5]
# acquire the iterator from the iterable
# for loop will call the __iter__ method on the iterable (lst)
# This method will return an iterable
# this iterable object has a __next__ method
# which is used in every loop unless a StopIteration exception is raised

lst_iter = iter(lst) # or lst.__iter__()

while True:
    try:
        curval = next(lst_iter)
        print(curval)
    except StopIteration:
        break