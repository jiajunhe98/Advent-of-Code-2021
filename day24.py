with open("day24.txt", "r") as f:
    f = f.read().splitlines()


# Puzzle 1

"""
Totally 2 kinds of order sets:
(a) if order[5][6:] > 0: z <- 26z + w + order[15][6:]
(b) if order[5][6:] < 0:
    (1) if x == 0 (i.e., z % 26 + order[5][6:] == w): z <- z // 26
    (2) if x == 1 (i.e., z % 26 + order[5][6:] != w): z <- z // 26 * 26 + w + order[15][6:]

There are in total 7 (a) and 7 (b), so every (b) needs to meet the condition of (1), otherwise the output cannot be the same as the input (0).

So to make it work, order sets need to be paired. Assuming the 1st in the pair is the a-th one and the 2nd is the b-th one. 
w_b - w_a = order_a[15][6:] + order_b[5][6:] need to be true. 

"""


def get_MONAD(data):
    MONAD = []
    for line in data:
        if line[:3] == "inp":
            MONAD.append([])
        MONAD[-1].append(line)
    return MONAD

def puzzle_1(data):
    MONAD = get_MONAD(data)
    order_stack = []
    index_stack = []
    constrains = {}
    for idx, order_set in enumerate(MONAD):
        if int(order_set[5][6:]) > 0:
            order_stack.append(int(order_set[15][6:]))
            index_stack.append(idx)
        else:
            last_order = order_stack.pop(-1)
            last_index = index_stack.pop(-1)

            constrains[last_index] = [max(1 - (last_order + int(order_set[5][6:])), 1), min(9 - (last_order + int(order_set[5][6:])), 9)]
            constrains[idx] = [max(1 + (last_order + int(order_set[5][6:])), 1), min(9 + (last_order + int(order_set[5][6:])), 9)]
    return "".join([str(constrains[i][-1]) for i in range(14)])

print(puzzle_1(f))

# Puzzle 2
def puzzle_2(data):
    MONAD = get_MONAD(data)
    order_stack = []
    index_stack = []
    constrains = {}
    for idx, order_set in enumerate(MONAD):
        if int(order_set[5][6:]) > 0:
            order_stack.append(int(order_set[15][6:]))
            index_stack.append(idx)
        else:
            last_order = order_stack.pop(-1)
            last_index = index_stack.pop(-1)

            constrains[last_index] = [max(1 - (last_order + int(order_set[5][6:])), 1),
                                      min(9 - (last_order + int(order_set[5][6:])), 9)]
            constrains[idx] = [max(1 + (last_order + int(order_set[5][6:])), 1),
                               min(9 + (last_order + int(order_set[5][6:])), 9)]
    return "".join([str(constrains[i][0]) for i in range(14)])

print(puzzle_2(f))
