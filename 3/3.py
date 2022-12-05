priorities = 0

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

        line = line.strip()
        
        first_compartment = set(line[:(len(line)//2)])
        second_compartment = set(line[(len(line)//2):])

        intersection = first_compartment.intersection(second_compartment)

        priorities += value_to_prio(intersection.pop())

print(priorities)