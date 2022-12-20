from pprint import pprint
from typing import Protocol, TypeVar


class SimpleGraph:
    def __init__(self):
        self.edges: dict[int, list[int]] = {}

    def neighbors(self, index: int) -> list[int]:
        return self.edges[index]


line_width = 0
map = []

with open("input") as fp:
    while True:
        line = fp.readline()
        if not line:
            break

        clean_line = line.strip()

        if not line_width:
            line_width = len(clean_line)

        map += [letter for letter in list(clean_line)]

start_index = map.index("S")
end_index = map.index("E")

map[start_index] = "a"
map[end_index] = "z"

height_map = [ord(letter) - 97 for letter in map]

print(height_map)

possible_neighbours = {}

# Finding all the possible_neighbours
for index, value in enumerate(height_map):
    neighbours = []

    # above
    if index - line_width >= 0 and height_map[index - line_width] <= value + 1:
        neighbours.append(index - line_width)

    # below
    if (
        index + line_width < len(height_map)
        and height_map[index + line_width] <= value + 1
    ):
        neighbours.append(index + line_width)

    # right
    if (index + 1) % line_width != 0 < len(height_map) and height_map[
        index + 1
    ] <= value + 1:
        neighbours.append(index + 1)

    # left
    if index % line_width != 0 and height_map[index - 1] <= value + 1:
        neighbours.append(index - 1)

    possible_neighbours[index] = neighbours

pprint(possible_neighbours)

frontier = [start_index]
came_from = {}
came_from[start_index] = None

while frontier:
    current = frontier.pop(0)

    if current == end_index:  # early exit
        break

    for next in possible_neighbours[current]:
        if next not in came_from:
            frontier.append(next)
            came_from[next] = current


length = 0
next_index = came_from[end_index]
while True:
    if next_index == None:
        break

    length += 1
    next_index = came_from[next_index]

print(length)
