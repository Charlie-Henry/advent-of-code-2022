import math


class monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.worry_operation = operation
        self.worry_test = test
        self.test_t = None
        self.test_f = None
        self.count_inspections = 0

    def monkey_round(self):
        if self.items:
            item = self.items.pop(0)
            self.count_inspections += 1
            item = self.worry_operation(item)
            item = math.floor(item / 3)  # Monkey gets bored with item.
            if item % self.worry_test == 0:
                self.throw_item(self.test_t, item)
            else:
                self.throw_item(self.test_f, item)

            self.monkey_round()

    def throw_item(self, dest_monkey, item):
        dest_monkey.items.append(item)


def test():
    ## Test cases
    monkey_0 = monkey([79, 98], lambda x: x * 19, 23)
    monkey_1 = monkey([54, 65, 75, 74], lambda x: x + 6, 19)
    monkey_2 = monkey([79, 60, 97], lambda x: x * x, 13)
    monkey_3 = monkey([74], lambda x: x + 3, 17)

    monkey_0.test_t = monkey_2
    monkey_0.test_f = monkey_3

    monkey_1.test_t = monkey_2
    monkey_1.test_f = monkey_0

    monkey_2.test_t = monkey_1
    monkey_2.test_f = monkey_3

    monkey_3.test_t = monkey_0
    monkey_3.test_f = monkey_1

    monkeys = [monkey_0, monkey_1, monkey_2, monkey_3]

    for k in range(20):  # 20 monkey rounds
        for i in monkeys:
            i.monkey_round()

    business = []
    for i in monkeys:
        business.append(i.count_inspections)
    business.sort(reverse=True)
    print(business[0] * business[1])


def main():
    ## Given cases
    monkey_0 = monkey([54, 53], lambda x: x * 3, 2)
    monkey_1 = monkey([95, 88, 75, 81, 91, 67, 65, 84], lambda x: x * 11, 7)
    monkey_2 = monkey([76, 81, 50, 93, 96, 81, 83], lambda x: x + 6, 3)
    monkey_3 = monkey([83, 85, 85, 63], lambda x: x + 4, 11)
    monkey_4 = monkey([85, 52, 64], lambda x: x + 8, 17)
    monkey_5 = monkey([57], lambda x: x + 2, 5)
    monkey_6 = monkey([60, 95, 76, 66, 91], lambda x: x * x, 13)
    monkey_7 = monkey([65, 84, 76, 72, 79, 65], lambda x: x + 5, 19)

    monkey_0.test_t = monkey_2
    monkey_0.test_f = monkey_6

    monkey_1.test_t = monkey_3
    monkey_1.test_f = monkey_4

    monkey_2.test_t = monkey_5
    monkey_2.test_f = monkey_1

    monkey_3.test_t = monkey_7
    monkey_3.test_f = monkey_4

    monkey_4.test_t = monkey_0
    monkey_4.test_f = monkey_7

    monkey_5.test_t = monkey_1
    monkey_5.test_f = monkey_3

    monkey_6.test_t = monkey_2
    monkey_6.test_f = monkey_5

    monkey_7.test_t = monkey_6
    monkey_7.test_f = monkey_0

    monkeys = [
        monkey_0,
        monkey_1,
        monkey_2,
        monkey_3,
        monkey_4,
        monkey_5,
        monkey_6,
        monkey_7,
    ]

    for k in range(20):  # 20 monkey rounds
        for i in monkeys:
            i.monkey_round()

    business = []
    for i in monkeys:
        business.append(i.count_inspections)
    business.sort(reverse=True)
    print(business[0] * business[1])


main()
