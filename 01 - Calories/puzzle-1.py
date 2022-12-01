data = []  # array that we will overwrite that stores the snacks for one elf
elf_calories = []  # stores the calories carried by each elf

with open("input.txt") as f:
    for line in f.readlines():
        # Empty string is what separates each elf
        if line.strip() == "":
            elf_calories.append(sum(data))
            data = []
        else:
            data.append(int(line.strip()))


print(max(elf_calories))  # 68775 : most calories

elf_calories.sort(reverse=True)
print(sum(elf_calories[0:3]))  # 202585 : top three elves
