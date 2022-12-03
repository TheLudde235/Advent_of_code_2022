inp = open('input.txt').read().split('\n')

current_calories: int = 0
koths: list[int] = [0, 0, 0]

for line in inp:
    if line == '':
        if current_calories > koths[0]:
            if current_calories > koths[1]:
                if current_calories > koths[2]:
                    koths[0] = koths[1]
                    koths[1] = koths[2]
                    koths[2] = current_calories
                else:
                    koths[0] = koths[1]
                    koths[1] = current_calories
            else:
                koths[0] = current_calories
        current_calories = 0
    else:
        current_calories += int(line)

print(sum(koths))