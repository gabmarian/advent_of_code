# https://adventofcode.com/2025/day/4

import argparse


def parse_input(lines):
    result = []
    for line in lines:
        parsed_line = line.strip()
        result.append(parsed_line)
    return result


def remove_paper_rolls(map):
    removed_count = 0
    new_map = []

    for x in range(0, len(map)):
        new_map_line = map[x]

        for y in range(0, len(map[x])):
            if map[x][y] != "@":
                continue

            occupied_neighbors = 0

            if symbol_is_in_position(map, x-1, y-1):
                occupied_neighbors += 1

            if symbol_is_in_position(map, x-1, y):
                occupied_neighbors += 1

            if symbol_is_in_position(map, x-1, y+1):
                occupied_neighbors += 1

            if symbol_is_in_position(map, x, y-1):
                occupied_neighbors += 1

            if symbol_is_in_position(map, x, y+1):
                occupied_neighbors += 1

            if symbol_is_in_position(map, x+1, y-1):
                occupied_neighbors += 1

            if symbol_is_in_position(map, x+1, y):
                occupied_neighbors += 1

            if symbol_is_in_position(map, x+1, y+1):
                occupied_neighbors += 1

            if occupied_neighbors < 4:
                removed_count += 1
                new_map_line = new_map_line[:y] + "x" + new_map_line[y+1:]

        new_map.append(new_map_line)
        # print(new_map_line)

    return (new_map, removed_count)


def symbol_is_in_position(map, x, y, symbol="@"):
    if x < 0 or y < 0:
        return False

    try:
        if (map[x][y]) == symbol:
            return True
    except IndexError:
        pass

    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=str, required=True,
                        help="The name of the file to process")
    args = parser.parse_args()

    file = open(args.filename, "r")

    map = parse_input(file.readlines())

    total_removed_count = 0

    while True:
        result_of_removal = remove_paper_rolls(map)
        map = result_of_removal[0]

        if (result_of_removal[1] == 0):
            break
        else:
            total_removed_count += result_of_removal[1]

    print(total_removed_count)


if __name__ == "__main__":
    main()
