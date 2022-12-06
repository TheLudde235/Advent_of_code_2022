inp = open('input.txt').read()

for i in range(3, len(inp)):
    s = {inp[i - 3]}
    if inp[i-2] in s:
        continue
    s.add(inp[i-2])
    if inp[i-1] in s:
        continue
    s.add(inp[i-1])
    if inp[i] not in s:
        print(i+1)
        break