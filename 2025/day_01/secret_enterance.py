# https://adventofcode.com/2025/day/1

import argparse

class safe_dial:
    def __init__(self):
        self.dial = 50
        self.count_zero_clicked = 0
    
    def rotate_left(self, value):
        start_index = self.dial - 1
        end_index = self.dial - value - 1
        self.count_zero_clicked += (start_index // 100) - (end_index // 100)

        self.dial = (self.dial - value) % 100

    def rotate_right(self, value):
        self.count_zero_clicked += ( self.dial + value ) // 100       
        self.dial = ( self.dial + value ) % 100

def read_instructions_from_file(filename):
    instructions = []
    with open(filename,"r") as file:
        lines = file.readlines()
    for line in lines:
        parsed_line = line.strip()
        instructions.append({ 'direction' : parsed_line[0:1], 'value' : int(parsed_line[1:]) })
    return instructions    


def process_instructions(dial, instructions):
    for inst in instructions:
        if (inst['direction'] == "L"):
            dial.rotate_left(inst['value'])
        elif (inst['direction'] == "R"):
            dial.rotate_right(inst['value'])
        print(inst['direction'] + str(inst['value']), dial.dial, ",", dial.count_zero_clicked)     

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--filename", type=str, required=True, help="The name of the instruction file to process")
    args = parser.parse_args()

    dial = safe_dial()
    process_instructions(dial,read_instructions_from_file(args.filename))
    print(dial.count_zero_clicked)

if __name__ == "__main__":
    main()