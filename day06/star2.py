inp = open('input.txt').read()


def calculate_depending_on_depth(depth: int, message: str) -> int:
    for i in range(depth - 1, len(message)):
        s = {inp[i]}
        specific = True
        for j in range(1, depth):
            print(inp[i-j])
            if inp[i-j] in s:
                specific = False
                break
            s.add(inp[i-j])
        if specific:
            print(s)
            return i+1


print(calculate_depending_on_depth(14, inp))
