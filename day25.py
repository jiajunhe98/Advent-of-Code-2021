example = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>""".splitlines()

with open("day25.txt") as f:
    f = f.read().splitlines()

# Puzzle 1
def process_data(data):
    return [[i for i in j] for j in data]

def move_1_step(data):
    move_count = 0
    move = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == ">":
                if data[i][(j+1) % len(data[0])] == ".":
                    move.append((i, j))
    for index in move:
        i, j = index
        data[i][j] = "."
        data[i][(j+1) % len(data[0])] = ">"
        move_count += 1

    move = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "v":
                if data[(i+1) % len(data)][j] == ".":
                    move.append((i, j))
    for index in move:
        i, j = index
        data[i][j] = "."
        data[(i+1) % len(data)][j] = "v"
        move_count += 1
    return data, move_count

def puzzle_1(data):
    data = process_data(data)
    move_count = 1
    step = 0
    while move_count:
        data, move_count = move_1_step(data)
        #print(data)
        step += 1
    return step

assert puzzle_1(example) == 58
print(puzzle_1(f))
