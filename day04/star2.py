inp = open('input.txt').read().split('\n')

score: int = 0

for line in inp:
    [elf1, elf2] = line.split(',')

    elf1_set: set = {*range(int(elf1.split('-')[0]), int(elf1.split('-')[1]) + 1)}
    elf2_set: set = {*range(int(elf2.split('-')[0]), int(elf2.split('-')[1]) + 1)}

    for chore in elf1_set:
        if chore in elf2_set:
            score += 1
            break

print(score)
