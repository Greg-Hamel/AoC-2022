
elves_group = []
prio_sum = 0

def value_to_prio(value: str) -> int:
    ordinal = ord(value)

    if ordinal > 90:
        return ordinal - 96
    else:
        return ordinal - 38

with open("input") as fp:
    while True:
        line = fp.readline()
        if not line:
            break

        if len(elves_group) < 3:
            elves_group.append(set(line.strip()))

        if len(elves_group) == 3:
            common_item = elves_group[0].intersection(elves_group[1]).intersection(elves_group[2])
            prio_sum += value_to_prio(common_item.pop())
            elves_group = []

print(prio_sum)