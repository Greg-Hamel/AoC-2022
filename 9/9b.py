DIRECTION_MAPPING = {
    'U': [0, 1],
    'D': [0, -1],
    'L': [-1, 0],
    'R': [1, 0],
}
ROPE_LENGTH = 10


knot_positions = [[0,0] for knot in range(10)]
tail_positions = set()

def new_knot_position(leading_knot, trailing_knot):
    h_displacement = trailing_knot[0] - leading_knot[0]
    v_displacement = trailing_knot[1] - leading_knot[1]

    if (h_displacement ** 2 + v_displacement ** 2) ** 0.5 >= 2:
        return [trailing_knot[0] - min(max(h_displacement, -1), 1), trailing_knot[1] - min(max(v_displacement, -1), 1)]

    return trailing_knot

with open("input") as fp:
    while True:
        line = fp.readline().strip()
        if not line:
            break

        direction, amount = line.split(' ')

        for i in range(int(amount)):
            knot_positions[0] = [knot_positions[0][0] + DIRECTION_MAPPING[direction][0], knot_positions[0][1] + DIRECTION_MAPPING[direction][1]]
            for index in range(ROPE_LENGTH - 1):
                knot_positions[index + 1] = new_knot_position(knot_positions[index], knot_positions[index + 1])
                if index == ROPE_LENGTH - 2:
                    tail_positions.add(','.join([ str(unit) for unit in knot_positions[index + 1]]))

print('Head end position:', knot_positions[0])
print('Tail end position:', knot_positions[-1])
print(len(tail_positions))