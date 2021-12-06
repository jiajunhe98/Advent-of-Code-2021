example="""0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")

with open("day5.txt") as f:
    f = f.read().splitlines()

import re

# Puzzle 1
def puzzle_1(data):
    grid = {}
    for d in data:
        x1, y1, x2, y2 = re.findall(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)", d)[0]
        if x1 == x2:
            for i in range(min(int(y1), int(y2)), max(int(y1), int(y2))+1):
                try:
                    grid[(int(x1), i)] += 1
                except:
                    grid[(int(x1), i)] = 1
        elif y1 == y2:
            for i in range(min(int(x1), int(x2)), max(int(x1), int(x2))+1):
                try:
                    grid[(i, int(y1))] += 1
                except:
                    grid[(i, int(y1))] = 1
    return sum([i > 1 for i in grid.values()])

assert (puzzle_1((example)) == 5)
print(puzzle_1(f))


# Puzzle 2
def puzzle_2(data):
    grid = {}
    for d in data:
        x1, y1, x2, y2 = re.findall(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)", d)[0]
        if x1 == x2:
            for i in range(min(int(y1), int(y2)), max(int(y1), int(y2))+1):
                try:
                    grid[(int(x1), i)] += 1
                except:
                    grid[(int(x1), i)] = 1
        elif y1 == y2:
            for i in range(min(int(x1), int(x2)), max(int(x1), int(x2))+1):
                try:
                    grid[(i, int(y1))] += 1
                except:
                    grid[(i, int(y1))] = 1
        elif abs(int(x1)-int(x2)) == abs(int(y1)-int(y2)):
            for i in range(abs(int(x1)-int(x2))+1):
                sign = lambda x: -1 if x<0 else 1
                x = int(x1) + sign(int(x2)-int(x1)) * i
                y = int(y1) + sign(int(y2)-int(y1)) * i
                try:
                    grid[(x, y)] += 1
                except:
                    grid[(x, y)] = 1

    return sum([i > 1 for i in grid.values()])

assert (puzzle_2((example)) == 12)
print(puzzle_2(f))

