example="""Player 1 starting position: 4
Player 2 starting position: 8""".splitlines()

with open("day21.txt") as f:
    f = f.read().splitlines()

# Puzzle 1
import re
def processing_data(data):
    return [int(re.findall(r"starting position: ([0-9]+)", i)[0]) for i in data]


def puzzle_1(data):
    deterministic_dice = lambda x: x + 1 if x < 100 else 1
    data = processing_data(data)
    dice = 1
    dice_times = 0
    score = [0, 0]
    while 1:
        data_add = 0
        for i in range(3):
            data_add += dice
            dice = deterministic_dice(dice)
            dice_times += 1
        data[0] += data_add
        data[0] = data[0] % 10 if data[0] % 10 != 0 else 10
        score[0] += data[0]
        if score[0] >= 1000:
            return score[1] * dice_times

        data_add = 0
        for i in range(3):
            data_add += dice
            dice = deterministic_dice(dice)
            dice_times += 1
        data[1] += data_add
        data[1] = data[1] % 10 if data[1] % 10 != 0 else 10
        score[1] += data[1]
        if score[1] >= 1000:
            return score[0] * dice_times


assert puzzle_1(example) == 739785
print(puzzle_1(f))



# Puzzle 2

'''
dice - num - value
1 1 1 - 1 - 3
2 2 2 - 1 - 6 
3 3 3 - 1 - 9

1 2 2 - 3 - 5
1 3 3 - 3 - 7
2 3 3 - 3 - 8
2 1 1 - 3 - 4
3 2 2 - 3 - 7
3 1 1 - 3 - 5

1 2 3 - 6 - 6

In total:
value - num 
3 - 1
4 - 3
5 - 6
6 - 7
7 - 6
8 - 3
9 - 1

'''
value_num_dict = {3: 1,
                  4: 3,
                  5: 6,
                  6: 7,
                  7: 6,
                  8: 3,
                  9: 1} # for each step

def all_steps(starting_point):
    # Given the starting point
    # return all results
    position = [starting_point]
    scores = [0]
    num = [1]
    step_num_dict = {} # {step: number} store how many universes in this step where it win
    step_num_dict_not_win = {}  # {step: number} store how many universes in this step where it does not win yet

    step = 0
    while scores:
        step += 1
        new_scores = []
        new_position = []
        new_num = []
        for idx, i in enumerate(scores):
            for j in value_num_dict.keys():
                new_p = position[idx] + j
                new_p = new_p % 10 if new_p % 10 != 0 else 10
                new_n = value_num_dict[j] * num[idx]
                new_s = i + new_p
                if new_s < 21:
                    new_scores.append(new_s)
                    new_position.append(new_p)
                    new_num.append(new_n)
                    try:
                        step_num_dict_not_win[step] += new_n
                    except:
                        step_num_dict_not_win[step] = new_n
                else:
                    try:
                        step_num_dict[step] += new_n
                    except:
                        step_num_dict[step] = new_n
        scores = new_scores
        position = new_position
        num = new_num

    return step_num_dict, step_num_dict_not_win


def puzzle_2(data):
    data = processing_data(data)
    step_num_dict_1, step_num_dict_not_win_1 = all_steps(data[0])
    step_num_dict_2, step_num_dict_not_win_2 = all_steps(data[1])
    winner_1 = 0
    winner_2 = 0
    for i in step_num_dict_1.keys():
        if i-1 in  step_num_dict_not_win_2.keys():
            winner_1 += step_num_dict_1[i] * step_num_dict_not_win_2[i-1]
    for i in step_num_dict_2.keys():
        if i in step_num_dict_not_win_1.keys():
            winner_2 += step_num_dict_2[i] * step_num_dict_not_win_1[i]
    return max(winner_1, winner_2)

assert(puzzle_2(example) == 444356092776315)


import time
t = time.time()
print(puzzle_2(f))
print(time.time()-t)
