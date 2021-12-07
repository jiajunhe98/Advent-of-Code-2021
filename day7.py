example="""16,1,2,0,4,2,7,1,2,14""".split(",")

with open("day7.txt") as f:
    f = f.read().splitlines()[0].split(",")

# Puzzle 1
# Minimize the Manhattan distance
def puzzle_1(data):
    data = [float(i) for i in data]
    data.sort()
    if len(data) % 2 == 1:
        return sum([abs(i - data[len(data) // 2]) for i in data])
    else:
        return sum([abs(i - (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2) for i in data])


assert (puzzle_1(example) == 37)
print(puzzle_1(f))

# Puzzle 2
def puzzle_2(data):
    data = [float(i) for i in data]
    pos_l = int(sum(data) / len(data))
    pos_h= int(sum(data) / len(data)) + 1
    return min(sum([(abs(i - pos_l)) * (abs(i - pos_l) + 1) / 2 for i in data]),
               sum([(abs(i - pos_h)) * (abs(i - pos_h) + 1) / 2 for i in data]))

assert(puzzle_2(data=example) == 168)
print(puzzle_2(f))

