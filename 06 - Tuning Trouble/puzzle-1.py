import sys

sys.setrecursionlimit(10000)  # Python default is 1,000 :(

# Read in data
with open("input.txt") as infile:
    data = infile.read()


def find_first_marker(data, pos, length):
    if pos >= len(data):
        return None  # Terminates recursion, none found
    # Start of search ignore first chars
    if pos < length:
        return find_first_marker(data, pos + 1, length)

    # Set() finds unique characters in a list
    # If that length is the same as the list by itself we have a unique
    # set of characters
    if len(set(data[pos - length : pos])) == len(data[pos - length : pos]):
        return pos  # Terminates recursion, answer found
    else:
        return find_first_marker(data, pos + 1, length)  # Recursion


# Given test case:
# data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

# Part One
print(find_first_marker(data, 0, 4))
# Answer = 1,480

# Part Two
print(find_first_marker(data, 0, 14))
# Answer = 2,746
