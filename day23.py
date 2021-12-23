example = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########""".splitlines()

with open("day23.txt") as f:
    f = f.read().splitlines()

import time

# Puzzle 1
def puzzle_1(data):
    state = [data[1], data[2], "##"+data[3][2:]+"##"]
    state = [[i for i in j] for j in state]
    state_energy = {state_to_tuple(state): 0}
    state_stack = [state]
    while state_stack:
        state = state_stack.pop()
        new_energy, new_stack = move(state, state_energy[state_to_tuple(state)], state_energy)
        state_energy = new_energy
        state_stack += new_stack
    min_energy = 1e8
    final_state = [["#"] + ["."] * 11 + ["#"], [i for i in "###A#B#C#D###"], [i for i in "###A#B#C#D###"]]
    for i in state_energy.keys():
        if all([i[j] == state_to_tuple(final_state)[j] for j in range(len(state_to_tuple(final_state)))]):
            #print(i)
            min_energy = min(min_energy, state_energy[i])
    return min_energy


def move(state, current_energy, state_energy):
    new_states_stack = []
    index = {"A": 3, "B": 5, "C": 7, "D": 9}
    energy = {"A": 1, "B": 10, "C": 100, "D": 1000}
    # move the nodes in the hallway
    for idx, i in enumerate(state[0]):
        if i in index.keys():
            if state[1][index[i]] == "." and \
                    state[2][index[i]] == "." and \
                    all([state[0][pos] == "." for pos in range(idx + 1 if idx - index[i] < 0 else idx - 1,
                                                               index[i], 1 if idx - index[i] < 0 else -1)]):
                new_state = [s.copy() for s in state]
                new_state[0][idx] = "."
                new_state[2][index[i]] = i
                try:
                    if state_energy[state_to_tuple(new_state)] > current_energy + (2 + abs(idx - index[i])) * energy[i]:
                        state_energy[state_to_tuple(new_state)] = current_energy + (2 + abs(idx - index[i])) * energy[i]
                        new_states_stack.append(new_state)
                except:
                    state_energy[state_to_tuple(new_state)] = current_energy + (2 + abs(idx - index[i])) * energy[i]
                    new_states_stack.append(new_state)
            if state[1][index[i]] == "." and \
                    state[2][index[i]] == i and \
                    all([state[0][pos] == "." for pos in range(idx + 1 if idx - index[i] < 0 else idx - 1,
                                                               index[i], 1 if idx - index[i] < 0 else -1)]):
                new_state = [s.copy() for s in state]
                new_state[0][idx] = "."
                new_state[1][index[i]] = i
                try:
                    if state_energy[state_to_tuple(new_state)] > current_energy + (1 + abs(idx - index[i])) * energy[i]:
                        state_energy[state_to_tuple(new_state)] = current_energy + (1 + abs(idx - index[i])) * energy[i]
                        new_states_stack.append(new_state)
                except:
                    state_energy[state_to_tuple(new_state)] = current_energy + (1 + abs(idx - index[i])) * energy[i]
                    new_states_stack.append(new_state)

    # move the nodes in the place adjacent to the hallway
    for idx, i in enumerate(state[1]):
        if i in index.keys():
            if idx != index[i] or state[2][idx] != i:
                for target_idx in [1, 2, 4, 6, 8, 10, 11]:
                    if all([state[0][pos] == "." for pos in range(idx,
                                                                  target_idx + 1 if idx - target_idx < 0 else target_idx - 1,
                                                                  1 if idx - target_idx < 0 else -1)]):
                        new_state = [s.copy() for s in state]
                        new_state[1][idx] = "."
                        new_state[0][target_idx] = i
                        try:
                            if state_energy[state_to_tuple(new_state)] > current_energy + (1 + abs(idx - target_idx)) * energy[i]:
                                state_energy[state_to_tuple(new_state)] = current_energy + (1 + abs(idx - target_idx)) * \
                                energy[i]
                                new_states_stack.append(new_state)
                        except:
                            state_energy[state_to_tuple(new_state)] = current_energy + (1 + abs(idx - target_idx)) * energy[i]
                            new_states_stack.append(new_state)

    # move the nodes in the 3rd row
    for idx, i in enumerate(state[2]):
        if i in index.keys():
            if idx != index[i] and state[1][idx] == ".":
                for target_idx in [1, 2, 4, 6, 8, 10, 11]:
                    if all([state[0][pos] == "." for pos in range(idx,
                                                                  target_idx + 1 if idx - target_idx < 0 else target_idx - 1,
                                                                  1 if idx - target_idx < 0 else -1)]):
                        new_state = [s.copy() for s in state]
                        new_state[2][idx] = "."
                        new_state[0][target_idx] = i
                        try:
                            if state_energy[state_to_tuple(new_state)] > current_energy + (2 + abs(idx - target_idx)) * energy[i]:
                                state_energy[state_to_tuple(new_state)] = current_energy + (2 + abs(idx - target_idx)) * energy[i]
                                new_states_stack.append(new_state)
                        except:
                            state_energy[state_to_tuple(new_state)] = current_energy + (2 + abs(idx - target_idx)) * \
                                                                      energy[i]
                            new_states_stack.append(new_state)
    return state_energy, new_states_stack


