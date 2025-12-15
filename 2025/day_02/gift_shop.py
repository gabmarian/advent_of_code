# https://adventofcode.com/2025/day/2

import argparse
import re

def parse_input(content):
    result = []
    ranges = content.split(",")
    for range_string in ranges:
        range = range_string.split("-")
        result.append({'start': int(range[0]), 'end': int(range[1])})
    return result


def get_invalid_ids(ranges):
    pattern = re.compile(r"^(\d+)(\1+)$")
    result = []
    for rng in ranges:
        for current_id in range(rng['start'], rng['end'] + 1):
            if pattern.match(str(current_id)):
                result.append(current_id)
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=str, required=True,
                        help="The name of the file to process")
    args = parser.parse_args()

    file = open(args.filename, "r")
    ranges = parse_input(file.readline())
    invalid_ids = get_invalid_ids(ranges)
    print(sum(invalid_ids))

if __name__ == "__main__":
    main()
