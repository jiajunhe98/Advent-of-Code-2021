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
    data = [[1e8]+[int(i) for i in j]+[1e8] for j in data]
    data.append([1e8]*len(data[0]))
    data.insert(0, [1e8] * len(data[0]))

    length = len(data)
    width = len(data[0])

    index_to_position = lambda x: (x // width, x % width)
    position_to_index = lambda x, y: x * width + y

    # Dijkstra
    paths = [1e8] * (length * width)
    fixed_nodes = {width + 1}
    shortest_paths = {width + 1: 0}
    current_node = width + 1
    current_path_length = 0
    while 1:
        x, y = index_to_position(current_node)
        add_list = {}
        for add in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
            if paths[position_to_index(*add)] > data[add[0]][add[1]] + current_path_length \
                    and position_to_index(*add) not in fixed_nodes:
                paths[position_to_index(*add)] = min(data[add[0]][add[1]] + current_path_length,
                                               paths[position_to_index(*add)])
                add_list[paths[position_to_index(*add)]] = position_to_index(*add)

        current_path_length = min(paths)
        current_node = paths.index(current_path_length)

        fixed_nodes.add(current_node)
        shortest_paths[current_node] = current_path_length
        paths[current_node] = 1e8

        if current_node == (length - 1) * width - 2:

            return current_path_length
assert(puzzle_1(example) == 40)
time_start = time.time()
print(puzzle_1(f))
print("time: ", time.time() - time_start)

#
#
# # Puzzle 2
# def puzzle_2(data):
#     data = [[int(i) for i in j] +
#             [(int(i)+1) % 10 + 1 if (int(i)+1) > 9 else int(i)+1 for i in j] +
#             [(int(i)+2) % 10 + 1 if (int(i)+2) > 9 else int(i)+2 for i in j] +
#             [(int(i)+3) % 10 + 1 if (int(i)+3) > 9 else int(i)+3 for i in j] +
#             [(int(i)+4) % 10 + 1 if (int(i)+4) > 9 else int(i)+4 for i in j] for j in data]
#     len_data = len(data)
#     for i in range(4):
#         for k in range(len_data):
#             data.append([(j+i+1) % 10 + 1 if j+i+1 > 9 else j+i+1 for j in data[k]])
#
#
#     data = [[1e8]+[i for i in j]+[1e8] for j in data]
#     data.append([1e8]*len(data[0]))
#     data.insert(0, [1e8] * len(data[0]))
#
#     length = len(data)
#     width = len(data[0])
#
#     index_to_position = lambda x: (x // width, x % width)
#     position_to_index = lambda x, y: x * width + y
#
#     # Dijkstra
#     paths = [1e8] * (length * width)
#     fixed_nodes = {width + 1}
#     shortest_paths = {width + 1: 0}
#     current_node = width + 1
#     current_path_length = 0
#     while 1:
#         x, y = index_to_position(current_node)
#         add_list = {}
#         for add in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
#             if paths[position_to_index(*add)] > data[add[0]][add[1]] + current_path_length \
#                     and position_to_index(*add) not in fixed_nodes:
#                 paths[position_to_index(*add)] = min(data[add[0]][add[1]] + current_path_length,
#                                                paths[position_to_index(*add)])
#                 add_list[paths[position_to_index(*add)]] = position_to_index(*add)
#
#         current_path_length = min(paths)
#         current_node = paths.index(current_path_length)
#
#         fixed_nodes.add(current_node)
#         shortest_paths[current_node] = current_path_length
#         paths[current_node] = 1e8
#
#         if current_node == (length - 1) * width - 2:
#
#             return current_path_length
# assert(puzzle_2(example) == 315)
#
# time_start = time.time()
# print(puzzle_2(f))
# print("time: ", time.time() - time_start)
#
#




