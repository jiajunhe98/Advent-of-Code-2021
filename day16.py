example1="""8A004A801A8002F478"""
example2="""C0015000016115A2E0802F182340"""
example3="""620080001611562C8802118E34"""
example4="""A0016C880162017C3686B18A3D4780"""
example5="""C200B40A82"""
example6="""04005AC33890"""
example7="""880086C3E88112"""
example8="""CE00C43D881120"""
example9="""D8005AC2A8F0"""
example10="""F600BC2D8F"""
example11="""9C005AC2F8F0"""
example12="""9C0141080250320F1802104A08"""

with open("day16.txt") as f:
    f = f.read().splitlines()[0]


# Puzzle 1

_16_to_2 = lambda x: "".join([("0000"+bin(int(i, 16))[2:])[-4:] for i in x])


def process_list(nested_list):
    while nested_list:
        nested_list[-1] -= 1
        if nested_list[-1] == 0:
            nested_list.pop(-1)
        else:
            break
    return nested_list

def parsing(data, nested_list=[1]):
    current_position = 0
    while 1:
        if nested_list == [] or current_position >= len(data) - 6:
            break
        version = int(data[current_position:current_position + 3], 2)
        yield version
        type = int(data[current_position + 3:current_position + 6], 2)
        if type == 4:
            curr_pos = current_position + 6
            while 1:
                if data[curr_pos] == "0":
                    break
                curr_pos += 5
            curr_pos = min(curr_pos + 5, len(data))
            current_position = curr_pos
            nested_list = process_list(nested_list)
        else:
            current_position = current_position + 6
            if data[current_position] == "0":
                length = int(data[current_position+1: current_position+16], 2)
                yield from parsing(data[current_position+16: current_position+16+length], nested_list=[1e8])
                current_position = current_position + 16 + length
                nested_list = process_list(nested_list)
            elif data[current_position] == "1":
                num = int(data[current_position + 1: current_position + 12], 2)
                nested_list.append(num)
                current_position = current_position + 12


def puzzle_1(data):
    data = _16_to_2(data)
    return sum(list(parsing(data, [1])))

assert (puzzle_1(example1) == 16)
assert (puzzle_1(example2) == 23)
assert (puzzle_1(example3) == 12)
assert (puzzle_1(example4) == 31)
print(puzzle_1(f))

# Puzzle 2
def product_list(x):
    result = 1
    for i in x:
        result *= i
    return result
types = {
    0: lambda x: sum(x),
    1: product_list,
    2: lambda x: min(x),
    3: lambda x: max(x),
    5: lambda x: int(x[0] < x[1]),
    6: lambda x: int(x[0] > x[1]),
    7: lambda x: int(x[0] == x[1])
}

def parsing_2(data, operations, nested_list=[1]):
    current_position = 0
    while 1:
        if nested_list == []:
            break
        if current_position >= len(data) - 6:
            operations.append(")")
            break
        version = int(data[current_position:current_position + 3], 2)
        type = int(data[current_position + 3:current_position + 6], 2)
        if type == 4:
            curr_pos = current_position + 6
            value = ""
            while 1:
                value += data[curr_pos + 1:curr_pos + 5]
                if data[curr_pos] == "0":
                    break
                curr_pos += 5
            operations.append(int(value, 2))
            curr_pos = min(curr_pos + 5, len(data))
            current_position = curr_pos
            nested_list = process_list_2(nested_list, operations)
        else:
            operations.append(types[type])
            operations.append("(")
            current_position = current_position + 6
            if data[current_position] == "0":
                length = int(data[current_position+1: current_position+16], 2)
                parsing_2(data[current_position+16: current_position+16+length], operations, nested_list=[1e8])
                current_position = current_position + 16 + length
                nested_list = process_list_2(nested_list, operations)
            elif data[current_position] == "1":
                num = int(data[current_position + 1: current_position + 12], 2)
                nested_list.append(num)
                current_position = current_position + 12

def process_list_2(nested_list, oper):
    while nested_list:
        nested_list[-1] -= 1
        if nested_list[-1] == 0:
            nested_list.pop(-1)
            oper.append(")")
        else:
            break
    return nested_list

def puzzle_2(data):
    data = _16_to_2(data)
    global OPERATIONS
    OPERATIONS = []
    parsing_2(data, operations=OPERATIONS, nested_list=[1])
    stack = []
    while OPERATIONS:
        current = OPERATIONS.pop(0)
        if current == ")" and len(stack) > 1:
            numbers = []
            while stack:
                curr = stack.pop(-1)
                if curr  == "(":
                    break
                numbers.append(curr)
            operation = stack.pop(-1)
            stack.append(operation(numbers))
        else:
            stack.append(current)

    return stack[0]

assert(puzzle_2(example5) == 3)
assert(puzzle_2(example6) == 54)


print(puzzle_2(f))