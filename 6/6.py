non_repetitive_length = 4
first_marker_index = 0

with open("input") as fp:
    line = fp.readline()        
    
    stream = list(line)

    for index, byte in enumerate(stream):
        if index < non_repetitive_length - 1:
            continue

        current_fourteen_set = set(stream[index - (non_repetitive_length - 1):index + 1])

        if len(current_fourteen_set) == non_repetitive_length:
            first_marker_index = index + 1
            break

print(first_marker_index)