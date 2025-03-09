from __future__ import annotations
small_test_input = """noop
addx 3
addx -5"""

large_test_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

full_input = """addx 2
addx 3
noop
addx 1
addx 27
addx -23
addx 5
noop
addx 1
noop
addx 4
addx 1
noop
addx 4
addx 5
noop
noop
noop
addx 5
addx -4
addx 4
noop
addx 1
addx -38
noop
noop
addx 7
addx 8
addx -3
noop
addx 3
noop
addx 5
noop
noop
addx -2
addx 2
addx 9
addx -2
addx 6
addx 1
addx -4
addx 5
addx 2
addx -14
addx -6
addx -16
addx 1
addx 5
addx 1
addx 4
addx -2
noop
addx -7
addx -3
addx 17
addx 5
noop
noop
addx 19
addx -16
noop
addx 14
addx -8
addx 2
noop
addx 4
noop
addx -35
addx -2
noop
noop
addx 7
addx 19
addx -26
addx 10
addx 29
addx -21
noop
addx 4
noop
noop
addx -9
addx 4
addx 8
addx 7
noop
addx -2
addx 5
addx 2
addx -19
addx -18
noop
noop
noop
noop
addx 7
addx -7
addx 37
addx -27
addx 5
addx 2
addx -12
addx 4
addx 11
noop
noop
noop
addx 5
addx -14
addx 21
addx -4
addx 5
addx 2
noop
addx -35
noop
noop
noop
noop
addx 7
addx 1
noop
noop
addx 5
addx -1
addx 5
addx 1
noop
addx 4
addx 1
noop
noop
addx 4
noop
addx 1
addx 2
addx 5
addx 2
addx 1
noop
noop
noop
noop"""

from typing import List, Tuple, Union


def part1(raw_data: str) -> None:
    processor = CPU()
    instructions = process_raw(raw_data)
    for instruction in instructions:
        processor.do(instruction)
    total = find_interesting(processor)
    print(total)


def part2(raw_data:str) -> None:
    instructions = process_raw(raw_data)
    cpu = CPU()
    for instruction in instructions:
        cpu.do(instruction)
    current = CRT(processor_history=cpu.history)
    current.render()

from typing import Dict, Hashable, Any, Mapping, Iterable
class NoDupDict1(Dict[Hashable, Any]):
    def __setitem__(self, key, value) -> None:
        if key in self:
            raise ValueError(f"duplicate {key!r}")
        super().__setitem__(key, value)


from typing import cast, Union, Tuple
from collections import Hashable
DictInit = Union[
    Iterable[Tuple[Hashable, Any]],
    Mapping[Hashable, Any],
    None]
class NoDupDict2(Dict[Hashable, Any]):

    def __init__(self, init: DictInit = None, **kwargs: Any) -> None:
        print(init.__class__.__name__)
        print(init)
        if isinstance(init, Mapping):
            super().__init__(init, **kwargs)
        elif isinstance(init, Iterable):
            for k, v in cast(Iterable[Tuple[Hashable, Any]], init):
                self[k] = v
        elif init is None:
            super().__init__(**kwargs)
        else:
            super().__init__(init, **kwargs)
    def __setitem__(self, key: Hashable, value: Any) -> None:
        if key in self:
            raise ValueError(f"duplicate {key!r}")
        super().__setitem__(key, value)

def process_raw(raw_data: str) -> List[str]:
    data = raw_data.split("\n")
    return data


def find_interesting(processor: "CPU") -> int:
    interesting_signals = [20,60,100,140,180,220]
    total = 0
    for cycle in interesting_signals:
        total += processor.compute_signal_strength(cycle)
    return total


class CRT():
    def __init__(self, processor_history) -> None:
        self.screen =[["." for _ in range(40)] for _ in range(6)]
        self.processor_history = processor_history

    def render(self):
        for cycle, sprite_position in enumerate(self.processor_history):
            position = self.draw_position(cycle)
            sprite = self.sprite(sprite_position)
            self.draw(sprite=sprite, position=position)
        self.display()

    def draw_position(self, cycle):
        try:
            x = cycle % 40
            y = cycle // 40
        except ValueError as e:
            raise e(f"Wrong value for {cycle=}")
        return x, y

    def draw(self, sprite, position):
        if position[0] in sprite:
            self.screen[position[1]][position[0]] = "#"

    def display(self) -> None:
        for row in self.screen:
            print(" ".join(row))

    def sprite(self, position) -> None:
        x1 = position - 1
        x2 = position
        x3 = position + 1
        #if x1 or x2 or x3 not in range(40):
         #   raise ValueError("Invalid sprite position.")
        return (x1, x2, x3)



class CPU():
    def __init__(self):
        self.xreg = 1
        self.history = [1]
        self.cycle = 1

    def noop(self):
        self.history.append(self.xreg)
        self.cycle += 1

    def addx(self, value):
        try:
            value = int(value)
        except TypeError or ValueError as e:
            print("Invalid value:", value)
            raise e
        self.noop()
        self.xreg += value
        self.noop()

    def check_xreg(self, cycle) -> int:
        return self.history[cycle-1]

    def do(self, instruction) -> None:
        if instruction[:4] == "noop":
            self.noop()
        else:
            value = instruction.split(" ")[1]
            self.addx(value)

    def compute_signal_strength(self,cycle):
        if len(self.history) < cycle:
            raise ValueError("We haven't yet reached that cycle.")
        value = self.history[cycle-1]
        return value*cycle



if __name__ == "__main__":
    part2(full_input)