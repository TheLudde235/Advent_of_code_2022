inp = open('input.txt').read().split()

signal_strength: list = list()
v = 0
x: int = 1
cycle: int = 0
index: int = 0

while True:
    if v != 0:
        x += v
        v = 0
    if inp[index] == 'noop':
        cycle += 1
    elif inp[index] == 'addx':
        cycle += 1
    else:
        v = int(inp[index])
        cycle += 1
    if cycle in {20, 60, 100, 140, 180, 220}:
        signal_strength.append(cycle * x)
    if cycle == 220:
        break
    index += 1


print(sum(signal_strength))
