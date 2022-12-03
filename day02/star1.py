inp: list[str] = open('input.txt').read().split('\n')

beating_hands: dict = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

drawing_hands: dict = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

score_dict: dict = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

score: int = 0

for line in inp:
    if line[-1] == beating_hands[line[0]]:
        score += 6
    elif line[-1] == drawing_hands[line[0]]:
        score += 3
    score += score_dict[line[-1]]

print(score)