def state_to_tuple(state: list):
    return tuple([j for i in state for j in i])

def tuple_to_state(state: tuple):
    list_state = list(state)
    return [list_state[0:13], list_state[13:26], list_state[26:39]] if len(state) == 39 else \
        [list_state[0:13], list_state[13:26], list_state[26:39], list_state[39:39+13], list_state[39+13:39+26]]

assert(puzzle_1(example) == 12521)
print(puzzle_1(f))

# Puzzle 2
def puzzle_2(data):
    state = [data[1], data[2], "###D#C#B#A###", "###D#B#A#C###", "##" + data[3][2:] + "##"]
    state = [[i for i in j] for j in state]
    state_energy = {state_to_tuple(state): 0}
    state_stack = [state]
    while state_stack:
        state = state_stack.pop()
        new_energy, new_stack = move_2(state, state_energy[state_to_tuple(state)], state_energy)
        state_energy = new_energy
        state_stack += new_stack
    min_energy = 1e8
    final_state = [["#"] + ["."] * 11 + ["#"], [i for i in "###A#B#C#D###"],
                   [i for i in "###A#B#C#D###"], [i for i in "###A#B#C#D###"], [i for i in "###A#B#C#D###"]]
    for i in state_energy.keys():
        if all([i[j] == state_to_tuple(final_state)[j] for j in range(len(state_to_tuple(final_state)))]):
            min_energy = min(min_energy, state_energy[i])
    return min_energy



