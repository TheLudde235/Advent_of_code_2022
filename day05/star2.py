def pop_im(l: list, a: int) -> [list, list]:
    o = []
    for _ in range(a):
        o.insert(0, l.pop())
    return o, l


def move(a: int, f: int, t: int):
    removed_items, non_removed_items = pop_im(stacks_list[f-1], a)
    print(removed_items, non_removed_items)
    stacks_list[f - 1] = non_removed_items
    stacks_list[t - 1].extend(removed_items)


inp = open('input.txt').read().split('\n')
row_list: list = list()
move_list: list = list()
amount_of_stacks: int = 0
moves_part = False

for line in inp:
    if moves_part:
        if line:
            move_list.append(line)
    else:
        if line.split()[0] == '1':
            amount_of_stacks = int(line.split()[-1])
            moves_part = True
        else:
            row_list.append(line)

row_list.reverse()

stacks_list: list[list[str]] = [[] for x in range(amount_of_stacks)]
current_stack = 0

for layer in row_list:
    for i in range(amount_of_stacks):
        if i * 4 < len(layer) and layer[1 + i * 4] != ' ':
            stacks_list[i].append(layer[1 + i * 4])

print(stacks_list)

for mo in move_list:
    m = mo.split()
    amount = int(m[1])
    fr = int(m[3])
    to = int(m[5])
    move(amount, fr, to)
    print(mo)
    print(stacks_list)

out = ''
for stack in stacks_list:
    out += stack[-1]

print(out)
