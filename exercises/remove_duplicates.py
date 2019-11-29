'''
With a given list [12,24,35,24,88,120,155,88,120,155],
write a program to print this list after removing all duplicate values
with original order reserved.
'''

def remove_duplicates(lst: list, method='A'):

    if method == 'A':
        seen = []

        for i, item in enumerate(lst):
            if item not in seen:
                seen.append(item)

        return(seen)

    elif method == 'B':
        # NOTE: Doesn't make sense though, you could just call set().
        return(list({item for item in lst}))




if __name__ == '__main__':
    print(remove_duplicates([1, 1, 2, 3, 2, 5, 6]))