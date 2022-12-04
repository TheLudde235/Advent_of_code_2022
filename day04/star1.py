inp = open('input.txt').read().split('\n')

score: int = 0

for line in inp:
    [elf1, elf2] = line.split(',')

    elf1_set: set = {*range(int(elf1.split('-')[0]), int(elf1.split('-')[1]) + 1)}
    elf2_set: set = {*range(int(elf2.split('-')[0]), int(elf2.split('-')[1]) + 1)}

    all_in_one: bool = True

    for chore in elf1_set:
        if chore not in elf2_set:
            all_in_one = False

    if not all_in_one:
        all_in_one = True
        for chore in elf2_set:
            if chore not in elf1_set:
                all_in_one = False

    if all_in_one:
        score += 1

print(score)
