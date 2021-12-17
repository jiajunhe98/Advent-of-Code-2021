# example1="""8A004A801A8002F478""".splitlines()
# example2="""EE00D40C823060""".splitlines()
# example3="""C0015000016115A2E0802F182340""".splitlines()
#
# with open("day16.txt") as f:
#     f = f.read().splitlines()
#
# # Puzzle 1
#
# _16_to_2 = lambda x: "".join([bin(int(i, 16))[2:] for i in x])
# data = _16_to_2(example1)
# nested_list = []
# current_position = 0
# length_limit = len(data)
#
# def process_list():
#     while 1:
#         if nested_list[-1][0] == "pos" and current_position >= nested_list[-1][1]:
#             nested_list.pop(-1)
#             if nested_list[-1][0] == "num":
#                 nested_list[-1][1] -= 1
#         elif nested_list[-1][0] == "num" and nested_list[-1][1] <= 0:
#             nested_list.pop(-1)
#             if nested_list[-1][0] == "num":
#                 nested_list[-1][1] -= 1
#         else:
#             break
#
#
#
#
# def parsing(current_position):
#     version = int(data[current_position:current_position+3], 2)
#     type = int(data[current_position+3:current_position+6], 2)
#
#     if type == 4:
#         nested_list.append(["num", 0])
#         curr_pos = current_position + 6
#         while 1:
#             if curr_pos + 5 >= length_limit or data[curr_pos] == 0:
#                 break
#             curr_pos += 5
#         curr_pos = min(curr_pos + 5, length_limit)
#         current_position = curr_pos
#         process_list()
#         parsing(current_position)
#     else:
#         if data[current_position+6] == "0":
#             nested_list.append(["pos", current_position + 22 + int(data[current_position+7: current_position+22], 2)])
#             current_position += 22
#             parsing(current_position)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # def parsing(x, num_packets=[-1]):
# #     if num_packets == []:
# #         return 0
# #     if num_packets[-1] == 0:
# #         num_packets.pop(-1)
# #     if len(x) < 6:
# #         return 0
# #     print(x)
# #
# #     version = int(x[:3], 2)
# #     #yield version
# #     print(version)
# #     type = int(x[3:6], 2)
# #     if type == 4:
# #         curr_pos = 6
# #         while 1:
# #             if curr_pos >= len(x) or x[curr_pos] == 0:
# #                 break
# #             curr_pos += 5
# #         x = x[curr_pos + 5:]
# #         new_num_packets = num_packets.copy()
# #         if new_num_packets[-1] is None:
# #             new_num_packets.pop(-1)
# #         else:
# #             new_num_packets[-1] = num_packets[-1] - 1
# #         parsing(x, new_num_packets)
# #     else:
# #         if x[6] == "0":
# #             new_num_packets = num_packets.copy()
# #             new_num_packets.append(None)
# #             parsing(x[7 + 15: 22 + int(x[7:7 + 15], 2), new_num_packets])
# #
# #             new_num_packets = num_packets.copy()
# #             new_num_packets[-1] = num_packets[-1] - 1
# #             parsing(x[22 + int(x[7:7 + 15], 2):])
# #         if x[6] == "1":
# #             new_num_packets = num_packets.copy()
# #             new_num_packets[-1] = num_packets[-1] - 1 if num_packets[-1] else None
# #             new_num_packets.append(int(x[7:7 + 11], 2))
# #             parsing(x[7 + 11:], new_num_packets)
# #
# # def puzzle_1(data):
# #     data = parsing(_16_to_2(data))
# #     #print(list(data))
# #     #return sum(list(data))
# #
# #
# # puzzle_1(example2)
# # #assert(puzzle_1(example1) == 16)
# # #assert(puzzle_1(example2) == 12)
#
