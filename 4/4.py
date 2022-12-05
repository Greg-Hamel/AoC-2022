contained_count = 0

def make_binary(value_list: list[str]) -> list[int]:
    '''
    Generate list of integers of same bit-length between all `str` within the array

    ['1-2', '2-6'] -> [0b110000, 0b0111111]

    '''
    output = []

    max_range = 0

    for value in value_list:
        # Evaluate integer bit-value of range
        range_start, range_end = [int(val) for val in value.split('-')]
        
        if range_end > max_range:
            max_range = range_end

        binary_value = ''
        
        for index in range(range_end):
            binary_value += '1' if range_start - 1 <= index < range_end else '0'
        
        output.append(binary_value)

    # 0-pad shortest by difference in size.
    required_length = max(len(output[1]), len(output[0]))

    for index, output_value in enumerate(output):
        if len(output_value) < required_length:
            output[index] = output_value.ljust(required_length, '0')


    return [int(output_value, 2) for output_value in output]

with open("input") as fp:
    while True:
        line = fp.readline()
        if not line:
            break

        value1, value2 = make_binary(line.strip().split(','))
        anded = value1 & value2

        if anded and (anded == value1 or anded == value2):
            contained_count += 1

print(contained_count)