def move(amount: int, f: int, t: int):
    for x in range(amount):
        removed_item = stacks_list[f - 1].pop(-1)
        stacks_list[t - 1].append(removed_item)


inp = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''.split('\n')

# inp = open('input.txt').read().split('\n')
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
print(move_list)

for mo in move_list:
    m = mo.split()
    amount = int(m[1])
    fr = int(m[3])
    to = int(m[5])
    move(amount, fr, to)

out = ''
for stack in stacks_list:
    out += stack[-1]
print(out)