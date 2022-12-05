stacks = dict()
instructions = []
with open("input.txt") as infile:
    count = 0
    for line in infile:
        if count < 8:
            # Get inital positions of crates
            for i in range(1, len(line), 4):
                if line[i].strip():
                    key = int(i / 4) + 1
                    if key in stacks:
                        stacks[key].insert(0, line[i])
                    else:
                        stacks[key] = [line[i]]
        elif count > 9:
            # Get the moving instructions
            # (quantity, origin, destination)
            instructions.append([int(line[5:7]), int(line[12:14]), int(line[17:19])])
        count += 1


def move_crate(crates, quantity, origin, destination):
    for i in range(0, quantity):
        crates[destination].append(crates[origin].pop())
    return crates


for item in instructions:
    stacks = move_crate(stacks, item[0], item[1], item[2])

ans = str()
for i in range(1, 10):  # Answers output
    ans = f"{ans}{stacks[i].pop()}"

print(ans)  #  Part 1: TQRFCBSJJ
