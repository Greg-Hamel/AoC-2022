import typing


class Monkey:
    all_monkeys = []

    def __init__(
        self,
        starting_items: list[int],
        operation: str,
        test: str,
        if_true: int,
        if_false: int,
    ) -> None:
        self.monkey_number = len(Monkey.all_monkeys)
        Monkey.all_monkeys.append(self)

        self.items = starting_items
        self.operation = operation.split("=")[1].strip()
        self.test = int(test.split(" ")[-1])
        self.true = if_true
        self.false = if_false

        self.inspected = 0
        self.memory: typing.Dict[int, list[int]] = {}

    def throw(self, item, other_monkey):
        other_monkey.items.append(item)

    def assess(self):
        for item in self.items:
            if item in self.memory:
                self.throw(
                    self.memory[item][0], Monkey.all_monkeys[self.memory[item][1]]
                )
            else:
                old = item
                new_item = eval(self.operation)
                output = new_item // 3

                if output % self.test == 0:
                    print(
                        f"Monkey {self.monkey_number} throws item {output} to monkey {self.true}",
                    )
                    self.throw(output, Monkey.all_monkeys[self.true])
                    self.memory[item] = [output, self.true]
                else:
                    print(
                        f"Monkey {self.monkey_number} throws item {output} to monkey {self.false}",
                    )
                    self.throw(output, Monkey.all_monkeys[self.false])
                    self.memory[item] = [output, self.false]

            self.inspected += 1

        self.items = []


with open("input") as fp:
    while True:
        line = fp.readline()
        if not line:
            break

        if line.startswith("Monkey"):
            items = [
                int(item) for item in fp.readline().strip().split(":")[1].split(", ")
            ]
            operation = fp.readline().strip().split(":")[1]
            test = fp.readline().strip().split(":")[1]
            if_true = int(fp.readline().strip().split(":")[1].split(" ")[-1])
            if_false = int(fp.readline().strip().split(":")[1].split(" ")[-1])

            Monkey(items, operation, test, if_true, if_false)

NUMBER_OF_ROUNDS = 20

for round in range(NUMBER_OF_ROUNDS):
    for monkey in Monkey.all_monkeys:
        monkey.assess()

    print(round + 1, [monkey.items for monkey in Monkey.all_monkeys])

monkey_business_ordered = sorted(
    [monkey.inspected for monkey in Monkey.all_monkeys], reverse=True
)

print(monkey_business_ordered)

print(monkey_business_ordered[0] * monkey_business_ordered[1])
