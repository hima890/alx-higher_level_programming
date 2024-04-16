#!/usr/bin/python3
"""Input output in python"""


import sys


def print_metrics(total_size, status_counts):
    """
    Prints the computed metrics.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing status code counts.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


def main():
    """
    Main function to read stdin line by line and compute metrics.
    """
    total_size = 0
    status_counts = {"200": 0, "301": 0, "400": 0, "401": 0,
                     "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            split_line = line.split(" ")
            total_size += int(split_line[-1])
            status_code = split_line[-2]
            if status_code in status_counts:
                status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
