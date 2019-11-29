# Just a how to iterate

lst = [1, 2, 3, 4, 5, 6]
lst_iter = iter(lst)

while True:
    try:
        item = next(lst_iter)
        print(item)
    except StopIteration:
        break

print()

# If we know the length of an array
n = 6

i=0
while i < n:
    print(lst[i])
    i += 1
