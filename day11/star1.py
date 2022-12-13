inp = open('input.txt').read().split('\n\n')

class Monkey:
    items: list[int]
    operation: str
    test: int
    true_test: int
    false_test: int
    inspect: int

    def __init__(self, items, operation, test, true_test, false_test): # noqa
        self.items = items
        self.operation = operation
        self.test = test
        self.true_test = true_test
        self.false_test = false_test
        self.inspected = 0

    def inspect(self, worry_level: int) -> int:
        self.inspected += 1
        return eval(self.operation.replace('old', worry_level.__str__()))

    def append_item(self, item: int):
        self.items.append(item)

    def remove_items(self, items: list):
        for item in items:
            if self.items.index(item) >= 0:
                self.items.remove(item)
            else:
                print('hakjdahhakjdhakjhd')


monkeys: list[Monkey] = list()

for monkey in inp:
    line = monkey.split('\n')
    items = eval(f'[{line[1].split(": ")[1]}]')
    operation = line[2].split('= ')[1]
    test = int(line[3].split()[-1])
    true_test = int(line[4].split()[-1])
    false_test = int(line[5].split()[-1])
    monkeys.append(Monkey(items, operation, test, true_test, false_test))


def complete_round():
    for monke in monkeys:
        removed = list()
        for item in monke.items:
            inspected_item = (monke.inspect(item) // 3)
            print(inspected_item, monke.test, inspected_item % monke.test == 0)
            if inspected_item % monke.test == 0:
                monkeys[monke.true_test].append_item(inspected_item)
            else:
                monkeys[monke.false_test].append_item(inspected_item)
            removed.append(item)
        monke.remove_items(removed)


for _ in range(20):
    complete_round()

product: int = 1

m1 = 0
m2 = 0

for monkey in monkeys:
    if monkey.inspected > m1:
        m1 = monkey.inspected
    elif monkey.inspected > m2:
        m2 = monkey.inspected


print(m1 * m2)
