from pprint import pprint

TOTAL_DISK_SPACE = 70000000
SPACE_REQUIRED = 30000000

def analyze_dir(fp, current_location, filesystem):
    location = '/'.join(current_location)
    dir_total = 0
    listing = False
    while True:
        line = fp.readline().strip()

        if not line:
            break

        line_components = line.split(' ')

        if listing and line_components[0] == '$':
            listing = False

        if listing:
            if line_components[0] == 'dir':
                continue
            
            file_size = int(line_components[0])

            dir_total += int(file_size)
            filesystem[location + f'/{line_components[1]}'] = file_size
        else:
            if line_components[1] == 'ls':
                listing = True
            elif line_components[1] == 'cd':
                if line_components[2] == '..':
                    break
                elif line_components[2] == '/':
                    pass
                else: 
                    sub_dir, _ = analyze_dir(fp, current_location + [line_components[2]], filesystem)
                    dir_total += sub_dir

    filesystem[location + '/'] = dir_total
    return dir_total, filesystem


with open("input") as fp:
    root_total, fs = analyze_dir(fp, [], {})
    pprint(fs)

print('total disk usage:', fs['/'])
needed_size = SPACE_REQUIRED - (TOTAL_DISK_SPACE - fs['/'])
print('space to be cleared:', needed_size)

potential_directories = []

for item in fs:

    if item[-1] == '/':
        directory_size = fs[item]
        if directory_size > needed_size:
            potential_directories.append(directory_size)


potential_directories.sort()

print(potential_directories)




