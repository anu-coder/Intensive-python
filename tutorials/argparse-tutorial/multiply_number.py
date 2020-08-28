# Tutorial link https://t.ly/kwl3
# CLI to multiply a number by another

def multiply(n: float, m: float) -> float:
    return(n*m)



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Multiplies the input <n> by <m>'
    )

    parser.add_argument(
        'n', type=float, help='Input number to be multiplied'
    )

    parser.add_argument(
        '-m', '--optional-multiplier',
        type=float, default=1,
        help='multiplier for <n> : (default: 1)'
    )

    # TODO: Read about namespaces in python.
    namespace = parser.parse_args()
    # NOTE: Use attrgetter in case of too many attrs
    #       or just define your own attrgetter.
    n, m = namespace.n, namespace.optional_multiplier

    res = n*m
    print(res)
