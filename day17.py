example="""target area: x=20..30, y=-10..-5"""
with open("day17.txt") as f:
    f = f.read().splitlines()[0]


import re
import math

# Puzzle 1
def puzzle_1(data):
    y_low = int(re.findall(r"x=(\-?[0-9]+)\.\.(\-?[0-9]+).+y=(\-?[0-9]+)\.\.(\-?[0-9]+)", data)[0][-2])
    y0_max = - y_low - 1
    return y0_max * (y0_max + 1) // 2
assert (puzzle_1(example) == 45)
print(puzzle_1(f))

# Puzzle 2
def puzzle_2(data):
    x_left, x_right, y_low, y_up = re.findall(r"x=(\-?[0-9]+)\.\.(\-?[0-9]+).+y=(\-?[0-9]+)\.\.(\-?[0-9]+)", data)[0]
    y0_max = - int(y_low) - 1
    y0_min = int(y_low)
    x0_max = int(x_right)
    x0_min = math.ceil(math.sqrt(8 * int(x_left) + 1) / 2 - 0.5)
    possible_starting = set()
    for x in range(x0_min, x0_max + 1):
        for y in range(y0_min, y0_max + 1):
            curr_x = 0
            curr_y = 0
            x_speed = x
            y_speed = y
            while curr_x <= x0_max and curr_y >= y0_min:
                curr_x += x_speed
                curr_y += y_speed
                x_speed -= 1 if x_speed > 0 else 0
                y_speed -= 1
                if curr_x >= int(x_left) and curr_x <= int(x_right) and curr_y >= int(y_low) and curr_y <= int(y_up):
                    possible_starting.add((x, y))
                    continue
    return len(possible_starting)
assert (puzzle_2(example) == 112)
print(puzzle_2(f))


