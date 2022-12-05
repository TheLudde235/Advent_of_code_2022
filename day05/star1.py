inp = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''.split('\n')

row_list: list = list()
amount_of_stacks: int = 0
for line in inp:
    if line.split()[0] == '1':
        amount_of_stacks = int(line.split()[-1])
        break
    row_list.append(line)
row_list.reverse()

stacks_list: list[list[str]] = [[] for x in range(amount_of_stacks)]
current_stack = 0

for layer in row_list:
    current_stack = 0
    for stack in layer.split():
        print(stack, current_stack)
        stacks_list[current_stack].append(stack[1])
        current_stack += 1
print(stacks_list)
