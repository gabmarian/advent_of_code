# https://adventofcode.com/2025/day/7

import argparse
import numbers
import copy


def process_diagram(input):
    splits = 0
    diagram = [string_as_chars(input[0])]
    paths = []

    for x in range(1, len(input)):
        cells = string_as_chars(input[x])
        for y in range(len(cells)):
            match cells[y]:
                case '.':
                    if diagram[x-1][y] in ('S', '|'):
                        cells[y] = '|'
                case '^':
                    if diagram[x-1][y] in ('|'):
                        splits += 1

                        set_cell_if_valid(cells, y-1, '|')
                        set_cell_if_valid(cells, y+1, '|')
        diagram.append(cells)

    print("Total splits:", splits)

    paths = copy.deepcopy(diagram)

    for y in range(len(paths[0])):
        if paths[0][y] == 'S':
            paths[0][y] = 1

    for x in range(1, len(input)):
        for y in range(len(paths[x])):
            if paths[x][y] == '|':
                paths[x][y] = 0
                if isinstance(paths[x-1][y], numbers.Number):
                    paths[x][y] += paths[x-1][y]
                if is_cell_valid(paths[x], y-1) and paths[x][y-1] == '^':
                    paths[x][y] += evaluate(paths[x-1][y-1])
                if is_cell_valid(paths[x], y+1) and paths[x][y+1] == '^':
                    paths[x][y] += evaluate(paths[x-1][y+1])

    path_count = 0
    for i in paths[-1]:
        if isinstance(i, numbers.Number):
            path_count += i

    # Puzzle 2 output
    print("Number of different timelines:", path_count)


def evaluate(cell):
    if isinstance(cell, numbers.Number):
        return cell
    else:
        return 0


def string_as_chars(string):
    return list(string.strip())


def is_cell_valid(cells, idx):
    return 0 <= idx < len(cells)


def set_cell_if_valid(cells, idx, val):
    if is_cell_valid(cells, idx):
        cells[idx] = val


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=str, required=True,
                        help="The name of the file to process")
    args = parser.parse_args()

    file = open(args.filename, "r")
    lines = file.readlines()

    process_diagram(lines)


if __name__ == "__main__":
    main()
