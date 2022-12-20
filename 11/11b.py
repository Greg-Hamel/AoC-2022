import typing
import os
from pprint import pprint


class Item:
    all_items = []

    def __init__(self, value, first_monkey):
        self.index = len(Item.all_items)
        self.initial_value = value
        self.initial_monkey = first_monkey

        Item.all_items.append(self)

        self.value = value
        self.steady = False
        self.steady_state_counter = 0

    def set_value(self, value, next_monkey):
        self.value = value


class Monkey:
    all_monkeys = []
    highest_possible_value = 1

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

        # self.items: list[Item] = []
        self.items: list[int] = []

        for item in starting_items:
            # self.items.append(Item(item, self.monkey_number))
            self.items.append(item)

        self.operation = operation.split("=")[1].strip()
        self.test = int(test.split(" ")[-1])
        self.true = if_true
        self.false = if_false

        self.inspected = 0
        self.memory: typing.Dict[int, list[int]] = {}
        Monkey.highest_possible_value *= self.test

    def throw(self, item, other_monkey):
        other_monkey.items.append(item)

    def assess(self):
        for item in self.items:
            old = item
            output = eval(self.operation)

            if output > Monkey.highest_possible_value:
                output = output % Monkey.highest_possible_value

            if output % self.test == 0:
                Monkey.all_monkeys[self.true].items.append(output)
            else:
                Monkey.all_monkeys[self.false].items.append(output)

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

NUMBER_OF_ROUNDS = 10000

print("highest_possible_value", Monkey.highest_possible_value)

for round in range(NUMBER_OF_ROUNDS):
    for monkey in Monkey.all_monkeys:
        monkey.assess()

    if round % 100 == 0:
        # print(round + 1, [monkey.items for monkey in Monkey.all_monkeys])
        print(round)

monkey_business = [monkey.inspected for monkey in Monkey.all_monkeys]

monkey_business_ordered = sorted(monkey_business, reverse=True)

print(monkey_business)
print(monkey_business_ordered)

print(monkey_business_ordered[0] * monkey_business_ordered[1])
