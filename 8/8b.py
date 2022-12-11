from pprint import pprint
from functools import reduce
tree_patch = []

with open("input") as fp:
    while True:
        line = fp.readline().strip()
        if not line:
            break

        tree_patch.append([int(tree_height) for tree_height in list(line)])


pprint(tree_patch)

result = 0

tree_patch_columns = []
for index in range(len(tree_patch[0])):
    column = []
    for row in tree_patch:
        column.append(row[index])

    tree_patch_columns.append(column)

for row_index, current_row in enumerate(tree_patch):
    for column_index, current_column in enumerate(tree_patch_columns):
        if row_index in [0, len(current_row) - 1] or column_index in [0, len(current_column) - 1]:
            continue

        row_left = current_row[:column_index]
        row_left.reverse()
        row_right = current_row[column_index + 1:]

        column_up = current_column[:row_index]
        column_up.reverse()
        column_down = current_column[row_index + 1:]

        tree_count_multiplication = 1
        current_tree_height = tree_patch[row_index][column_index]

        for view in [row_left, row_right, column_up, column_down]:
            for tree_index, tree in enumerate(view):
                if tree >= current_tree_height or tree_index == len(view) - 1:
                    tree_count_multiplication *= tree_index + 1
                    break

        print([row_index, column_index], tree_count_multiplication)
        # print(visible_trees)

        # tree_count_multiplication = reduce(lambda a, b: a*b, visible_trees) if len(visible_trees) > 0 
        if tree_count_multiplication > result:
            result = tree_count_multiplication

print('Max multiplied view :', result)