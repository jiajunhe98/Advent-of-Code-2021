example = '''199
200
208
210
200
207
240
269
260
263'''.split()

with open("day1.txt") as f:
    f = f.read().splitlines()

# Puzzle 1
def puzzle_1(data):
    return sum([int(data[i]) > int(data[i-1]) for i in range(1, len(data))])
assert(puzzle_1(example) == 7)
print(puzzle_1(f))

# Puzzle 2
def puzzle_2(data):
    windows = [int(data[i]) + int(data[i-1]) + int(data[i-2]) for i in range(2, len(data))]
    return puzzle_1(windows)
assert(puzzle_2(example) == 5)
print(puzzle_2(f))






#
#
# f = np.loadtxt("day1.txt")
# ans1 = np.sum(f[1:] > f[:-1])
# print(ans1)
#
# # Puzzle 2
# windows = f[:-2] + f[1:-1] + f[2:]
# ans2 = np.sum(windows[1:] > windows[:-1])
# print(ans2)

