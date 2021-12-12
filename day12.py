example_1 = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''.splitlines()

example_2 = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''.splitlines()

example_3="""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".splitlines()

with open("day12.txt") as f:
    f = f.read().splitlines()

# Puzzle 1
def puzzle_1(data):
    paths = {}
    for i in data:
        a, b = tuple(i.split("-"))


        def add_path(s, e):
            try:
                paths[s].append(e)
            except:
                paths[s] = []
                paths[s].append(e)
        add_path(a, b)
        add_path(b, a)

    # BFS
    num_path = 0
    Paths = [("start", [], set())]
    while Paths:
        #print(Paths)
        current_state, current_paths, small_caves = Paths.pop()
        current_paths, small_caves = current_paths.copy(), small_caves.copy()
        current_paths.append(current_state)

        if current_state == "end":
            num_path += 1
            continue
        if current_state.islower():
            small_caves.add(current_state)
        for next_state in paths[current_state]:
            if next_state not in small_caves:
                Paths.append((next_state, current_paths, small_caves))
    return num_path

assert(puzzle_1(example_1) == 226)
assert(puzzle_1(example_2) == 10)
print(puzzle_1(f))





# Puzzle 2
def puzzle_2(data):
    paths = {}
    for i in data:
        a, b = tuple(i.split("-"))


        def add_path(s, e):
            try:
                paths[s].append(e)
            except:
                paths[s] = []
                paths[s].append(e)
        add_path(a, b)
        add_path(b, a)

    # BFS
    num_path = 0
    Paths = [("start", [], set(), 0)]
    while Paths:
        #print(Paths)
        current_state, current_paths, small_caves, twice_small_cave = Paths.pop()
        current_paths, small_caves = current_paths.copy(), small_caves.copy()
        current_paths.append(current_state)

        if current_state == "end":
            num_path += 1
            continue
        if current_state.islower():
            small_caves.add(current_state)
        for next_state in paths[current_state]:
            if next_state not in small_caves:
                Paths.append((next_state, current_paths, small_caves, twice_small_cave))
            elif twice_small_cave == 0 and next_state != 'start':
                Paths.append((next_state, current_paths, small_caves, 1))
        # if twice_small_cave == 0 and current_state.islower():
        #     for next_state in paths[current_state]:
        #         if next_state not in small_caves:
        #             Paths.append((next_state, current_paths.copy(), _small_caves.copy(), 1))

    return num_path

assert(puzzle_2(example_1) == 3509)
assert(puzzle_2(example_2) == 36)
assert(puzzle_2(example_3) == 103)
print(puzzle_2(f))