inp = open('input.txt').read().split()


def print_pixels(px_list: list):
    for i in range(len(px_list) // 40):
        out: str = ''
        for item in px_list[i*40:i*40+40]:
            out += item
        print(out)


signal_strength: list = list()
v = 0
x: int = 1
cycle: int = 0
index: int = 0

pixels: list = []

while True:
    x += v
    v = 0
    if inp[index] == 'noop':
        cycle += 1
    elif inp[index] == 'addx':
        cycle += 1
    else:
        v = int(inp[index])
        cycle += 1
    row = cycle // 40
    if cycle == x + row * 40 or cycle == x + 1 + row * 40 or cycle == x + 2 + row * 40:
        pixels.append('#')
    else:
        pixels.append(' ')

    if cycle in {20, 60, 100, 140, 180, 220}:
        signal_strength.append(cycle * x)
    if cycle == 240:
        break
    index += 1

print_pixels(pixels)
