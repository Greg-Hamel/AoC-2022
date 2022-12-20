sum_right_index = 0


def make_same_type(left, right):
    if type(left) != type(right):
        if type(left) == int:
            left = [left]
        if type(right) == int:
            right = [right]

    return left, right


def is_right_order(left, right):
    print(f"compare {left} vs {right}")
    # ensure int vs int or list vs list
    left, right = make_same_type(left, right)

    if type(left) == int:
        if left == right:
            return None

        return left < right

    for idx in range(len(left)):
        try:
            result = is_right_order(left[idx], right[idx])
            if result is None:
                continue
            return result
        except IndexError:
            print("Right side ran out of items, wrong order")
            return False

    if len(left) < len(right):
        print("Left side ran out of items, right order")
        return True
    return None


with open("input") as fp:
    index = 1
    while True:
        first = eval(fp.readline().strip())
        second = eval(fp.readline().strip())
        blank = fp.readline()
        if not blank:
            break

        print(f"== Pair {index} ==")
        if is_right_order(first, second):
            print("Right Order")
            sum_right_index += index
        else:
            print("Wrong Order")

        index += 1

print(f"sum of indices: {sum_right_index}")
