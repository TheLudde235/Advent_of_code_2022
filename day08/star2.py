inp = open('input.txt').read().split('\n')


def viewing_distance(row_index: int, col_index: int) -> int:
    tree_length: int = int(inp[row_index][col_index])
    # Left
    current_view = 0
    for h in list(inp[row_index][:col_index]).__reversed__():
        curr_tree = int(h)
        current_view += 1
        if curr_tree >= tree_length:
            break
    total_view = current_view

    # Right
    current_view = 0
    for h in inp[row_index][col_index + 1:]:
        curr_tree = int(h)
        current_view += 1
        if curr_tree >= tree_length:
            break
    total_view *= current_view

    # Down
    current_view = 0
    for h in inp[row_index + 1:]:
        curr_tree = int(h[col_index])
        current_view += 1
        if curr_tree >= tree_length:
            break
    total_view *= current_view

    # Up
    current_view = 0
    for h in inp[:row_index].__reversed__():
        curr_tree = int(h[col_index])
        current_view += 1
        if curr_tree >= tree_length:
            break
    total_view *= current_view

    return total_view


koth: int = 0

for r in range(len(inp)):
    for c in range(len(inp[r])):
        scenic_score: int = viewing_distance(r, c)
        if scenic_score > koth:
            koth = scenic_score
print(koth)
