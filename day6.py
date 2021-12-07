example="""3,4,3,1,2""".split(",")

with open("day6.txt") as f:
    f = f.read().splitlines()[0].split(",")

# Puzzle 1
def puzzle_1(data, day):
    for i in range(day):
        data = new_day(data)
    return len(data)

def new_day(data):
    new_fish = []
    for i in range(len(data)):
        data[i] = int(data[i]) - 1
        if data[i]  < 0:
            data[i] = 6
            new_fish.append(8)
    return data + new_fish
assert(puzzle_1(example, 80)==5934)
print(puzzle_1(f, 80))

# Puzzle 2
# Same as 1, but a cleverer way is needed
# 1 day pass: 1 -> 0 * 1; 2 -> 1 * 1; 3 -> 2 * 1; ...
# Only 0 -> 6 * 1 + 8 * 1

def puzzle_2(data, day):
    counts = {i: 0 for i in range(9)}
    for i in data:
        counts[i] += 1
    def new_day(counts):
        new_counts = {i: 0 for i in range(9)}
        for i in range(8):
            new_counts[i] = counts[i+1]
        new_counts[6] += counts[0]
        new_counts[8] += counts[0]
        return new_counts
    for i in range(day-1):
        counts = new_day(counts)
    return sum(counts.values())

assert(puzzle_2(example, 256)==26984457539)
print(puzzle_2(f, 256))