rocks = []
with open("input.txt") as infile:
    for line in infile:
        rocks.append(line.rstrip().split(" -> "))

grid = []
for i in range(1000):
    grid.append(["."] * 1000)

lowest = 0

for rock in rocks:
    prev = None
    for vertex in rock:
        arr = vertex.split(",")  # col, row
        arr = [int(i) for i in arr]
        if prev:
            if prev[0] == arr[0]:  # vertical
                dist = prev[1] - arr[1]
                if dist > 0:  # moving down
                    for j in range(0, dist + 1):
                        print("down", arr[1] + j, prev[0], dist)
                        grid[arr[1] + j][prev[0]] = "#"
                        if arr[1] + j > lowest:
                            lowest = arr[1] + j
                else:
                    for j in range(dist, 0):  # moving up
                        print("up", arr[1] + j, prev[0], dist)
                        grid[arr[1] + j][prev[0]] = "#"
                        if arr[1] + j > lowest:
                            lowest = arr[1] + j
            elif prev[1] == arr[1]:  # horizontal
                dist = prev[0] - arr[0]
                if dist > 0:  # moving right
                    for j in range(0, dist + 1):
                        print("right", prev[1], arr[1] + j, dist)
                        grid[prev[1]][arr[0] + j] = "#"
                        if prev[1] > lowest:
                            lowest = prev[1] + j
                else:
                    for j in range(dist, 0):  # moving left
                        print("left", prev[1], arr[1] + j, dist)
                        grid[prev[1]][arr[0] + j] = "#"
                        if prev[1] > lowest:
                            lowest = prev[1] + j
        prev = arr


def print_grid(grid):
    # for row in grid[0:10]:
    #    print(" ".join(str(x) for x in row[494:504]))
    for row in grid[0:176]:
        print(" ".join(str(x) for x in row[450:550]))


# add sand units and move them
def init_sand(grid, sand):
    for i in range(len(sand)):
        row = sand[i][0]
        col = sand[i][1]
        grid[row][col] = "."
        if grid[row + 1][col] == ".":
            sand[i] = (row + 1, col)
        else:
            if grid[row + 1][col - 1] == ".":
                sand[i] = (row + 1, col - 1)
            elif grid[row + 1][col + 1] == ".":
                sand[i] = (row + 1, col + 1)
        row = sand[i][0]
        col = sand[i][1]
        grid[row][col] = "o"
    return sand


# move sand until you can't anymore
def sim_sand(grid, sand):
    movement = True
    while movement:
        sand_before = sand.copy()
        sand_after = init_sand(grid, sand)
        if sand_before == sand_after:
            movement = False

    return sand_after


def check_at_rest(grid, sand):
    for i in range(len(sand)):
        row = sand[i][0]
        col = sand[i][1]
        if (
            grid[row + 1][col] == "."
            or grid[row + 1][col - 1] == "."
            or grid[row + 1][col + 1] == "."
        ):
            return False

    return True


sand = [(0, 500)]


# for k in range(23):
#     sand = init_sand(grid, sand)
#     if sand == "stop":
#         print(k + 1)
#         break
#     sand.append((0, 500))

# sand = sim_sand(grid, sand)

# print_grid(grid)

simming = True
count = 1
while simming:
    print(count - 1)
    sand = init_sand(grid, sand)
    sand = sim_sand(grid, sand)
    sand.append((0, 500))
    count += 1
