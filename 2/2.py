score = 0

with open("input") as fp:
    while True:
        line = fp.readline()
        if not line:
            break

        opponent, me = line.strip().split(' ')
        opponent_value = ord(opponent) - 64 # So A, B, C become 1, 2, 3 respectively
        me_value = ord(me) - 87 # So X, Y, Z become 1, 2, 3 respectively
        
        # This problem was solvable with some math trial and error
        score += (((me_value - opponent_value) + 4) % 3) * 3 + me_value

print(score)