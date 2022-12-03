inp = open('input.txt').read().split('\n')

current_calories: int = 0
koth: int = 0

for line in inp:
    if line == '':
        if current_calories > koth:
            koth = current_calories
        current_calories = 0
    else:
        current_calories += int(line)

print(koth)