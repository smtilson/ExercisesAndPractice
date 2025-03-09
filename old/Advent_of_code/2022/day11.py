test_input="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

real_input = """Monkey 0:
  Starting items: 99, 67, 92, 61, 83, 64, 98
  Operation: new = old * 17
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 2

Monkey 1:
  Starting items: 78, 74, 88, 89, 50
  Operation: new = old * 11
  Test: divisible by 5
    If true: throw to monkey 3
    If false: throw to monkey 5

Monkey 2:
  Starting items: 98, 91
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 3:
  Starting items: 59, 72, 94, 91, 79, 88, 94, 51
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 0
    If false: throw to monkey 5

Monkey 4:
  Starting items: 95, 72, 78
  Operation: new = old + 7
  Test: divisible by 11
    If true: throw to monkey 7
    If false: throw to monkey 6

Monkey 5:
  Starting items: 76
  Operation: new = old + 8
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 2

Monkey 6:
  Starting items: 69, 60, 53, 89, 71, 88
  Operation: new = old + 5
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 1

Monkey 7:
  Starting items: 72, 54, 63, 80
  Operation: new = old + 3
  Test: divisible by 7
    If true: throw to monkey 1
    If false: throw to monkey 3"""

from typing import List,Tuple, Union, Optional
import re

#part 2 uses the relief function.
def part1(raw_data:str)->None:
    monkeys = process_data(raw_data)
    for _ in range(10000):
        monkeys = do_round(monkeys)
        #print(f"round {_}^")
    for monkey in monkeys:
        print(monkey.count)
    level = monkey_business_level(monkeys)
    print(level)

def process_data(raw_data:str)->List["Monkey"]:
    list_of_monkeys = raw_data.split("\n\n")
    monkeys = []
    for monkey in list_of_monkeys:
        new_monkey = Monkey(monkey)
        monkeys.append(new_monkey)
        print(new_monkey.name)
        print(new_monkey.items)
    return monkeys

def relief(item:int)->int:
    num = 3*5*2*13*11*17*19*7
    num_test=23*19*13*17
    return item % num


class Monkey:
    monkeys = []
    def __init__(self,raw:str)->None:
        lines = raw.split("\n")
        self.name = self.find_name(lines[0])
        self.items = self.find_items(lines[1])
        self.opval = self.find_op(lines[2])
        self.testval = self.find_test(lines[3])
        self.true = self.find_throw(lines[4])
        self.false = self.find_throw(lines[5])
        self.count = 0
        self.monkeys.append(self)

    @staticmethod
    def find_name(line:str) -> int:
        name = line.split("onkey ")[1]
        name = name.strip(":")
        return int(name)

    @staticmethod
    def find_items(line: str) -> List[int]:
        items = line.split("items: ")[1]
        items = items.split(", ")
        return [int(n) for n in items]

    @staticmethod
    def find_op(line:str) -> str:
        return line.split("=")[1].strip()

    @staticmethod
    def find_test(line:str) -> int:
        value = line.split(" by ")[1]
        return int(value)

    @staticmethod
    def find_throw(line: str):
        name = line.split(" monkey ")[1]
        return int(name)

    def op(self, old:int) -> int:
        return eval(self.opval)

    def test(self, value: int)->bool:
        return value % self.testval == 0

    def target(self, result:bool) -> int:
        if result:
            return self.true
        else:
            return self.false

    @classmethod
    def find_monkey(cls, name)->"Monkey":
        for monkey in cls.monkeys:
            if monkey.name == name:
                return monkey
        raise ValueError("No such monkey exists.")

    def process_item(self, item:int)->None:
        #print(f"worry:{item}")
        worry = self.op(item)
        #print(f'{worry=}')
        worry = relief(worry)
        #print(f'{worry=}')
        target = self.target(self.test(worry))
        #print(f'{target=}')
        monkey = self.find_monkey(target)
        self.items.remove(item)
        #print(self.items)
        monkey.items.append(worry)
        #print(monkey.items)
        self.count +=1
        #kill()

    def process_all(self)->None:
        #print("process all")
        #kill()
        #print(f"{self.name} processing {self.items}.")
        while self.items:
            #print(f'current {self.items[0]}.')
            self.process_item(self.items[0])

    def process_one(self) -> None:
        print("process one")
        kill()
        print(f"{self.name} processing {self.items}.")
        item = self.items[0]
        print(f'current {item}.')
        self.process_item(item)


def kill():
    dead = input()
    if dead:
        raise KeyboardInterrupt


def do_round(monkeys:List[Monkey])->List[Monkey]:
    for monkey in monkeys:
        monkey.process_all()
    #for monkey in monkeys:
        #print(monkey.items)
    return monkeys

def monkey_business_level(monkeys) -> int:
    activity = [monkey.count for monkey in monkeys]
    activity.sort()
    return activity[-1]*activity[-2]

if __name__ == "__main__":
    part1(real_input)


