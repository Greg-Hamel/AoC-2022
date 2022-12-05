elf_with_most = 0
current_elf = 0

number_of_empty_string = 0

with open("input") as fp:
    while True:
        line = fp.readline()

        if not line:
            break

        if line == "\n":
            if current_elf > elf_with_most:
                elf_with_most = current_elf
                print("New most!", current_elf)
            current_elf = 0
        else:
            current_elf = current_elf + int(line.strip())


print(elf_with_most)
