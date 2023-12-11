import pathlib
import sys


def parse(puzzle_input):
    # parses input text file into list of lists of ints delimited by empty lines
    return [list(map(int, line.split("\n"))) for line in puzzle_input.split("\n\n")]


def calorie_counter(data):
    # takes parsed input, adds all values in each sublist, adds them to new list,
    # then orders values from greatest to least
    added_suplies = []
    for i in range(len(data)):
        new_value = 0
        for j in range(len(data[i])):
            new_value += data[i][j]
        added_suplies.append(new_value)

    added_suplies.sort(reverse=True)
    return (added_suplies)


def part1(data):
    # returns the value of highest elf's calorie count
    ordered_supplies = calorie_counter(data)
    return ordered_supplies[0]


def part2(data):
    # returns the value of the highest three elf's calorie count combined
    ordered_supplies = calorie_counter(data)
    return ordered_supplies[0] + ordered_supplies[1] + ordered_supplies[2]


def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

