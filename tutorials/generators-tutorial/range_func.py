# Simple understanding of generators using range
# NOTE: python builtin range function is NOT a generator
#       , which means it does not have a next method.
#       It is an iterable though, so when you use it in a
#       for loop, for will access __iter__ method, which will
#       return an iterator which will have a __next__ method
#       available

def my_range(start, end):
    cur = start
    while cur < end:
        yield cur
        cur += 1

    print('No more elements!')


r = my_range(1, 4)
for i in r:
    print(i)
    if i == 3: # This will prevent whatever is run after the yield
        break


# Basically when 3 is printed, the generator is exhausted, and when next is run
# again there will be no yield statements, so it will go on, to whatever block of
# code is after the yield in the function, then raise StopIteration. The for
# loop handles this StopIteration.