import pathlib
import sys


def parse(puzzle_input):
    data = [lines for lines in puzzle_input.split("\n")]
    return data


def dupe_checker(lst1, lst2):
    dupe_item = ""
    for n in range(len(lst2)):
        if lst2[n] in lst1:
            dupe_item = lst2[n]

    return dupe_item


def priority_total(dupe_items):
    item_priority = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52
    }

    total = 0

    for j in range(len(dupe_items)):
        value = item_priority.get(dupe_items[j])
        total += value
    
    return total


def part1(data):
    total = 0
    dupe_items = []
    for i in range(len(data)):
        # breaks string into equal halves
        current_line = data[i]
        newline_1 = current_line[:(len(current_line)//2)]
        newline_2 = current_line[(len(current_line)//2):]

        # finds duplicate char in both compartments and adds it to list
        dupe_items.append(dupe_checker(newline_1, newline_2))

        # calculates total based on item priority values
    total = priority_total(dupe_items)
    return total


def part2(data):
    total = 0
    # groups rucksacks into groups of 3
    def chunk (lst, n):
        return zip(*[iter(lst)]*n)

    chunked_data = []
    for l in chunk(data, 3):
        chunked_data.append(list(l))
    
    # finds duplicate char in all three rucksacks and adds them to list
    dupe_items = []
    for i in range(len(chunked_data)):
        for n in range(len(chunked_data[i][0])):
            if (chunked_data[i][0][n] in chunked_data[i][1]) and (chunked_data[i][0][n] in chunked_data[i][2]):
                dupe_items.append(chunked_data[i][0][n])
                break

    # calculates total based on item priority values
    total = priority_total(dupe_items)
    return total


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
        print("\n".join(str(solution) for solution in solutions) + "\n")
