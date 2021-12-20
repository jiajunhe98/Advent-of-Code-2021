example="""..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###""".splitlines()

with open("day20.txt") as f:
    f = f.read().splitlines()


# Puzzle 1
def process_pixel(line_1, line_2, line_3, enhance_algorithm):
    index = line_1 + line_2 + line_3
    index = int("".join(["1" if i == "#" else "0" for i in index]), 2)
    return enhance_algorithm[index]


def process_once(input_image, enhance_algorithm, padding_pixels):
    # new image (1 pixel larger on each side)
    new_image = [["."] * (len(input_image[0]) + 2) for i in range(len(input_image)+2)]

    # pad input image (2 pixels on each side) to process it more easily
    input_image = [[padding_pixels] * 2 + i + [padding_pixels] * 2 for i in input_image]
    input_image = [[padding_pixels] * len(input_image[0]) for i in range(2)] + \
                  input_image + [[padding_pixels] * len(input_image[0]) for i in range(2)]

    new_padding_pixels = enhance_algorithm[0] if padding_pixels == "." else enhance_algorithm[-1]

    for i in range(1, len(input_image)-1):
        for j in range(1, len(input_image[0])-1):
            line_1 = input_image[i-1][j-1:j+2]
            line_2 = input_image[i+0][j-1:j+2]
            line_3 = input_image[i+1][j-1:j+2]
            new_image[i-1][j-1] = process_pixel(line_1, line_2, line_3, enhance_algorithm)
    return new_image, new_padding_pixels

def read_in(data):
    enhance_algorithm = data[0]
    image = [[j for j in line] for line in data[2:]]
    return image, enhance_algorithm

def puzzle_1(data):
    image, enhance_algorithm = read_in(data)
    image, padding_pixels = process_once(image, enhance_algorithm, ".")
    image, padding_pixels = process_once(image, enhance_algorithm, padding_pixels)
    return sum([1 if j == "#" else 0 for i in image for j in i])

assert(puzzle_1(example) == 35)
print(puzzle_1(f))

# Puzzle 2
def puzzle_2(data):
    image, enhance_algorithm = read_in(data)
    padding_pixels = "."
    for i in range(50):
        image, padding_pixels = process_once(image, enhance_algorithm, padding_pixels)
    return sum([1 if j == "#" else 0 for i in image for j in i])

assert(puzzle_2(example) == 3351)
print(puzzle_2(f))