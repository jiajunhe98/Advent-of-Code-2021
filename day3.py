example = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''.split("\n")

with open("day3.txt") as f:
    f = f.read().splitlines()

# Puzzle 1
def puzzle_1(data):
    length = len(data[0])
    count_zero = [0] * length
    for i in range(length):
        for j in range(len(data)):
            count_zero[i] += 1 if data[j][i] == "0" else 0
    gamma = [0 if i > len(data) / 2 else 1 for i in count_zero][::-1]
    epsilon = [1 if i > len(data) / 2 else 0 for i in count_zero][::-1]
    gamma = sum([gamma[i] * 2 ** i for i in range(len(gamma))])
    epsilon = sum([epsilon[i] * 2 ** i for i in range(len(epsilon))])
    return epsilon * gamma

assert(puzzle_1(example)==198)
print(puzzle_1(f))

# Puzzle 2
def puzzle_2(data):
    oxygen = sum([2 ** i * int(iteration(data, oxygen=1)[::-1][i]) for i in range(len(data[0]))])
    co2 = sum([2 ** i * int(iteration(data, oxygen=0)[::-1][i]) for i in range(len(data[0]))])
    return co2 * oxygen

def iteration(l, index=0, oxygen=1):
    if len(l) == 1:
        return l[0]
    count = sum([1-int(i[index]) for i in l])
    judge = lambda count, oxygen: count > len(l) / 2 if oxygen else count <= len(l) / 2
    if judge(count, oxygen):
        return iteration(list(filter(lambda x: x[index] == "0", l)), index+1, oxygen)
    return iteration(list(filter(lambda x: x[index] == "1", l)), index+1, oxygen)


assert(puzzle_2(example)==230)
print(puzzle_2(f))