score = 0

with open("input") as fp:
    while True:
        line = fp.readline()
        if not line:
            break

        opponent, outcome = line.strip().split(' ')
        opponent_value = ord(opponent) - 64 # So A, B, C become 1, 2, 3 respectively
        outcome_value = (ord(outcome) - 88) # So X, Y, Z become 0, 1, 2 respectively
        
        # This problem was solvable with some math trial and error
        score += (outcome_value) * 3 + ((opponent_value + (outcome_value - 2)) % 3) + 1

print(score)
