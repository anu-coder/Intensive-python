# Link: https://t.ly/5882b
# Sum a variable number of arguments provided


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description=('Return the sum of the given numbers')
    )

    parser.add_argument(
        'num', type=int, nargs='*'
    )

    args = parser.parse_args()
    numbers = args.num
    print(sum(numbers))
