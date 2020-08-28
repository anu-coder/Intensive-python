# Link: https://t.ly/5882b
# Greet the person and show current time

import datetime as dt

def greet(name, show_time):
    print(f'Hello {name}!')
    if show_time:
        print(f'The time right now is {dt.datetime.now()}')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Greet the user and show the time if requested.')

    parser.add_argument(
        '--name',
        required=True)
    # NOTE: dest is used for the namespace if it's provided.
    #       show_time seems like a more apt name for a logical.
    #       But the user would just like a simple -t or --time option.
    parser.add_argument('-t', '--time', dest='show_time', action='store_true')

    args = parser.parse_args()

    name, show_time = args.name, args.show_time
    greet(name, show_time)