contained_count = 0

def make_binary(value_list: list[str]) -> list[int]:
    '''
    Generate list of integers from all `str` within the array

    ['1-2', '2-6'] -> [0b11, 0b0111110]

    '''
    output = []

    for value in value_list:
        # Evaluate integer bit-value of range
        range_start, range_end = [int(val) for val in value.split('-')]
        
        range_length = range_end - range_start + 1

        range_value = int('1' * range_length, 2) << (range_start - 1)
        
        output.append(range_value)

    return output

with open("input") as fp:
    while True:
        line = fp.readline()

        if not line:
            break
        
        elf1, elf2 = make_binary(line.strip().split(','))

        if elf1 & elf2 > 1:
            contained_count += 1

print(contained_count)