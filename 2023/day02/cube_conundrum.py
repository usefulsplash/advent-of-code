import pathlib
import sys


def parse():
    test = 1
    return test


def cube_conundrum():
    test = 1
    return test


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = parse(puzzle_input)
        solution = cube_conundrum(data)
        print(solution)
