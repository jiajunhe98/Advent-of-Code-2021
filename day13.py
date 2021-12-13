example="""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split("\n")

with open("day13.txt") as f:
    f = f.read().splitlines()


import re

# Puzzle 1
def puzzle_1(data):
    points = []
    fold = []
    add_points = lambda x: points.append([int(x.split(",")[0]), int(x.split(",")[1])])
    add_fold = lambda x: fold.append((
        re.findall(r'([x, y])=([0-9]+)', string=x)[0][0],
        int(re.findall(r'([x, y])=([0-9]+)', string=x)[0][1])))
    current_add = add_points
    for i in data:
        if i == "":
            current_add = add_fold
            continue
        current_add(i)
    max_x, max_y = max([i[0] for i in points]), max([i[1] for i in points])
    points_folded = set()
    if fold[0][0] == "y":
        add_points_x = lambda x: x
        add_points_y = lambda y: y if y < fold[0][1] else max_y - y
        def add_point(x, y):
            if y != fold[0][1]:
                points_folded.add((add_points_x(x), add_points_y(y)))
    else:
        add_points_x = lambda x: x if x < fold[0][1] else max_x - x
        add_points_y = lambda y: y
        def add_point(x, y):
            if x != fold[0][1]:
                points_folded.add((add_points_x(x), add_points_y(y)))
    for i in points:
        add_point(*i)
    return len(points_folded)


assert(puzzle_1(example)==17)
print(puzzle_1(f))


def puzzle_2(data):
    points = []
    fold = []
    add_points = lambda x: points.append([int(x.split(",")[0]), int(x.split(",")[1])])
    add_fold = lambda x: fold.append((
        re.findall(r'([x, y])=([0-9]+)', string=x)[0][0],
        int(re.findall(r'([x, y])=([0-9]+)', string=x)[0][1])))
    current_add = add_points
    for i in data:
        if i == "":
            current_add = add_fold
            continue
        current_add(i)
    for f in fold:
        max_x, max_y = max([i[0] for i in points]), max([i[1] for i in points])
        points_folded = set()
        if f[0] == "y":
            add_points_x = lambda x: x
            add_points_y = lambda y: y if y < f[1] else max_y - y

            def add_point(x, y):
                if y != f[1]:
                    points_folded.add((add_points_x(x), add_points_y(y)))
        else:
            add_points_x = lambda x: x if x < f[1] else max_x - x
            add_points_y = lambda y: y

            def add_point(x, y):
                if x != f[1]:
                    points_folded.add((add_points_x(x), add_points_y(y)))
        for i in points:
            add_point(*i)
        points = list(points_folded)
    max_x, max_y = max([i[0] for i in points])+1, max([i[1] for i in points])+1
    pattern = [[" " for i in range(max_x)] for j in range(max_y)]
    for i in points:
        pattern[i[1]][i[0]] = "#"
    for i in pattern:
        for j in i:
            print(j, end="")
        print("\n", end="")
puzzle_2(example)
puzzle_2(f)