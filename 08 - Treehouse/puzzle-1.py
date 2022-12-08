heights = []
with open("input.txt") as infile:
    for line in infile:
        row = list(line.strip())
        heights.append(list(map(int, row)))

BOARD_WIDTH = len(heights[0])
BOARD_HEIGHT = len(heights)

# Create a boolean matrix of if the trees are visible
board = [[False for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

# Also valid for top-down
def left_to_right(row, output):
    max_height = -1
    for i in range(0, BOARD_WIDTH):
        if row[i] > max_height:
            max_height = row[i]
            output[i] = True

    return output


# Also valid for bottom-up
def right_to_left(row, output):
    max_height = -1
    for i in range(BOARD_WIDTH - 1, -1, -1):
        if row[i] > max_height:
            max_height = row[i]
            output[i] = True
    return output


def get_column(matrix, i):  # returns a column of our 2-d list
    column = []
    for row in matrix:
        column.append(row[i])
    return column


def write_column(matrix, i, col):  # writes a column back to our 2-d list
    output = []
    for j in range(0, BOARD_HEIGHT):
        row = matrix[j]
        row[i] = col[j]
        output.append(row)
    return output


# note: assumes square board
for i in range(0, BOARD_HEIGHT):
    # get row
    row = heights[i]
    # Check L->R
    board[i] = left_to_right(row, board[i])
    # Check R->L
    board[i] = right_to_left(row, board[i])

    # get columns
    col = get_column(heights, i)
    board_col = get_column(board, i)

    # Check T->B
    board_col = left_to_right(col, board_col)
    # Check B->T
    board_col = right_to_left(col, board_col)

    # write back to our board matrix
    board = write_column(board, i, board_col)

count = 0
for row in board:
    # print(row)
    count += sum(row)

print(f"Part One: {count}")  # 1,672


# Counts the number of trees one location can see to the north
def count_north(matrix, x, y, count, height):
    if y - 1 >= 0:
        count += 1
        if matrix[y - 1][x] >= height:
            return count
        else:
            return count_north(matrix, x, y - 1, count, height)
    else:
        return count


# Counts the number of trees one location can see to the south
def count_south(matrix, x, y, count, height):
    if y + 1 <= BOARD_HEIGHT - 1:
        count += 1
        if matrix[y + 1][x] >= height:
            return count
        else:
            return count_south(matrix, x, y + 1, count, height)
    else:
        return count


# Counts the number of trees one location can see to the west
def count_west(matrix, x, y, count, height):
    if x - 1 >= 0:
        count += 1
        if matrix[y][x - 1] >= height:
            return count
        else:
            return count_west(matrix, x - 1, y, count, height)
    else:
        return count


# Counts the number of trees one location can see to the east
def count_east(matrix, x, y, count, height):
    if x + 1 <= BOARD_WIDTH - 1:
        count += 1
        if matrix[y][x + 1] >= height:
            return count
        else:
            return count_east(matrix, x + 1, y, count, height)
    else:
        return count


max_score = -1
scores = [[-1 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
for y in range(0, BOARD_HEIGHT):
    for x in range(0, BOARD_WIDTH):
        north = count_north(heights, x, y, 0, heights[y][x])
        south = count_south(heights, x, y, 0, heights[y][x])
        east = count_east(heights, x, y, 0, heights[y][x])
        west = count_west(heights, x, y, 0, heights[y][x])
        scores[y][x] = north * south * east * west

        if scores[y][x] > max_score:
            max_score = scores[y][x]

print(f"Part Two: {max_score}")  # 327,180
