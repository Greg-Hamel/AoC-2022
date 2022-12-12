from computer import CPU

program = []

with open("input") as fp:
    while True:
        line = fp.readline().strip()
        if not line:
            break

        program.append(line)

cpu = CPU()
cpu.set_program(program)

signal_strength_sum = 0

while True:
    try:
        cpu.clock_signal(0)
        # During
        if (cpu.clock_counter - 20) % 40 == 0:
            signal_strength_sum += cpu.clock_counter * cpu.x_register
        cpu.clock_signal(1)
        # After

    except EOFError:
        break

print(signal_strength_sum)