example1="""[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]""".splitlines()

example2="""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".splitlines()
with open("day18.txt") as f:
    f = f.read().splitlines()

# Puzzle 1
def add_all(data):
    list_data = []
    for i in data:
        l = list(filter(lambda x: x != ",", [j for j in i]))
        for j in range(len(l)):
            if l[j] not in ["[", "]"]:
                l[j] = int(l[j])
        list_data.append(l)
    result_list = list_data[0]
    for i in range(1, len(list_data)):
        result_list = reduce(add(result_list, list_data[i]))
    return result_list

def add(list_1, list_2):
    list_add = ["["] + list_1 + list_2 + ["]"]
    return list_add

def reduce(list):
    while 1:
        continue_or_not = 0
        nest_count = 0
        new_list = []
        for idx, i in enumerate(list):
            new_list.append(i)
            if i == "[":
                nest_count += 1
            if i == "]":
                if nest_count > 4:
                    explodes = list[idx-2], list[idx-1]
                    new_list = new_list[:-4]
                    for exp_id in range(len(new_list)-1, -1, -1):
                        if new_list[exp_id] not in ["[", "]"]:
                            new_list[exp_id] += explodes[0]
                            break
                    new_list.append(0)
                    for exp_id in range(idx+1, len(list)):
                        if list[exp_id] not in ["[", "]"]:
                            list[exp_id] += explodes[1]
                            break
                    new_list += list[idx+1:]
                    list = new_list
                    continue_or_not = 1
                    break
                nest_count -= 1
        if continue_or_not:
            continue
        for idx, i in enumerate(list):
            if i not in ["[", "]"] and i >= 10:
                list[idx] = "]"
                list.insert(idx, i - i // 2)
                list.insert(idx, i // 2)
                list.insert(idx, "[")
                continue_or_not = 1
                break
        if continue_or_not == 0:
            break
    return list

def get_magnitude(final_list):
    stack = []
    for idx, i in enumerate(final_list):
        stack.append(i)
        if i == "]":
            stack.pop(-1)
            magnitude = 2 * stack.pop(-1) + 3 * stack.pop(-1)
            stack.pop(-1)
            stack.append(magnitude)
    return stack[0]

def puzzle_1(data):
    final_list = add_all(data)
    return get_magnitude(final_list)

assert(puzzle_1(example1) == 3488)
print(puzzle_1(f))

# Puzzle 2

def puzzle_2(data):
    magnitude = 0
    list_data = []
    for i in data:
        l = list(filter(lambda x: x != ",", [j for j in i]))
        for j in range(len(l)):
            if l[j] not in ["[", "]"]:
                l[j] = int(l[j])
        list_data.append(l)

    for idx_i, i in enumerate(list_data):
        for idx_j, j in enumerate(list_data):
            if idx_i != idx_j:
                result_list = reduce(add(i, j))
                magnitude = max(magnitude, get_magnitude(result_list))
    return magnitude

assert(puzzle_2(example2)==3993)
print(puzzle_2(f))