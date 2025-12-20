# https://adventofcode.com/2025/day/6

import argparse


def sum_by_horizontal_numbers(lines):
    matrix = []
    operators = []

    pos = -1
    for line in lines:
        pos += 1
        elements = line.strip().split()

        if pos == len(lines) - 1:
            for element in elements:
                operators.append(element)
        else:
            numbers = []
            for element in elements:
                numbers.append(int(element))
            matrix.append(numbers)

    total = 0
    for j in range(len(operators)):
        match operators[j]:
            case '*':
                subtotal = 1
            case '+':
                subtotal = 0
        for i in range(len(matrix)):
            match operators[j]:
                case '*':
                    subtotal = matrix[i][j] * subtotal
                case '+':
                    subtotal = matrix[i][j] + subtotal
        total += subtotal
    return total


def sum_by_vertical_numbers(lines):
    current_operator = ''
    columns = len(lines[0]) -1  # to ignore newline character
    numbers = []
    total = 0

    for j in range(0, columns): 
        numc = ""
        for i in range(0, len(lines)):
            if i < len(lines) - 1:
                numc = numc + lines[i][j]
            elif lines[i][j] in ('*', '+'):
                current_operator = lines[i][j]
        
        if numc.isspace() == False:
            number = int(numc)
            numbers.append(number)

        if numc.isspace() or j == columns - 1:
            match current_operator:
                case '*':
                    subtotal = 1
                case '+':
                    subtotal = 0
            for x in numbers:
                match current_operator:
                    case '*':
                        subtotal = x * subtotal
                    case '+':
                        subtotal = x + subtotal
            total += subtotal
            numbers = []

    return total

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=str, required=True,
                        help="The name of the file to process")
    args = parser.parse_args()

    file = open(args.filename, "r")
    lines = file.readlines()

    print(sum_by_horizontal_numbers(lines))
    print(sum_by_vertical_numbers(lines))


if __name__ == "__main__":
    main()
