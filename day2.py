example = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''.split("\n")

with open("day2.txt") as f:
    f = f.read().splitlines()

# Puzzle 1
def puzzle_1(data):
    depth = 0
    length = 0
    for i in data:
        if i[0] == "f":
            length += int(i.split()[-1])
        if i[0] == "d":
            depth += int(i.split()[-1])
        if i[0] == "u":
            depth -= int(i.split()[-1])
    return depth * length

assert(puzzle_1(example) == 150)
print(puzzle_1(f))

# Puzzle 2
def puzzle_2(data):
    depth = 0
    length = 0
    aim = 0
    for i in data:
        if i[0] == "f":
            length += int(i.split()[-1])
            depth += aim * int(i.split()[-1])
        if i[0] == "d":
            aim += int(i.split()[-1])
        if i[0] == "u":
            aim -= int(i.split()[-1])
    return depth * length

assert(puzzle_2(example) == 900)
print(puzzle_2(f))