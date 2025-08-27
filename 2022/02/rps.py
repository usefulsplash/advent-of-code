import pathlib
import sys

def parse(puzzle_input):
    data = [line.split(" ") for line in puzzle_input.split("\n")]
    return data

def part1(data):
    total = 0
    for i in range(len(data)):
        score = 0
        if data[i][1] == "X":
            score += 1
        if data[i][1] == "Y":
            score += 2
        if data[i][1] == "Z":
            score += 3
        score += rps(data[i][0], data[i][1])
        total += score
    return total


def part2(data):
    total = 0
    for i in range(len(data)):
        score = 0
        if data[i][1] == "X":
            if data[i][0] == "A":
                score += (rps(data[i][0], "Z") + 3)
            if data[i][0] == "B":
                score += (rps(data[i][0], "X") + 1)
            if data[i][0] == "C":
                score += (rps(data[i][0], "Y") + 2)
        if data[i][1] == "Y":
            if data[i][0] == "A":
                score += (rps(data[i][0], "X") + 1)
            if data[i][0] == "B":
                score += (rps(data[i][0], "Y") + 2)
            if data[i][0] == "C":
                score += (rps(data[i][0], "Z") + 3)
        if data[i][1] == "Z":
            if data[i][0] == "A":
                score += (rps(data[i][0], "Y") + 2)
            if data[i][0] == "B":
                score += (rps(data[i][0], "Z") + 3)
            if data[i][0] == "C":
                score += (rps(data[i][0], "X") + 1)
        total += score
    return total

def rps(opp, user):
    if (opp == "A" and user == "Z") or (opp == "B" and user == "X") or (opp == "C" and user == "Y"):
        return 0
    if (opp == "A" and user == "X") or (opp == "B" and user == "Y") or (opp == "C" and user == "Z"):
        return 3
    if (opp == "A" and user == "Y") or (opp == "B" and user == "Z") or (opp == "C" and user == "X"):
        return 6


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
