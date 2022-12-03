inp: list[str] = open('input.txt').read().split('\n')

winning_score: dict = {
    'A': 2,
    'B': 3,
    'C': 1
}

drawing_scores: dict = {
    'A': 1,
    'B': 2,
    'C': 3
}

losing_scores: dict = {
    'A': 3,
    'B': 1,
    'C': 2
}

actions: dict = {
    'X': losing_scores,
    'Y': drawing_scores,
    'Z': winning_score
}

scores: dict = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

score: int = 0

for line in inp:
    score += actions[line[-1]][line[0]] + scores[line[-1]]
print(score)