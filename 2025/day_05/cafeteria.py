# https://adventofcode.com/2025/day/5

import argparse


def parse_input(lines):
    fresh_id_ranges = []
    ingredients = []
    for line in lines:
        parts = line.strip().split("-")
        if len(parts) == 2:
            fresh_id_ranges.append(
                {'start': int(parts[0]), 'end': int(parts[1])})
        else:
            if parts[0] == "":
                continue
            ingredients.append(int(parts[0]))

    return {'fresh_id_ranges': fresh_id_ranges, 'ingredients': ingredients}


def count_valid_ingredients(fresh_id_ranges, ingredients):
    valid_count = 0
    for ingredient in ingredients:
        ingredient_id = ingredient
        for id_range in fresh_id_ranges:
            if id_range['start'] <= ingredient_id <= id_range['end']:
                valid_count += 1
                break
    return valid_count


def join_id_ranges(fresh_id_ranges):
    sorted_ranges = sorted(fresh_id_ranges, key=lambda x: x['start'])
    merged_ranges = []
    current_range = sorted_ranges[0]

    for next_range in sorted_ranges[1:]:
        if current_range['end'] >= next_range['start'] - 1:
            current_range['end'] = max(current_range['end'], next_range['end'])
        else:
            merged_ranges.append(current_range)
            current_range = next_range

    merged_ranges.append(current_range)
    return merged_ranges


def count_all_valid_ingredients(fresh_id_ranges):
    total_count = 0
    for id_range in fresh_id_ranges:
        total_count += id_range['end'] - id_range['start'] + 1
    return total_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=str, required=True,
                        help="The name of the file to process")
    args = parser.parse_args()

    file = open(args.filename, "r")

    input = parse_input(file.readlines())

    merged_ranges = join_id_ranges(input['fresh_id_ranges'])
    print(count_valid_ingredients(merged_ranges, input['ingredients']))
    print(count_all_valid_ingredients(merged_ranges))


if __name__ == "__main__":
    main()
