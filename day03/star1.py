inp = open('input.txt').read().split()


def get_score(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


score: int = 0

for line in inp:
    first_half = slice(0, len(line)//2)
    last_half = slice(len(line)//2, len(line))
    firsts: set[str] = set(line[first_half])

    for ch in line[last_half]:
        if ch in firsts:
            score += get_score(ch)
            firsts.remove(ch)
print(score)