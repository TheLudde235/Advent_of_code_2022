inp = open('input.txt').read().split('\n')


def touching(head_index: tuple[int, int], tail_index: tuple[int, int]) -> bool:
    return abs(head_index[0] - tail_index[0]) <= 1 and abs(head_index[1] - tail_index[1]) <= 1


def move(head_index: tuple[int, int], tail_index: tuple[int, int]) -> tuple[int, int]:
    if touching(head_index, tail_index):
        return tail_index

    # row
    if head_index[0] == tail_index[0]:
        if head_index[1] > tail_index[1]:
            return tail_index[0], tail_index[1] + 1
        return tail_index[0], tail_index[1] - 1
    # col
    elif head_index[1] == tail_index[1]:
        if head_index[0] > tail_index[0]:
            return tail_index[0] + 1, tail_index[1]
        return tail_index[0] - 1, tail_index[1]
    # diagonal
    else:
        # left
        if head_index[1] < tail_index[1]:
            # top
            if head_index[0] < tail_index[0]:
                return tail_index[0] - 1, tail_index[1] - 1
            return tail_index[0] + 1, tail_index[1] - 1
        # right
        else:
            # top
            if head_index[0] < tail_index[0]:
                return tail_index[0] - 1, tail_index[1] + 1
            return tail_index[0] + 1, tail_index[1] + 1


prev_set: set[tuple[int, int]] = set()

head: tuple[int, int] = (100_000, 100_000)
tail: tuple[int, int] = (100_000, 100_000)
for line in inp:
    [direction, speed] = line.split()
    speed = int(speed)

    for step in range(speed):
        if direction == 'U':
            head = head[0] - 1, head[1]
        elif direction == 'D':
            head = head[0] + 1, head[1]
        elif direction == 'L':
            head = head[0], head[1] - 1
        else:
            head = head[0], head[1] + 1

        tail = move(head, tail)
        prev_set.add(tail)
print(len(prev_set))
