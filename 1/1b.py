elve = []

with open("input") as fp:
    current_elf = 0
    while True:
        line = fp.readline()

        if not line:
            break

        if line == "\n":
            elve.append(current_elf)
            current_elf = 0
        else:
            current_elf = current_elf + int(line.strip())


elve.sort(reverse=True)
print(sum(elve[:3]))
