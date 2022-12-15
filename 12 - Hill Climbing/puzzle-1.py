from queue import PriorityQueue

grid = []
start = ()
goal = ()
with open("input.txt") as infile:

    count = 0
    for line in infile:

        row = list(line.strip())

        if "S" in row:
            start = (count, row.index("S"))
        if "E" in row:
            goal = (count, row.index("E"))
        grid.append(row)
        count += 1


def get_valid_moves(grid, pos):
    # Returns a list of the legal moves from the current position
    # Doesn't take into account the height of moves, that is in costfxn
    moves = []

    row = pos[0]
    col = pos[1]

    moves.append((row + 1, col))
    moves.append((row, col + 1))
    moves.append((row - 1, col))
    moves.append((row, col - 1))

    final_moves = []
    for move in moves:
        if move[0] >= 0 and move[1] >= 0:
            if move[0] < len(grid) and move[1] < len(grid[0]):
                final_moves.append(move)

    return final_moves


def cost_fxn(grid, start, end):
    # Defines the cost to go from one node to another
    # Is -1 if we are heading uphill
    # Is 1 if we are heading down or same level
    # Returns none if the move is too steep

    start_score = grid[start[0]][start[1]]
    end_score = grid[end[0]][end[1]]
    if start_score == "S":
        start_score = chr(ord("a") - 1)
    if end_score == "E":
        end_score = chr(ord("z") + 1)
    if ord(end_score) - ord(start_score) == 1:
        return -1
    elif ord(end_score) - ord(start_score) <= 0:
        return 1
    return None


def path_output(visited, start, count):
    # returns a count of our path steps
    if visited[start]:
        count += 1
        return path_output(visited, visited[start], count)  # recursion
    return count  # base case


def get_path(visited, start, path):
    # returns a list of the steps of our path for visualization
    if visited[start]:
        path.append(visited[start])
        return get_path(visited, visited[start], path)  # recursion
    return path  # base case


def visualize_path(grid, visited, start):
    # Prints a map of our path
    path = get_path(visited, start, [start])

    for row in range(len(grid)):
        subset = ""
        for col in range(len(grid[0])):
            if (row, col) in path:
                subset = f"{subset}[{grid[row][col]}]"
            else:
                subset = f"{subset} {grid[row][col]} "
        print(subset)


def dijkstras(grid, start, goal):
    queue = PriorityQueue()
    queue.put((0, start, None))  # (cost, node, upstream node)

    visited = dict()
    # Storing the sequence of nodes we have visited and their parent node

    while not queue.empty():
        x = queue.get()
        # Any node that we have popped off the queue we can be confident that is the shortest path
        visited[x[1]] = x[2]

        # If we popped the target node, we are done
        if x[1] == goal:
            visualize_path(grid, visited, x[1])
            return path_output(visited, x[1], 0)

        # gets all possible moves
        moves = get_valid_moves(grid, x[1])

        for move in moves:
            if move not in visited:  # ignore nodes we have already been to
                updated = False
                cost = cost_fxn(grid, x[1], move)  # calculate cost
                if cost is not None:  # valid moves only
                    cost += x[0]  # add upstream cost
                    ## Here, I am updating the priorty queue if it is already in there else creating a new entry
                    for i in range(len(queue.queue)):
                        if queue.queue[i][1] == move:
                            updated = True
                            if cost < queue.queue[i][0]:
                                queue.queue.pop(i)
                                queue.put((cost, move, x[1]))
                            break
                    if not updated:
                        queue.put((cost, move, x[1]))


print(dijkstras(grid, start, goal))

# answer = 391
