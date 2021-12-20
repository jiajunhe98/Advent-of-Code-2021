example="""--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14""".splitlines()

with open("day19.txt") as f:
    f = f.read().splitlines()


def process_data(data):
    scanners = []
    for i in data:
        if i[:3] == "---":
            scanners.append([])
        elif i != "":
            scanners[-1].append([int(x) for x in i.split(",")])
    return scanners


def generate_descriptors(data):
    descriptors = [[] for i in range(len(data))]

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            distance = sum([(data[i][x] - data[j][x]) ** 2 for x in range(3)])
            descriptors[i].append(distance)
            descriptors[j].append(distance)
    for i in range(len(descriptors)):
        descriptors[i] = sorted(descriptors[i])[:8]
    return descriptors

def get_paths(data): # get overlapping pairs
    paths = {i:[] for i in range(len(data))}  # store overlapping pairs
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            overlap_num = 0
            d1 = generate_descriptors(data[i])
            d2 = generate_descriptors(data[j])
            for a in d1:
                for b in d2:
                    if sum([a[x] in b for x in range(8)]) > 1:
                        overlap_num += 1
            if overlap_num >= 12:
                paths[i].append(j)
                paths[j].append(i)
    return paths

def solve_relative_pos(data_1, data_2):
    d1 = generate_descriptors(data_1)
    d2 = generate_descriptors(data_2)

    signs = [(i, j, k) for i in [1, -1] for j in [1, -1] for k in [1, -1]]
    permutations = list(filter(None, [(i, j, k) if i != j and j != k else None for i in range(3) for j in range(3) for k in range(3)]))

    corresponding = []
    for i in range(len(d1)):
        for j in range(len(d2)):
            if sum([d1[i][x] in d2[j] for x in range(8)]) > 1:
                corresponding.append((i, j))
    true_sign, true_permutation, true_relative_coor = None, None, None
    for sign in signs:
        for permutation in permutations:
            true_or_not = 1
            relative_coor = None
            for pair in corresponding:
                relative_coor = [data_2[pair[1]][permutation[i]]*sign[i] - data_1[pair[0]][i] for i in range(3)] if relative_coor is None else relative_coor
                if relative_coor and any([data_2[pair[1]][permutation[i]]*sign[i] - data_1[pair[0]][i] != relative_coor[i] for i in range(3)]):
                    true_or_not = 0
                    break
            if true_or_not:
                true_sign = sign
                true_permutation = permutation
                true_relative_coor = relative_coor
                break
        if true_sign:
            break
    new_data_2 = []
    for i in data_2:
        new_data_2.append([i[true_permutation[j]] * true_sign[j] - true_relative_coor[j] for j in range(3)])
    return true_relative_coor, new_data_2

def puzzle_1(data):
    data = process_data(data)
    paths = get_paths(data)
    passed_scanner = set()
    next_scanner = [0]

    # BFS
    while next_scanner:
        current_scanner_1 = next_scanner.pop()
        for current_scanner_2 in paths[current_scanner_1]:
            passed_scanner.add(current_scanner_1)
            if current_scanner_2 not in passed_scanner:
                _, new_data = solve_relative_pos(data[current_scanner_1], data[current_scanner_2])
                data[current_scanner_2] = new_data
                next_scanner.append(current_scanner_2)
    assert (len(passed_scanner) == len(data))

    beacons = {tuple(i) for j in data for i in j}
    return len(beacons)


assert(puzzle_1(example) == 79)
print(puzzle_1(f))

# Puzzle 2
def puzzle_2(data):
    data = process_data(data)
    paths = get_paths(data)
    passed_scanner = set()
    next_scanner = [0]
    scanners_coors = {0: [0, 0, 0]}

    # BFS
    while next_scanner:
        current_scanner_1 = next_scanner.pop()
        for current_scanner_2 in paths[current_scanner_1]:
            passed_scanner.add(current_scanner_1)
            if current_scanner_2 not in passed_scanner:
                scanner_coor, new_data = solve_relative_pos(data[current_scanner_1], data[current_scanner_2])
                data[current_scanner_2] = new_data
                next_scanner.append(current_scanner_2)
                scanners_coors[current_scanner_2] = scanner_coor
    assert (len(passed_scanner) == len(data))

    distance = 0
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            distance = max(distance, sum([abs(scanners_coors[i][k] - scanners_coors[j][k]) for k in range(3)]))


    return distance


assert (puzzle_2(example) == 3621)
print(puzzle_2(f))


