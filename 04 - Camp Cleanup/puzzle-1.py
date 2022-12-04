# Loading in data

# List of assignments, where each row is a list where the first
# entry is a list of campsites for elf 1 and second entry is campsites
# for elf 2
list_of_pairs = []
with open("input.txt") as infile:
    for line in infile:
        if line.strip():
            res = line.strip().split(",")  # Get row of data

            first = res[0].split("-")  # First elf
            second = res[1].split("-")  # Second elf

            # Converting into a list of assignments
            first = list(range(int(first[0]), int(first[1]) + 1))
            second = list(range(int(second[0]), int(second[1]) + 1))

            entry = (first, second)
            list_of_pairs.append(entry)

# If all in list 1 are in list 2 or vice-versa
# return True
def compare_lists_all(list1, list2):
    if all(item in list1 for item in list2):
        return True
    elif all(item in list2 for item in list1):
        return True
    return False


# If any in list 1 are in list 2 or vice-versa
# return True
def compare_lists_any(list1, list2):
    if any(item in list1 for item in list2):
        return True
    elif any(item in list2 for item in list1):
        return True
    return False


count_p1 = 0  # answer for part 1
count_p2 = 0  # answer for part 2

for assignment in list_of_pairs:
    one = assignment[0]
    two = assignment[1]

    if compare_lists_all(one, two):
        count_p1 += 1
    if compare_lists_any(one, two):
        count_p2 += 1


print(count_p1)
print(count_p2)
