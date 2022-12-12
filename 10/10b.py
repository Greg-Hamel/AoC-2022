from computer import CPU, CRTDisplay

program = []

with open("input") as fp:
    while True:
        line = fp.readline().strip()
        if not line:
            break

        program.append(line)

cpu = CPU()
crt = CRTDisplay()
cpu.set_program(program)
cpu.connect(crt)

while True:
    try:
        cpu.run()

    except EOFError:
        break
