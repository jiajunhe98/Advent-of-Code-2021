example="""be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".split("\n")

with open("day8.txt") as f:
    f = f.read().splitlines()

# Puzzle 1
def puzzle_1(data):
    data = [i.split("|")[-1].split(" ") for i in data]
    return sum([len(i) in [2, 3, 4, 7] for j in data for i in j])
assert (puzzle_1(example) == 26)
print(puzzle_1(f))

# Puzzle 1
def puzzle_2(data):
    return sum([process_line(i) for i in data])

def process_line(line):
    patterns = line.split("|")[0].split()
    patterns = [tuple(sorted([j for j in i])) for i in patterns]
    pattern_dict = {}
    num_dict = {}
    for i in patterns:
        if len(i) == 2:
            pattern_dict[i] = 1
            num_dict[1] = i
        if len(i) == 4:
            pattern_dict[i] = 4
            num_dict[4] = i
        if len(i) == 3:
            pattern_dict[i] = 7
            num_dict[7] = i
        if len(i) == 7:
            pattern_dict[i] = 8
            num_dict[8] = i
    for i in patterns:
        if len(i) == 6:
            if all(j in i for j in num_dict[4]):
                pattern_dict[i] = 9
                num_dict[9] = i
            elif all(j in i for j in num_dict[1]):
                pattern_dict[i] = 0
                num_dict[0] = i
            else:
                pattern_dict[i] = 6
                num_dict[6] = i
    for i in patterns:
        if len(i) == 5:
            if all(j in i for j in num_dict[1]):
                pattern_dict[i] = 3
                num_dict[3] = i
            elif all(j in num_dict[9] for j in i):
                pattern_dict[i] = 5
                num_dict[5] = i
            else:
                pattern_dict[i] = 2
                num_dict[2] = i
    patterns = line.split("|")[1].split()
    patterns = [str(pattern_dict[tuple(sorted([j for j in i]))]) for i in patterns]
    return int("".join(patterns))
assert(puzzle_2(example) == 61229)
print(puzzle_2(f))