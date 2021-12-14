example="""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".split("\n")



with open("day14.txt") as f:
    f = f.read().splitlines()

# Puzzle 1
def puzzle_1(data, steps=10):
    polymer = data[0]
    polymer = [(polymer[i-1], polymer[i]) for i in range(1, len(polymer))]
    insert = {(i[0], i[1]): i[-1] for i in data[2:]}
    for step in range(steps):
        new_polymer = []
        for i in polymer:
            try:
                new_polymer.append((i[0], insert[i]))
                new_polymer.append((insert[i], i[1]))
            except:
                new_polymer.append(i)
        polymer = new_polymer
    polymer = [polymer[0][0]] + [i[1] for i in polymer]
    counts = {}
    for i in polymer:
        try:
            counts[i] += 1
        except:
            counts[i] = 1
    return max(counts.values()) - min(counts.values())


assert(puzzle_1(example) == 1588)
print(puzzle_1(f))

# Puzzle 2
def puzzle_2(data, steps=40):
    polymer = {data[0][i:i+2]: 0 for i in range(len(data[0])-1)}
    for i in range(len(data[0])-1): polymer[data[0][i:i+2]] += 1
    insert = {i[:2]: (i[0]+i[-1], i[-1]+i[1]) for i in data[2:]}

    for step in range(steps):
        new_polymer = {}#polymer.copy()
        for i in polymer.keys():
            if polymer[i] > 0:
                def add_to_polymer(x, num):
                    try: new_polymer[x] += num
                    except: new_polymer[x] = num
                add_num = polymer[i]
                add_to_polymer(insert[i][0], add_num)
                add_to_polymer(insert[i][1], add_num)
                #new_polymer[i] -= add_num
        polymer = new_polymer
    counts = {data[0][-1]: 1}
    for i in polymer.keys():
        try:
            counts[i[0]] += polymer[i]
        except:
            counts[i[0]] = polymer[i]
    return max(counts.values()) - min(counts.values())

assert(puzzle_2(example, 40) == 2188189693529)
print(puzzle_2(f))