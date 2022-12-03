groups = []  # array of arrays that will store our teams
team = []
shared_items = []

count = 0
with open("input.txt") as f:
    # making 2D array
    for line in f.readlines():
        team.append(line)
        count += 1
        if count == 3:
            # Once our team is full restart and add to our group array
            count = 0
            groups.append(team)
            team = []

for squad in groups:
    for char in squad[0]:
        if char in squad[1] and char in squad[2]:
            if char.isupper():
                # Converting to the priorty based on the ASCII value
                shared_items.append(ord(char) - 38)
            else:
                shared_items.append(ord(char) - 96)
            break

# Answer is 2,780
print(sum(shared_items))
