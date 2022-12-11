DIRECTION_MAPPING = {
    'U': [0, 1],
    'D': [0, -1],
    'L': [-1, 0],
    'R': [1, 0],
}

head_position = [0,0]
tail_position = [0,0]
tail_positions = set()

def new_tail_position(h_position, t_position):
    h_displacement = t_position[0] - h_position[0]
    v_displacement = t_position[1] - h_position[1]

    if (h_displacement ** 2 + v_displacement ** 2) ** 0.5 >= 2:
        return [t_position[0] - min(max(h_displacement, -1), 1), t_position[1] - min(max(v_displacement, -1), 1)]

    return t_position

with open("input") as fp:
    while True:
        line = fp.readline().strip()
        if not line:
            break

        direction, amount = line.split(' ')

        for i in range(int(amount)):
            head_position = [head_position[0] + DIRECTION_MAPPING[direction][0], head_position[1] + DIRECTION_MAPPING[direction][1]]
            tail_position = new_tail_position(head_position, tail_position)
            tail_positions.add(','.join([ str(unit) for unit in tail_position ]))

print('Head end position:', head_position)
print('Tail end position:', tail_position)
print(len(tail_positions))