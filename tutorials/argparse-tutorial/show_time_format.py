# Link: https://t.ly/5882b
# Show time in a specific format
import datetime as dt
import time

def show_current_time(fmt):

    if fmt == 'tz':
        return(dt.datetime.now(dt.timezone.utc))

    return(
        {
            'std': dt.date.today,
            'iso': dt.datetime.now().isoformat,
            'unix': time.time,
        }[fmt]()
    )


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Show current time in a specific format'
    )

    parser.add_argument(
        '--now', dest='format',
        choices=['std', 'iso', 'unix', 'tz'],
        help='show datetime in the given format'
    )

    args = parser.parse_args()
    fmt = args.format
    print(show_current_time(fmt))