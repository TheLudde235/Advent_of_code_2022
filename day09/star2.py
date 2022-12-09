inp = open('input.txt').read().split('\n')


def touching(head_index: tuple[int, int], tail_index: tuple[int, int]) -> bool:
    return abs(head_index[0] - tail_index[0]) <= 1 and abs(head_index[1] - tail_index[1]) <= 1


def move(head_index: tuple[int, int], tail_index: tuple[int, int]) -> tuple[int, int]:
    if touching(head_index, tail_index):
        return tail_index

    if head_index[0] == tail_index[0]:
        if head_index[1] > tail_index[1]:
            return tail_index[0], tail_index[1] + 1
        return tail_index[0], tail_index[1] - 1

    elif head_index[1] == tail_index[1]:
        if head_index[0] > tail_index[0]:
            return tail_index[0] + 1, tail_index[1]
        return tail_index[0] - 1, tail_index[1]
    else:
        if head_index[1] < tail_index[1]:
            if head_index[0] < tail_index[0]:
                return tail_index[0] - 1, tail_index[1] - 1
            return tail_index[0] + 1, tail_index[1] - 1
        else:
            if head_index[0] < tail_index[0]:
                return tail_index[0] - 1, tail_index[1] + 1
            return tail_index[0] + 1, tail_index[1] + 1


prev_set: set[tuple[int, int]] = set()

knot_que: list[tuple[int, int]] = [(100_000, 100_000) for _ in range(10)]
print(knot_que)

for line in inp:
    [direction, speed] = line.split()
    speed = int(speed)
    for step in range(speed):
        if direction == 'U':
            knot_que[0] = knot_que[0][0] - 1, knot_que[0][1]
        elif direction == 'D':
            knot_que[0] = knot_que[0][0] + 1, knot_que[0][1]
        elif direction == 'L':
            knot_que[0] = knot_que[0][0], knot_que[0][1] - 1
        else:
            knot_que[0] = knot_que[0][0], knot_que[0][1] + 1

        for i in range(1, len(knot_que)):
            knot_que[i] = move(knot_que[i - 1], knot_que[i])
        prev_set.add(knot_que[-1])
print(len(prev_set))
