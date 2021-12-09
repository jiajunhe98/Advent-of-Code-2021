example="""2199943210
3987894921
9856789892
8767896789
9899965678""".split("\n")

with open("day9.txt") as f:
    f = f.read().splitlines()


# Puzzle 1

def puzzle_1(data):
    res = 0
    data = [[9] * (len(data[0]) + 2)] + [[9] + [int(j)  for j in i] + [9] for i in data] + [[9] * (len(data[0]) + 2)]
    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            if data[i][j] < min(data[i][j-1], data[i-1][j], data[i][j+1], data[i+1][j]):
                res += data[i][j] + 1
    return res

assert(puzzle_1(example) == 15)
print(puzzle_1(f))

# Puzzle 2
def puzzle_2(data):
    basin_size = []
    data = [[9] * (len(data[0]) + 2)] + [[9] + [int(j) for j in i] + [9] for i in data] + [[9] * (len(data[0]) + 2)]
    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            if data[i][j] != 9:
                # Start BFS
                nodes = [(i, j)]
                data[i][j] = 9
                size = 0
                while len(nodes) != 0:
                    node = nodes.pop()
                    size += 1
                    def append_to_nodes(x, y):
                        if data[x][y] != 9: nodes.append((x, y)); data[x][y] = 9
                    append_to_nodes(node[0] - 1, node[1])
                    append_to_nodes(node[0], node[1] - 1)
                    append_to_nodes(node[0] + 1, node[1])
                    append_to_nodes(node[0], node[1] + 1)
                basin_size.append(size)
    basin_size.sort()
    return basin_size[-1] * basin_size[-2] * basin_size[-3]
assert (puzzle_2(example) == 1134)
print(puzzle_2(f))



