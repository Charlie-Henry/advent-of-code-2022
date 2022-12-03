shared_items = []

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        first_compartment = line[0 : int(len(line) / 2)]
        second_compartment = line[int(len(line) / 2) : len(line)]

        for item in first_compartment:
            if item in second_compartment:
                if item.isupper():
                    # Converting to the priorty based on the ASCII value
                    shared_items.append(ord(item) - 38)
                else:
                    shared_items.append(ord(item) - 96)
                break

# Answer 7,568
print(sum(shared_items))
