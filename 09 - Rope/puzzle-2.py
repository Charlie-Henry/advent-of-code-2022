# Reading in data
moves = []
with open("input.txt") as infile:
    for line in infile:
        moves.append(line.strip().split(" "))

# moves it right one unit
def move_right(position):
    position[1] = position[1] + 1
    return position


# moves it left one unit
def move_left(position):
    position[1] = position[1] - 1
    return position


# moves it up one unit
def move_up(position):
    position[0] = position[0] - 1
    return position


# moves it down one unit
def move_down(position):
    position[0] = position[0] + 1
    return position


# updates the tail position based on the head's position
def update_tail(head_position, tail_position):
    if head_position == tail_position:
        print("do nothing")
        return tail_position
    # same row
    if head_position[0] == tail_position[0]:
        if abs(head_position[1] - tail_position[1]) > 1:
            # head is to the right
            if head_position[1] - tail_position[1] > 0:
                print("move right")
                return move_right(tail_position)
            # head is to the left
            else:
                print("move left")
                return move_left(tail_position)
        else:
            print("do nothing")
            return tail_position
    # same column
    if head_position[1] == tail_position[1]:
        if abs(head_position[0] - tail_position[0]) > 1:
            # head is below tail
            if head_position[0] - tail_position[0] > 0:
                print("move down")
                return move_down(tail_position)
            # head is above tail
            else:
                print("move up")
                return move_up(tail_position)
        else:
            print("do nothing")
            return tail_position

    # now, the head must be diagonal to our tail
    # if directly diagonal do nothing
    if (
        abs(head_position[0] - tail_position[0]) == 1
        and abs(head_position[1] - tail_position[1]) == 1
    ):
        print("do nothing")
        return tail_position
    else:  # move diagonally
        # if farther along to the right
        if head_position[1] - tail_position[1] > 0:
            if head_position[0] - tail_position[0] > 0:
                # move down to the right
                print("move down and to the right")
                tail_position = move_down(tail_position)
                return move_right(tail_position)
            else:
                # move up to the right
                print("move up and to the right")
                tail_position = move_up(tail_position)
                return move_right(tail_position)
        # if farther along to the left
        if head_position[1] - tail_position[1] < 0:
            if head_position[0] - tail_position[0] > 0:
                # move down to the left
                print("move down and to the left")
                tail_position = move_down(tail_position)
                return move_left(tail_position)
            else:
                # move up to the left
                print("move up and to the left")
                tail_position = move_up(tail_position)
                return move_left(tail_position)
        # if farther along up
        if head_position[0] - tail_position[0] < 0:
            if head_position[1] - tail_position[1] > 0:
                # move up to the right
                print("move up and to the right")
                tail_position = move_up(tail_position)
                return move_right(tail_position)
            else:
                print("move up and to the left")
                # move up to the left
                tail_position = move_up(tail_position)
                return move_left(tail_position)
        # if farther along down
        if head_position[0] - tail_position[0] > 0:
            if head_position[1] - tail_position[1] > 0:
                # move down to the right
                print("move down and to the right")
                tail_position = move_down(tail_position)
                return move_right(tail_position)
            else:
                # move down to the left
                print("move down and to the left")
                tail_position = move_down(tail_position)
                return move_left(tail_position)
    # we should never get here
    assert -1 == 1


# start at 0,0
# [row = x, col = y]
positions = [
    [0, 0],  # head
    [0, 0],  # 1
    [0, 0],  # 2
    [0, 0],  # 3
    [0, 0],  # 4
    [0, 0],  # 5
    [0, 0],  # 6
    [0, 0],  # 7
    [0, 0],  # 8
    [0, 0],  # 9
]
tail_locs = dict()
tail_locs[0, 0] = 1

for instruction in moves:
    direction = instruction[0]
    quantity = int(instruction[1])
    print(f"{direction}:{quantity}")

    for i in range(quantity):
        # print(f"{head_position},{tail_position}")
        if direction == "R":
            # print("move right")
            positions[0] = move_right(positions[0])
        if direction == "L":
            # print("move left")
            positions[0] = move_left(positions[0])
        if direction == "U":
            # print("move up")
            positions[0] = move_up(positions[0])
        if direction == "D":
            # print("move down")
            positions[0] = move_down(positions[0])

        for i in range(0, 9):
            positions[i + 1] = update_tail(positions[i], positions[i + 1])

        if tuple(positions[9]) not in tail_locs:
            tail_locs[tuple(positions[9])] = 1
        else:
            tail_locs[tuple(positions[9])] += 1

print(len(tail_locs))
