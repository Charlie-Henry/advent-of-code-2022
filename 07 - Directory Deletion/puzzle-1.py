import copy


class directory:
    def __init__(self, dir_name, parent_dir):
        self.name = dir_name
        self.parent = parent_dir  # directory object of the parent
        self.children = []  # list of directory objects of children
        self.items = []  # list of item sizes

    def add_child(self, child):
        self.children.append(child)

    def add_item(self, size):
        self.items.append(size)

    def sum_size(self):
        return sum(self.items)

    def __str__(self):  # was for debugging
        return f"{self.name}:{self.sum_size()}"


pwd = None  # Previous working directory
cwd = None  # Current working directory
with open("input.txt") as infile:
    count = 0
    for line in infile:
        # print(line)
        # print(cwd)
        if count == 0:  # Only for starting the root of system
            cwd = directory("/", None)
            root = cwd
            count += 1
            continue
        if line.strip() == "$ ls":  # we can ignore these
            continue
        # if we're changing directories
        if line[0:4] == "$ cd":
            # if we're not going back
            if line.strip() != "$ cd ..":
                pwd = copy.copy(cwd)
                for child in cwd.children:
                    if child.name == line.strip()[5:]:
                        cwd = copy.copy(child)
                continue
            else:  # We're moving back up
                pwd = cwd
                cwd = cwd.parent
                continue
        if line.strip()[0:3] == "dir":
            # We found a child node of our cwd
            cwd.add_child(directory(line.strip()[4:], cwd))
        else:
            # Found a file
            file_size = int(line.strip()[0 : line.strip().find(" ")])
            cwd.add_item(file_size)

output = 0
queue = [root]
dir_sizes = dict()
while queue:  # outer queue that will iterate through all nodes
    selected = queue.pop()
    sub_queue = [selected]
    node_sum = 0

    while sub_queue:  # inner queue that iterates through all children
        cur_node = sub_queue.pop()
        node_sum += cur_node.sum_size()
        if cur_node.children:
            for child in cur_node.children:
                sub_queue.append(child)

    dir_sizes[selected.name] = node_sum

    if node_sum <= 100000:  # answer part 1 calculation
        output += node_sum

    for child in selected.children:
        queue.append(child)

# answer to part one
print(output)

space_needed = -1 * (70000000 - dir_sizes["/"] - 30000000)

min_size = dir_sizes["/"]
min_key = "/"
for key in dir_sizes:
    if dir_sizes[key] >= space_needed and dir_sizes[key] < min_size:
        min_size = dir_sizes[key]
        min_key = key

# Answer to part two
print(min_size)
