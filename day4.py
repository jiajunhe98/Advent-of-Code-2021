example="""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split("\n")

with open("day4.txt") as f:
    f = f.read().splitlines()

# Puzzle 1
class Board:
    def __init__(self):
        self.board = []
        self.row_count = [0] * 5
        self.col_count = [0] * 5

def puzzle_1(data):
    random_numbers = data[0].split(",")
    board_list = []
    for i in range(1, len(data)):
        if data[i] == "":
            board_list.append(Board())
        else:
            board_list[-1].board.append(data[i].split())
    for number in random_numbers:
        for j in board_list:
            for m in range(5):
                for n in range(5):
                    if j.board[m][n] == number:
                        j.board[m][n] = 0
                        j.row_count[m] += 1
                        j.col_count[n] += 1
                        if j.row_count[m] == 5 or j.col_count[n] == 5:
                            return sum([int(j.board[a][b]) for a in range(5) for b in range(5)]) * int(number)
assert(puzzle_1(example) == 4512)
print(puzzle_1(f))


# Puzzle 2

class Board2:
    def __init__(self):
        self.board = []
        self.row_count = [5] * 5
        self.col_count = [5] * 5
        self.sum = 0


def puzzle_2(data):
    random_numbers = data[0].split(",")
    board_list = []
    for i in range(1, len(data)):
        if data[i] == "":
            board_list.append(Board2())
        else:
            board_list[-1].board.append(data[i].split())
    for number in random_numbers[::-1]:
        for j in board_list:
            for m in range(5):
                for n in range(5):
                    if j.board[m][n] == number:
                        j.sum += int(j.board[m][n])
                        j.row_count[m] -= 1
                        j.col_count[n] -= 1
                        if (5 not in j.row_count) and (5 not in j.col_count):
                            return (j.sum - int(j.board[m][n])) * int(number)

assert(puzzle_2(example) == 1924)
print(puzzle_2(f))




