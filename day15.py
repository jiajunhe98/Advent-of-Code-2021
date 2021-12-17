example="""1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".split("\n")



with open("day15.txt") as f:
    f = f.read().splitlines()

import time

# Puzzle 1
def puzzle_1(data):

    data = [[int(i) for i in j] for j in data]

    paths = [[1e8 for i in j] for j in data]
    paths[0][0] = 0
    while 1:
        change_num = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                def get_ij(i, j):
                    try: return paths[i][j]
                    except: return 1e8

                last_value = paths[i][j]
                paths[i][j] = min(get_ij(i - 1, j) + data[i][j],
                                  get_ij(i + 1, j) + data[i][j],
                                  get_ij(i, j - 1) + data[i][j],
                                  get_ij(i, j + 1) + data[i][j], paths[i][j])
                if paths[i][j] != last_value:
                    change_num += 1
        if change_num == 0:
            return paths[-1][-1]

assert(puzzle_1(example) == 40)
time_start = time.time()
print(puzzle_1(f))
print("time: ", time.time() - time_start)




# Puzzle 2
def puzzle_2(data):
    expand_entry = lambda x, i: (int(x)+i) % 10 + 1 if (int(x)+i) > 9 else int(x)+i
    def data_row(x):
        row = []
        for i in range(5):
            row += [expand_entry(char, i) for char in x]
        return row
    data = [data_row(x) for x in data]
    len_data = len(data)
    for i in range(1, 5):
        for k in range(len_data):
            data.append([expand_entry(j, i) for j in data[k]])

    paths = [[1e8 for i in j] for j in data]
    paths[0][0] = 0
    while 1:
        change_num = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                def get_ij(i, j):
                    try: return paths[i][j]
                    except: return 1e8

                last_value = paths[i][j]
                paths[i][j] = min(get_ij(i - 1, j) + data[i][j],
                                  get_ij(i + 1, j) + data[i][j],
                                  get_ij(i, j - 1) + data[i][j],
                                  get_ij(i, j + 1) + data[i][j], paths[i][j])
                if paths[i][j] != last_value:
                    change_num += 1
        if change_num == 0:
            return paths[-1][-1]



assert(puzzle_2(example) == 315)

time_start = time.time()
print(puzzle_2(f))
print("time: ", time.time() - time_start)







