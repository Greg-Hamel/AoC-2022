from functools import cmp_to_key
from pprint import pprint

sort_array = ["[[2]]", "[[6]]"]


def make_same_type(left, right):
    if type(left) != type(right):
        if type(left) == int:
            left = [left]
        if type(right) == int:
            right = [right]

    return left, right


def is_right_order(left, right):
    print(f"compare {left} vs {right}")
    if type(left) == str:
        left = eval(left)
        right = eval(right)

    # ensure int vs int or list vs list
    left, right = make_same_type(left, right)

    if type(left) == int:
        return left - right

    for idx in range(len(left)):
        try:
            result = is_right_order(left[idx], right[idx])
            if result == 0:
                continue
            return result
        except IndexError:
            print("Right side ran out of items, wrong order")
            return 1

    if len(left) < len(right):
        print("Left side ran out of items, right order")
        return -1
    return 0


with open("input") as fp:
    index = 1
    while True:
        line = fp.readline()
        if line == "\n":
            continue

        if not line:
            break

        sort_array.append(line.strip())

sorted_array = sorted(sort_array, key=cmp_to_key(is_right_order))

pprint((sorted_array.index("[[2]]") + 1) * (sorted_array.index("[[6]]") + 1))