def move_2(state, current_energy, state_energy):
    new_states_stack = []
    index = {"A": 3, "B": 5, "C": 7, "D": 9}
    energy = {"A": 1, "B": 10, "C": 100, "D": 1000}

    # move the nodes in the hallway
    for idx, i in enumerate(state[0]):
        if i in index.keys():
            if state[1][index[i]] == "." and \
                    state[2][index[i]] == "." and \
                    state[3][index[i]] == "." and \
                    state[4][index[i]] == "." and \
                    all([state[0][pos] == "." for pos in range(idx + 1 if idx - index[i] < 0 else idx - 1,
                                                               index[i], 1 if idx - index[i] < 0 else -1)]):
                new_state = [s.copy() for s in state]
                new_state[0][idx] = "."
                new_state[4][index[i]] = i
                try:
                    if state_energy[state_to_tuple(new_state)] > current_energy + (4 + abs(idx - index[i])) * energy[i]:
                        state_energy[state_to_tuple(new_state)] = current_energy + (4 + abs(idx - index[i])) * energy[i]
                        new_states_stack.append(new_state)
                except:
                    state_energy[state_to_tuple(new_state)] = current_energy + (4 + abs(idx - index[i])) * energy[i]
                    new_states_stack.append(new_state)
            if state[1][index[i]] == "." and \
                    state[2][index[i]] == "." and \
                    state[3][index[i]] == "." and \
                    state[4][index[i]] == i and \
                    all([state[0][pos] == "." for pos in range(idx + 1 if idx - index[i] < 0 else idx - 1,
                                                               index[i], 1 if idx - index[i] < 0 else -1)]):
                new_state = [s.copy() for s in state]
                new_state[0][idx] = "."
                new_state[3][index[i]] = i
                try:
                    if state_energy[state_to_tuple(new_state)] > current_energy + (3 + abs(idx - index[i])) * energy[i]:
                        state_energy[state_to_tuple(new_state)] = current_energy + (3 + abs(idx - index[i])) * energy[i]
                        new_states_stack.append(new_state)
                except:
                    state_energy[state_to_tuple(new_state)] = current_energy + (3 + abs(idx - index[i])) * energy[i]
                    new_states_stack.append(new_state)
            if state[1][index[i]] == "." and \
                    state[2][index[i]] == "." and \
                    state[3][index[i]] == i and \
                    state[4][index[i]] == i and \
                    all([state[0][pos] == "." for pos in range(idx + 1 if idx - index[i] < 0 else idx - 1,
                                                               index[i], 1 if idx - index[i] < 0 else -1)]):
                new_state = [s.copy() for s in state]
                new_state[0][idx] = "."
                new_state[2][index[i]] = i
                try:
                    if state_energy[state_to_tuple(new_state)] > current_energy + (2 + abs(idx - index[i])) * energy[i]:
                        state_energy[state_to_tuple(new_state)] = current_energy + (2 + abs(idx - index[i])) * energy[i]
                        new_states_stack.append(new_state)
                except:
                    state_energy[state_to_tuple(new_state)] = current_energy + (2 + abs(idx - index[i])) * energy[i]
                    new_states_stack.append(new_state)
            if state[1][index[i]] == "." and \
                    state[2][index[i]] == i and \
                    state[3][index[i]] == i and \
                    state[4][index[i]] == i and \
                    all([state[0][pos] == "." for pos in range(idx + 1 if idx - index[i] < 0 else idx - 1,
                                                               index[i], 1 if idx - index[i] < 0 else -1)]):
                new_state = [s.copy() for s in state]
                new_state[0][idx] = "."
                new_state[1][index[i]] = i
                try:
                    if state_energy[state_to_tuple(new_state)] > current_energy + (1 + abs(idx - index[i])) * energy[i]:
                        state_energy[state_to_tuple(new_state)] = current_energy + (1 + abs(idx - index[i])) * energy[i]
                        new_states_stack.append(new_state)
                except:
                    state_energy[state_to_tuple(new_state)] = current_energy + (1 + abs(idx - index[i])) * energy[i]
                    new_states_stack.append(new_state)

    # move the nodes in the place adjacent to the hallway
    for idx, i in enumerate(state[1]):
        if i in index.keys():
            if idx != index[i] or state[2][idx] != i or state[3][idx] != i or state[4][idx] != i:
                for target_idx in [1, 2, 4, 6, 8, 10, 11]:
                    if all([state[0][pos] == "." for pos in range(idx,
                                                                  target_idx + 1 if idx - target_idx < 0 else target_idx - 1,
                                                                  1 if idx - target_idx < 0 else -1)]):
                        new_state = [s.copy() for s in state]
                        new_state[1][idx] = "."
                        new_state[0][target_idx] = i
                        try:
                            if state_energy[state_to_tuple(new_state)] > current_energy + (1 + abs(idx - target_idx)) * energy[i]:
                                state_energy[state_to_tuple(new_state)] = current_energy + (1 + abs(idx - target_idx)) * \
                                energy[i]
                                new_states_stack.append(new_state)
                        except:
                            state_energy[state_to_tuple(new_state)] = current_energy + (1 + abs(idx - target_idx)) * energy[i]
                            new_states_stack.append(new_state)

    # move the nodes in the 3rd row
    for idx, i in enumerate(state[2]):
        if i in index.keys():
            if (idx != index[i] or state[3][idx] != i or state[4][idx] != i) and state[1][idx] == ".":
                for target_idx in [1, 2, 4, 6, 8, 10, 11]:
                    if all([state[0][pos] == "." for pos in range(idx,
                                                                  target_idx + 1 if idx - target_idx < 0 else target_idx - 1,
                                                                  1 if idx - target_idx < 0 else -1)]):
                        new_state = [s.copy() for s in state]
                        new_state[2][idx] = "."
                        new_state[0][target_idx] = i
                        try:
                            if state_energy[state_to_tuple(new_state)] > current_energy + (2 + abs(idx - target_idx)) * energy[i]:
                                state_energy[state_to_tuple(new_state)] = current_energy + (2 + abs(idx - target_idx)) * energy[i]
                                new_states_stack.append(new_state)
                        except:
                            state_energy[state_to_tuple(new_state)] = current_energy + (2 + abs(idx - target_idx)) * \
                                                                      energy[i]
                            new_states_stack.append(new_state)

    # move the nodes in the 4th row
    for idx, i in enumerate(state[3]):
        if i in index.keys():
            if (idx != index[i] or state[4][idx] != i) and state[1][idx] == "." and state[2][idx] == ".":
                for target_idx in [1, 2, 4, 6, 8, 10, 11]:
                    if all([state[0][pos] == "." for pos in range(idx,
                                                                  target_idx + 1 if idx - target_idx < 0 else target_idx - 1,
                                                                  1 if idx - target_idx < 0 else -1)]):
                        new_state = [s.copy() for s in state]
                        new_state[3][idx] = "."
                        new_state[0][target_idx] = i
                        try:
                            if state_energy[state_to_tuple(new_state)] > current_energy + (3 + abs(idx - target_idx)) * energy[i]:
                                state_energy[state_to_tuple(new_state)] = current_energy + (3 + abs(idx - target_idx)) * energy[i]
                                new_states_stack.append(new_state)
                        except:
                            state_energy[state_to_tuple(new_state)] = current_energy + (3 + abs(idx - target_idx)) * \
                                                                      energy[i]
                            new_states_stack.append(new_state)

    # move the nodes in the 5th row
    for idx, i in enumerate(state[4]):
        if i in index.keys():
            if idx != index[i] and state[1][idx] == "." and state[2][idx] == "." and state[3][idx] == ".":
                for target_idx in [1, 2, 4, 6, 8, 10, 11]:
                    if all([state[0][pos] == "." for pos in range(idx,
                                                                  target_idx + 1 if idx - target_idx < 0 else target_idx - 1,
                                                                  1 if idx - target_idx < 0 else -1)]):
                        new_state = [s.copy() for s in state]
                        new_state[4][idx] = "."
                        new_state[0][target_idx] = i
                        try:
                            if state_energy[state_to_tuple(new_state)] > current_energy + (4 + abs(idx - target_idx)) * energy[i]:
                                state_energy[state_to_tuple(new_state)] = current_energy + (4 + abs(idx - target_idx)) * energy[i]
                                new_states_stack.append(new_state)
                        except:
                            state_energy[state_to_tuple(new_state)] = current_energy + (4 + abs(idx - target_idx)) * \
                                                                      energy[i]
                            new_states_stack.append(new_state)
    return state_energy, new_states_stack

assert(puzzle_2(example) == 44169)
t = time.time()
print(puzzle_2(f))
print(time.time() - t)