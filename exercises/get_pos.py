# Get the position of every element in a list.

def get_pos(lst: list) -> dict:

    res = {}
    for i, item in enumerate(lst):
        try:
            res[item].append(i)
        except KeyError:
            res[item] = [i]


    return(res)


def main():
    lst = [1, 1, 3, 5, 9, 9, 0, 8, 7, 8, 1]
    print(lst)
    print(get_pos(lst))


if __name__ == "__main__":
    main()