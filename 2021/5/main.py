import os
import time

def part_one(filename: str) -> int:
    coords = []
    with open(filename, "r") as input:
        for row in input:
            row = row.strip()
            row_coords = [[int(y) for y in x.split(",")] for x in row.split(" -> ")]
            if row_coords[0][0] == row_coords[1][0] or row_coords[0][1] == row_coords[1][1]:
                coords.append(row_coords)

    lines = []
    for coord in coords:
        if coord[0][0] == coord[1][0]:
            if coord[0][1] < coord[1][1]:
                line_length = range(coord[0][1], coord[1][1] + 1)
                line_coords = [[coord[0][0], y] for y in line_length]
            else:
                line_length = range(coord[1][1], coord[0][1] + 1)
                line_coords = [[coord[1][0], y] for y in line_length]
        else:
            if coord[0][0] < coord[1][0]:
                line_length = range(coord[0][0], coord[1][0] + 1)
                line_coords = [[x, coord[0][1]] for x in line_length]
            else:
                line_length = range(coord[1][0], coord[0][0] + 1)
                line_coords = [[x, coord[1][1]] for x in line_length]
        lines.append(line_coords)

    flat_list = []
    for line in lines:
        flat_list.extend(line)
    dupes = [x for x in flat_list if flat_list.count(x) > 1]
    unique_dupes = []
    [unique_dupes.append(x) for x in dupes if x not in unique_dupes]

    return len(unique_dupes)


def part_two(filename: str) -> int:
    coords = []
    with open(filename, "r") as input:
        for row in input:
            row = row.strip()
            row_coords = [[int(y) for y in x.split(",")] for x in row.split(" -> ")]
            if row_coords[0][0] == row_coords[1][0] or row_coords[0][1] == row_coords[1][1]:
                coords.append(row_coords)
            elif abs((row_coords[1][1] - row_coords[0][1]) / (row_coords[1][0] - row_coords[0][0])) == 1:
                coords.append(row_coords)

    lines = []
    for coord in coords:
        # x is same, vertical
        if coord[0][0] == coord[1][0]:
            if coord[0][1] < coord[1][1]:
                line_length = range(coord[0][1], coord[1][1] + 1)
                line_coords = [[coord[0][0], y] for y in line_length]
            else:
                line_length = range(coord[1][1], coord[0][1] + 1)
                line_coords = [[coord[1][0], y] for y in line_length]
        # y is same, horizontal
        elif coord[0][1] == coord[1][1]:
            if coord[0][0] < coord[1][0]:
                line_length = range(coord[0][0], coord[1][0] + 1)
                line_coords = [[x, coord[0][1]] for x in line_length]
            else:
                line_length = range(coord[1][0], coord[0][0] + 1)
                line_coords = [[x, coord[1][1]] for x in line_length]
        # diagonal
        else:
            slope = (coord[1][1] - coord[0][1]) / (coord[1][0] - coord[0][0])
            if slope == -1:
                if coord[0][1] < coord[1][1]:
                    # 8,0 -> 0,8
                    line_length = range(0, coord[1][1] - coord[0][1] + 1)
                    line_coords = [[coord[0][0] - y, coord[0][1] + y] for y in line_length]
                else:
                    # 5,5 -> 8,2
                    line_length = range(0, coord[0][1] - coord[1][1] + 1)
                    line_coords = [[coord[0][0] + y, coord[0][1] - y] for y in line_length]
            else:
                if coord[0][1] < coord[1][1]:
                    # 0,0 -> 8,8
                    line_length = range(0, coord[1][1] - coord[0][1] + 1)
                    line_coords = [[coord[0][0] + y, coord[0][1] + y] for y in line_length]
                else:
                    # 6,4 -> 2,0
                    line_length = range(0, coord[0][1] - coord[1][1] + 1)
                    line_coords = [[coord[0][0] - y, coord[0][1] - y] for y in line_length]
        lines.append(line_coords)

    flat_list = []
    for line in lines:
        flat_list.extend(line)
    dupes = [x for x in flat_list if flat_list.count(x) > 1]
    unique_dupes = []
    [unique_dupes.append(x) for x in dupes if x not in unique_dupes]

    return len(unique_dupes)


if __name__ == "__main__":
    day = __file__.split('/')[-2]
    year = __file__.split('/')[-3]
    print(f"day: {day} year: {year}")
    input_path = "input.txt"
    test_input = "input-test.txt"
    if not os.path.exists(input_path):
        os.system(f"nog -y {year} -d {day} > {input_path}")
    if not os.path.exists("puzzle.txt"):
        os.system(f"nog -y {year} -d {day} -p > puzzle.txt")
    if os.path.exists(test_input):
        print("---Part One---")
        test_one = part_one(test_input)
        print(f"test: {test_one}")
        assert test_one == 5

        start = time.time()
        print(f"start part one: {start}")
        real_one = part_one(input_path)
        end = time.time()
        print(f"real: {real_one}")
        print("time in seconds:")
        print(end - start)


        print("---Part Two---")
        test_two = part_two(test_input)
        print(f"test: {test_two}")
        assert test_two == 12

        start = time.time()
        print(f"start part two: {start}")
        real_two = part_two(input_path)
        end = time.time()
        print(f"real: {real_two}")
        print("time in seconds:")
        print(end - start)
