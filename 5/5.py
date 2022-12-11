import re
from pprint import pprint

crate_stacks = []

stacks_line_regexp = r'[\[\s]([A-Z]|\s)[\]\s]\s'
movement_regexp = r'move (\d{1,2}) from (\d{1,2}) to (\d{1,2})'

with open("input") as fp:
    while True:
        # Crate array builder

        line = fp.readline()

        if line.startswith(' 1'):
            break

        matched_line = re.findall(stacks_line_regexp, line)

        for index, potential_crate in enumerate(matched_line):
            if len(crate_stacks) == index:
                crate_stacks.append([])

            if potential_crate != ' ':
                crate_stacks[index].append(potential_crate)
        
    pprint(crate_stacks)

    # skip empty line
    fp.readline()

    while True:
        # Crate updater
        line = fp.readline()

        if not line:
            pprint(crate_stacks)
            break

        # print(line)

        matched_line = [int(value) for value in re.findall(movement_regexp, line)[0]]

        for i in range(matched_line[0]):
            try:
                crate_stacks[matched_line[2] - 1].insert(0, crate_stacks[matched_line[1] - 1].pop(0))
            except IndexError:
                pass  
        
print(''.join([stack[0] for stack in crate_stacks]))
        