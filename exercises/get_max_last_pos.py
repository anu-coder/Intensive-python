# Get the position of the last maximum in a list

def get_max_last_pos(lst: list) -> int:

    i_max = 0
    max_val = lst[0]

    for i, n in enumerate(lst):
        if n >= max_val:
            i_max = i
            max_val = n

    return(i_max)


def main():
    print(get_max_last_pos([1, 4, 5, 9, 8, 9, 3]))


if __name__ == "__main__":
    main()
