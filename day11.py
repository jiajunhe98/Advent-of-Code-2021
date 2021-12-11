example="""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split("\n")

with open("day11.txt") as f:
    f = f.read().splitlines()

# Puzzle 1
def puzzle_1(data):
    counts = 0
    data = [[int(j) for j in i] for i in data]
    for i in range(100):
        c, data = update(data)
        counts += c
    return counts

def update(data):
    update_stack = [(i, j) for i in range(len(data)) for j in range(len(data[0]))]
    while update_stack:
        update_pos = update_stack.pop(-1)
        if update_pos[0] < 0 or\
            update_pos[1] < 0 or\
            update_pos[0] >= len(data) or\
            update_pos[1] >= len(data[0]):
            continue
        if data[update_pos[0]][update_pos[1]] <= 9:
            data[update_pos[0]][update_pos[1]] += 1
            if data[update_pos[0]][update_pos[1]] == 10:
                update_stack.append((update_pos[0] - 1, update_pos[1] - 1))
                update_stack.append((update_pos[0] - 0, update_pos[1] - 1))
                update_stack.append((update_pos[0] + 1, update_pos[1] - 1))
                update_stack.append((update_pos[0] - 1, update_pos[1] + 1))
                update_stack.append((update_pos[0] - 0, update_pos[1] + 1))
                update_stack.append((update_pos[0] + 1, update_pos[1] + 1))
                update_stack.append((update_pos[0] - 1, update_pos[1] + 0))
                update_stack.append((update_pos[0] + 1, update_pos[1] + 0))
    new_data = []
    count = 0
    for i in data:
        new_data.append([])
        for j in i:
            new_data[-1].append(j if j <=9 else 0)
            count += 0 if j <= 9 else 1
    return count, new_data

assert(puzzle_1(example)==1656)
print(puzzle_1(f))


# Puzzle 2
def puzzle_2(data):
    data = [[int(j) for j in i] for i in data]
    step = 0
    while 1:
        step += 1
        c, data = update(data)
        if c == len(data) * len(data[0]):
            return step
assert(puzzle_2(example)==195)
print(puzzle_2(f))



