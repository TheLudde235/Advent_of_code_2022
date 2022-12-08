inp = open('input.txt').read().split('\n')


def isvisible(row_index: int, col_index: int) -> bool:
    if row_index <= 0 or col_index <= 0 or row_index >= len(inp) - 1 or col_index >= len(inp) - 1:
        return True
    tree_length: int = int(inp[row_index][col_index])
    highest: int = 0
    for h in inp[row_index][:col_index]:
        curr_tree = int(h)
        if curr_tree > highest:
            highest = curr_tree
    if highest < tree_length:
        return True
    highest = 0
    for h in inp[row_index][col_index + 1:]:
        curr_tree = int(h)
        if curr_tree > highest:
            highest = curr_tree
    if highest < tree_length:
        return True
    highest = 0
    for h in inp[:row_index]:
        curr_tree = int(h[col_index])
        if curr_tree > highest:
            highest = curr_tree
    if highest < tree_length:
        return True
    highest = 0
    for h in inp[row_index + 1:]:
        curr_tree = int(h[col_index])
        if curr_tree > highest:
            highest = curr_tree
    if highest < tree_length:
        return True
    return False


visible_trees: int = 0

for row_index in range(len(inp)):
    for col_index in range(len(inp[row_index])):
        if isvisible(row_index, col_index):
            visible_trees += 1

print(visible_trees)
