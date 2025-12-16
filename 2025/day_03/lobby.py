# https://adventofcode.com/2025/day/3

import argparse


def parse_input(lines):
    banks = []
    for line in lines:
        parsed_line = line.strip()
        banks.append(parsed_line)
    return banks


def process_battery_banks(banks, size):
    result = []

    for bank in banks:

        larges_part = ""
        max = 0

        for cut in range(size-1, -1, -1):

            for idx in range(max, len(bank) - cut):
                if int(bank[idx]) > int(bank[max]):
                    max = idx

            larges_part += bank[max]
            max = max + 1

        result.append(int(larges_part))

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=str, required=True,
                        help="The name of the file to process")
    args = parser.parse_args()

    file = open(args.filename, "r")

    banks = parse_input(file.readlines())

    result = process_battery_banks(banks, 12)
    # print(result)
    print(sum(result))


if __name__ == "__main__":
    main()
