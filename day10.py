example="""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split("\n")

with open("day10.txt") as f:
    f = f.read().splitlines()


# Puzzle 1
def puzzle_1(data):
    error_score = 0
    scores = {']': 57, ')': 3, '}': 1197, '>': 25137}
    for line in data:
        stack = []
        corresponds = {']': '[', ')': '(', '}': '{', '>': '<'}
        for i in line:
            if i not in corresponds.keys():
                stack.append(i)
            else:
                last_one = stack.pop(-1)
                if last_one != corresponds[i]:
                    error_score += scores[i]
                    break
    return error_score

assert (puzzle_1(example) == 26397)
print(puzzle_1(f))


# Puzzle 2
def puzzle_2(data):
    total_score = []
    scores = {'[': 2, '(': 1, '{': 3, '<': 4}
    for line in data:
        stack = []
        corresponds = {']': '[', ')': '(', '}': '{', '>': '<'}

        corrupted = 0
        for i in line:
            if i not in corresponds.keys():
                stack.append(i)
            else:
                last_one = stack.pop(-1)
                if last_one != corresponds[i]:
                    corrupted = 1
                    break
        if corrupted: continue
        score = 0
        while len(stack) != 0:
            score = score * 5 + scores[stack.pop(-1)]
        total_score.append(score)
        total_score.sort()
    return total_score[len(total_score)//2]


assert (puzzle_2(example) == 288957)
print(puzzle_2(f))


