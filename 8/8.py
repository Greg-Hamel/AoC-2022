from pprint import pprint
tree_patch = []

with open("input") as fp:
    while True:
        line = fp.readline().strip()
        if not line:
            break

        tree_patch.append([int(tree_height) for tree_height in list(line)])


pprint(tree_patch)

visible_tree_count = 0

tree_patch_columns = []
for index in range(len(tree_patch[0])):
    column = []
    for row in tree_patch:
        column.append(row[index])

    tree_patch_columns.append(column)

for row_index, current_row in enumerate(tree_patch):
    for column_index, current_column in enumerate(tree_patch_columns):
        if row_index in [0, len(current_row) - 1] or column_index in [0, len(current_column) - 1]:
            visible_tree_count += 1
            continue

        current_tree_height = tree_patch[row_index][column_index]

        for direction in range(2):
            if direction == 0:
                row_left = current_row[:column_index]
                row_right = current_row[column_index + 1:]

                higher_trees_left = sum([min(max((tree + 1) - current_tree_height, 0), 1) for tree in row_left])
                higher_trees_right = sum([min(max((tree + 1) - current_tree_height, 0), 1) for tree in row_right])
                
                if higher_trees_left == 0 or higher_trees_right == 0:
                    visible_tree_count += 1
                    break
                
            if direction == 1:
                column_up = current_column[:row_index]
                column_down = current_column[row_index + 1:]

                higher_trees_up = sum([min(max((tree + 1)  - current_tree_height, 0), 1) for tree in column_up])
                higher_trees_down = sum([min(max((tree + 1)  - current_tree_height, 0), 1) for tree in column_down])
                
                if higher_trees_up == 0 or higher_trees_down == 0:
                    visible_tree_count += 1
                    break

print('Total number of visible trees:', visible_tree_count)