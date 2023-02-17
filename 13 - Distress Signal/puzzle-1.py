import json
import copy

data = []
with open("test.txt") as infile:
    count = 0
    compare = [[], []]
    for line in infile:
        row = line.strip()
        if row:
            compare[count] = json.loads(row)
            count += 1
            if count == 2:
                count = 0
                data.append(compare)
                compare = [[], []]


def compare_items(pair):
    left = pair[0]
    right = pair[1]

    for i in range(len(left)):
        if i > len(right) - 1:
            return True

        if type(left[i]) == list and type(right[i]) == list:
            s_left = deconstruct(left[i])
            s_right = deconstruct(right[i])

        elif type(left[i]) == list and type(right[i]) == int:
            s_left = deconstruct(left[i])
            s_right = [right[i]] * len(left[i])

        elif type(left[i]) == int and type(right[i]) == list:
            s_left = [left[i]] * len(right[i])
            s_right = deconstruct(right[i])

    if i < len(right) - 1:
        return False

    return None

    #     if type(s_left) == list and type(s_right) == list:
    #         for j in range(len(s_left)):
    #             #print(s_left, s_right, i)
    #             if s_left[i] < s_right[j]:
    #                 return True
    #             if s_left[i] > s_right[j]:
    #                 return False
    #         if len(s_left) < len(s_right):
    #             return False
    #         elif len(s_left) > len(s_right):
    #             return True
    #     if type(s_left) == int and type(s_right) == list:
    #         s_left = [s_left] * len(s_right)
    #         for j in range(len(s_left)):
    #             if s_left[i] < s_right[j]:
    #                 return True
    #             if s_left[i] > s_right[j]:
    #                 return False
    #         if len(s_left) < len(s_right):
    #             return False
    #         elif len(s_left) > len(s_right):
    #             return True
    #     if type(s_left) == list and type(s_right) == int:
    #         s_right = [s_right] * len(s_left)
    #         for j in range(len(s_left)):
    #             if s_left[i] < s_right[j]:
    #                 return True
    #             if s_left[i] > s_right[j]:
    #                 return False
    #         if len(s_left) < len(s_right):
    #             return False
    #         elif len(s_left) > len(s_right):
    #             return True
    #     else:
    #         if s_left < s_right:
    #             return True
    #         if s_left > s_right:
    #             return False
    # if len(left) > len(right):
    #     return True
    # if len(left) < len(right):
    #     return False
    # return None


def check_rules(left, right):
    pass


def deconstruct(item):
    if type(item) == list:
        if len(item) == 0:
            return item
        if type(item[0]) == list:
            return deconstruct(item[0])
        else:
            return item
    return item


for pair in data:
    print(compare_items(pair))
