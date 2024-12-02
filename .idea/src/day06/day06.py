import util.util


def solve_part_one(points, size):
    grids = []
    result_dict = dict()
    final_grid = generate_field(size)
    for point in points:
        grids.append(mark_reachable_area(generate_field(size), point[0], point[1]))
    for y in range(size):
        for x in range(size):
            min_grid = ""
            min_value = 100000000
            for grid in grids:
                if grid[y][x] < min_value:
                    min_value = grid[y][x]
                    min_grid = "{}".format(grids.index(grid))
                    # print(min_grid)
                elif grid[y][x] == min_value:
                    min_grid = "."

            final_grid[y][x] = min_grid
            if min_grid != ".":
                result_dict[min_grid] = 0

    for row in final_grid:
        for j in row:
            if j != ".":
                result_dict[j] += 1
    keys = list(result_dict.keys())
    for i in final_grid[0]:
        if i in keys:
            keys.remove(i)
    for i in final_grid[len(final_grid) - 1]:
        if i in keys:
            keys.remove(i)
    for row in final_grid:
        for i in final_grid[len(final_grid) - 1]:
            if row[0] in keys:
                keys.remove(row[0])
            if row[len(row) - 1] in keys:
                keys.remove(row[len(row) - 1])

    max_area = 0
    for key in keys:
        max_area = max(max_area, result_dict[key])
    return max_area

def solve_part_two(points, size, bound):
    grids = []
    result_dict = dict()
    final_grid = generate_field(size)
    for point in points:
        grids.append(mark_reachable_area(generate_field(size), point[0], point[1]))
    result = 0
    for y in range(size):
        for x in range(size):
            sum = 0
            for grid in grids:
                sum += grid[y][x]
            if sum < bound:
                result += 1

    return result




def generate_field(size):
    return [[0 for i in range(size)] for j in range(size)]

def mark_reachable_area(grid, start_x, start_y):
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = abs(start_x - j) + abs(start_y - i)
    return grid


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0
coordinates = []
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    split_line = input_line.split(", ")
    coordinates.append((int(split_line[0]), int(split_line[1])))
    count += 1

field_size = 700



print("TASK 1 - sol: {}".format(solve_part_one(coordinates, field_size)))

print("TASK 2 - sol: {}".format(solve_part_two(coordinates, field_size, 10000)))
