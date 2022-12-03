def main():
    inp: list[str] = open('input.txt').read().split()

    score: int = 0

    backpacks: list[set[str]] = [{''}, {''}, {''}]
    group_index: int = 0

    for line in inp:
        backpacks[group_index] = set(line)
        group_index += 1
        if group_index == 3:
            for ch in backpacks[0]:
                if ch in backpacks[1] and ch in backpacks[2]:
                    score += get_score(ch)
            group_index = 0
    print(score)


def get_score(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


main()
