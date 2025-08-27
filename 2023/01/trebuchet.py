import pathlib
import sys


def parse(puzzle_input):
    data = [lines for lines in puzzle_input.split("\n")]
    return(data)


def value_sum(data):
    values = []
    sum = 0 
    for string in data:
        numerics = []
        for char in string:
            if char.isdecimal():
                numerics.append(char)
        new_value = int(numerics[0] + numerics[-1])
        values.append(new_value)
    for num in values:
        sum += num
    return sum

def dumber_value_sum(data):
    spelled_out_nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = parse(puzzle_input)
        solution = value_sum(data)
        print(solution)
