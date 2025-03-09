from typing import List, Tuple, Union, NamedTuple
from copy import deepcopy

real_input="""abccccccccaaaaaaaccaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccaaaaaa
abccccccccaaaaaaaccaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccaaaaaa
abccccccccccaaaaaaccaaaaaaaaaaaaaaaaccccccccccccccccacccccccccccccccccccaaaaa
abcccccaaaacaaaaaaccaaaaaaaaaaaaaaaaacccccccccccccccaaaccccaccccccccccccccaaa
abccccaaaaacaaccccccaaaaaacaaacaacaaaaaaacccccccccccaaaacccaacccccccccccccaaa
abaaccaaaaaaccccaaacaaaacacaaacaaccaaaaaacccccccccccaklaccccccccccccccccccaac
abaaccaaaaaaccaaaaaacccccccaaacccaaaaaaaccccccccccckkkllllccccccccccccccccccc
abaaccaaaaaaccaaaaaacccccccaaaaacaaaaaaacccccccccckkkklllllcccccccaaaccaccccc
abacccccaacccccaaaaacccccccaaaaaccaaaaaaacccccccckkkkpppllllccccccaaaaaaccccc
abacccccccccccaaaaacccccccccaaaacccaaaaaaccccccckkkkpppppplllccccddddaaaccccc
abccccccccccccaaaaaccccccccccaaaccaaaccccccccccckkkppppppppllllldddddddaccccc
abccacccccccccccccccccccccccccccccaaccccccccccckkkopppupppplllmmmmdddddaacccc
abccaaacaaaccccccccccccccccccccaaaaaaaaccccccckkkkopuuuuupppllmmmmmmddddacccc
abccaaaaaaaccccccccccccccccccccaaaaaaaacccccjjkkkooouuuuuuppqqqqqmmmmddddcccc
abccaaaaaacccccccccccccccaaccccccaaaacccccjjjjjjoooouuxuuuppqqqqqqmmmmdddcccc
abcaaaaaaaacccccccccccccaaacccccaaaaaccccjjjjoooooouuuxxuuvvvvvqqqqmmmdddcccc
abaaaaaaaaaacccccccaaaaaaacaacccaacaaacccjjjooooouuuuxxxxvvvvvvvqqqmmmdddcccc
abaaaaaaaaaacccaaacaaaaaaaaaacccacccaaccjjjooootttuuuxxxyyvyyvvvqqqmmmeeecccc
abcccaaacaaacccaaaaaaacaaaaaccccccccccccjjjooottttxxxxxxyyyyyyvvqqqmmmeeccccc
abcccaaacccccccaaaaaacaaaaaccccaaccaacccjjjnnntttxxxxxxxyyyyyvvvqqqnneeeccccc
SbccccaacccccccaaaaaaaaacaaacccaaaaaacccjjjnnntttxxxEzzzzyyyyvvqqqnnneeeccccc
abcccccccccccccaaaaaaaaacaaccccaaaaaccccjjjnnnttttxxxxyyyyyvvvrrrnnneeecccccc
abcccaacccccccaaaaaaaaaccccccccaaaaaacccciiinnnttttxxxyyyyywvvrrrnnneeecccccc
abcccaaaaaaccaaaaaaaacccccccccaaaaaaaaccciiiinnnttttxyyywyyywvrrrnnneeecccccc
abcccaaaaaaccaaaaaaaacccccccccaaaaaaaacccciiinnnntttxwywwyyywwwrrnnneeecccccc
abcaaaaaaaccaaaaaaaaaccccccccccccaacccccccciiinnnttwwwwwwwwwwwwrrnnneeecccccc
abcaaaaaaaccaaaaaacccccccccccccccaaccccccaaiiiinnttwwwwwwwwwwwrrrnnnffecccccc
abcccaaaaaaccaaaaaccccccccccccccccccccaaaaaciiinnssswwwssssrwwrrrnnnfffcccccc
abaacaaccaaccaaaccccccccaacccccccccccccaaaaaiiinnssssssssssrrrrrronnfffcccccc
abaccaaccaacccccccccaaacaacccccccccccccaaaaaiiimmmssssssmoosrrrrooonffaaacccc
abaaaccccaaaaaaccccccaaaaaccccccccccccaaaaaccihmmmmsssmmmoooooooooofffaaacccc
abaaaccccaaaaaacccccccaaaaaacccccccccccccaacchhhmmmmmmmmmoooooooooffffaaccccc
abaacccaaaaaaaccccccaaaaaaaaccccaaccccccccccchhhhmmmmmmmgggggooofffffaaaccccc
abaacccaaaaaaaccccccaaaaaaaccccaaaaccccccccccchhhhmmmmhggggggggfffffaaaaccccc
abccccccaaaaaaacccccaacaaaaacccaaaaccccccccccchhhhhhhhggggggggggfffaacaaccccc
abccaacccaaaaaaccccccccaaaaaccaaaaacccccccccccchhhhhhhggaaaaaaccccccccccccccc
abccaaaccaaccccccccccccccaaaaaaaaaccccccccccccccchhhhaaaccaaaacccccccccccccaa
abaaaaaaaccccccccccccccccaaaaaaaaccccccccccccccccccccaaaccccaaccccccccccccaaa
abaaaaaaaccccccccaaaccccacaaaaaacccccccccccccccccccccaaaccccccccccccccccccaaa
abaaaaaacccccccaaaaacaaaaaaaaaaacccccccccccccccccccccaaccccccccccccccccaaaaaa
abaaaaaacccccccaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccccccccaaaaaa"""

test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def part1(raw_data:str)->None:
    grid = create_grid(raw_data)
    Solution_space = Paths(grid)
    while not Solution_space.finished_paths:
        Solution_space.grow()
        Solution_space.prune()
        #Solution_space.report()
    print(Solution_space.lengths())


def part1_tails(raw_data:str)->None:
    grid = create_grid(raw_data)
    solution_space = Tail_Sols(grid)
    counter = 0
    while not solution_space.finished_tails:
        if counter == 100:
            solution_space.report()
            counter = 0
        solution_space.grow()
        solution_space.prune()
        #Solution_space.report()
        counter += 1
        #print(solution_space.time)
    print(solution_space.time)


def create_order()->dict:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    order = {letter: alpha.find(letter) for letter in alpha}
    order['S'] = 'S'
    order['E'] = order['z']+1
    return order


def create_grid(raw_data:str)->List[List[str]]:
    grid = raw_data.split('\n')
    #grid = [list(row) for row in rows]
    return grid


def find_range(grid) -> Tuple[int,int]:
    return len(grid[0])-1, len(grid)-1


class Paths:
    def __init__(self, grid:List[List[str]]) -> None:
        self.grid = grid
        self.start = self.find_S()
        self.paths = {Path(grid, self.start)}
        self.finished_paths = set()
        self.dead_paths = set()
        self.rules = create_order()
        self.previous = set()

    def find_S(self) -> Tuple[int, int]:
        for y, row in enumerate(self.grid):
            for x, letter in enumerate(row):
                if letter == 'S':
                    return x, y

    def grow(self) -> None:
        new_paths = set()
        for path in self.paths:
            self.previous.add((path.x, path.y))
            if path.check_finished():
                continue
            neighbors = path.neighbors()
            if not neighbors:
                continue
            for index, neighbor in enumerate(neighbors):
                new = deepcopy(path)
                if new.move(neighbor):
                    if (new.x, new.y) in self.previous:
                        continue
                    new_paths.add(new)
        #print([path.path for path in new_paths])
        #print([path.path for path in self.paths])
        self.paths = new_paths
        #print([path.path for path in self.paths])

    def report(self):
        print("dead paths:")
        for p in self.dead_paths:
            print(p.path)
        print("active paths")
        for p in self.paths:
            print(p.path)
            print(p.val)
        input()

    def prune(self) -> None:
        paths = deepcopy(self.paths)
        for path in paths:
            if path.check_finished():
                self.finished_paths.add(path)
                self.paths.discard(path)
            elif path.dead:
                self.dead_paths.add(path)
                self.paths.discard(path)
                # input(f"{path} is dead.")
            elif (path.x, path.y) in self.previous:
                self.paths.discard(path)
        self.merge()

    def merge(self):
        paths = deepcopy(self.paths)
        for path1 in paths:
            for path2 in paths:
                if len(path1) == len(path2) and path1.current == path2.current:
                    self.paths.discard(path2)

    def lengths(self)-> List[int]:
        lengths = [len(path.path)-1 for path in self.finished_paths]
        lengths.sort()
        return lengths


class Tail_Sols:
    def __init__(self, grid:List[List[str]]) -> None:
        self.grid = grid
        self.rules = create_order()
        self.start = self.find_S()
        self.tails = self.find_a()
        self.finished_tails = set()
        self.dead_tails = set()
        self.previous = set()
        self.rules = create_order()
        self.time = 0
        self.range = find_range(grid)

    def find_S(self) -> Tuple[int, int]:
        for y, row in enumerate(self.grid):
            for x, letter in enumerate(row):
                if letter == 'S':
                    return x, y

    def find_a(self):
        all_a = set()
        for y, row in enumerate(self.grid):
            #print(row)
            for x, letter in enumerate(row):
                #print(letter)
                if letter == 'a':
                    #print(f"adding ({x, y})")
                    all_a.add((x,y))
        return all_a

    def grow(self) -> None:
        new_tails = set()
        for point in self.tails:
            tail = Tail(x=point[0], y=point[1], val=self.grid[point[1]][point[0]],
                        range=self.range)
            self.previous.add(point)
            if tail.check_finished():
                continue
            neighbors = tail.neighbors()
            if not neighbors:
                continue
            for index, neighbor in enumerate(neighbors):
                new = tail.move(neighbor, grid=self.grid, rules=self.rules)
                if new in self.previous:
                    continue
                elif new:
                    new_tails.add((new.x, new.y))
        #print([path.path for path in new_paths])
        #print([path.path for path in self.paths])
        self.tails = new_tails
        #print([path.path for path in self.paths])
        self.time += 1

    def report(self):
        print("dead paths:")
        print(self.dead_tails)
        print("active paths")
        print(self.tails)
        input()

    def prune(self) -> None:
        tails = deepcopy(self.tails)
        for point in tails:
            tail = Tail(x=point[0], y=point[1], val=self.grid[point[1]][point[0]],
                        range=self.range)
            if tail.check_finished():
                self.finished_tails.add(point)
                self.tails.discard(point)
            elif tail.dead(self.grid, self.rules):
                self.dead_tails.add(point)
                self.tails.discard(point)
                # input(f"{path} is dead.")
            elif point in self.previous:
                self.tails.discard(point)


class Tail(NamedTuple):
        x: int
        y: int
        val: str
        range: Tuple[int,int]

        def neighbors(self):
            neighbors = []
            basic = {(1, 0), (0, 1), (-1, 0), (0, -1)}
            for direction in basic:
                #print(f"{self.x=},{self.y=}, {direction=}")
                new = (self.x + direction[0], self.y + direction[1])
                #print(new)
                if new[0] < 0 or new[1] < 0:
                    continue
                elif new[0] > self.range[0] or new[1] > self.range[1]:
                    continue
                    #print(f"checking {new=}")
                else:
                    neighbors.append(new)
                    #print("appending ", new)
            return neighbors

        def compare(self, b, grid, rules) -> bool:
            val_b = grid[b[1]][b[0]]
            # print(f"comparing {self.current}:{self.val} and {b}:{val_b}")
            # input()
            if self.val == "S":
                if rules[val_b] <= 1:
                    # print(f"moving from {self.current}:{self.val} to {b}:{val_b}.")
                    return True
                else:
                    return False
            elif val_b == "S":
                return False
            elif rules[val_b] > rules[self.val] + 1:
                return False
            """try:
                return self.rules[self.val] >= self.rules[val_b]
            except TypeError:
            print(f"{self.val=},{val_b=}")
            print(f"{self.rules[self.val]=},{self.rules[val_b]=}")
            input()"""
            # print(f"moving from {self.current}:{self.val} to {b}:{val_b}.")
            return True

        def move(self, neighbor, grid, rules) -> bool:
            if self.compare(neighbor, grid, rules):
                new = Tail(x=neighbor[0],y=neighbor[1], val=grid[neighbor[1]][neighbor[0]],
                            range=self.range)
                return new
            return None

        def check_finished(self) -> bool:
            if self.val == 'E':
                return True
            return False

        def dead(self, grid, rules):
            # print("checking for death.")
            for neighbor in self.neighbors():
                if self.compare(neighbor, grid, rules):
                    return False
            return True


class Path:
    def __init__(self,grid,start, path: List[str] = None):
        self.grid = grid
        self.rules = create_order()
        if path is None:
            path = [start]
        self.path = path
        if path is None:
            current = start
        else:
            current = path[-1]
        self.current = current

    @property
    def val(self):
        return self.grid[self.current[1]][self.current[0]]

    @property
    def x(self):
        return self.current[0]

    @property
    def y(self):
        return self.current[1]

    def neighbors(self):
        neighbors = []
        basic = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        for direction in basic:
            #print(f"{self.x=},{self.y=}, {direction=}")
            new = (self.x+direction[0], self.y+direction[1])
            if new in self.path:
                continue
            #print(new)
            elif new[0] < 0 or new[1] < 0:
                continue
            try:
                #print(f"checking {new=}")
                self.grid[new[1]][new[0]]
            except IndexError:
                #print(f"{new=} failed to be in the grid")
                continue
            else:
                neighbors.append(new)
                # print("appending ", new)
        return neighbors

    def compare(self, b: str) -> bool:
        val_b = self.grid[b[1]][b[0]]
        #print(f"comparing {self.current}:{self.val} and {b}:{val_b}")
        #input()
        if b in self.path:
            return False
        if self.val == "S":
            if self.rules[val_b] <= 1:
                #print(f"moving from {self.current}:{self.val} to {b}:{val_b}.")
                return True
            else:
                return False
        elif val_b == "S":
            return False
        elif self.rules[val_b] > self.rules[self.val]+1:
            return False
        """try:
            return self.rules[self.val] >= self.rules[val_b]
        except TypeError:
        print(f"{self.val=},{val_b=}")
        print(f"{self.rules[self.val]=},{self.rules[val_b]=}")
        input()"""
        #print(f"moving from {self.current}:{self.val} to {b}:{val_b}.")
        return True

    def move(self, neighbor) -> bool:
        if self.compare(neighbor):
            self.path.append(neighbor)
            self.current = neighbor
            return True
        return False

    def copy(self):
        return Path(self.grid, self.path[0], self.path)

    def check_finished(self) -> bool:
        if self.val == 'E':
            return True
        return False

    @property
    def dead(self):
        #print("checking for death.")
        if len(self.path) != len(set(self.path)):
            return True
        for neighbor in self.neighbors():
            if self.compare(neighbor):
                return False
        return True

    def __len__(self):
        return len(self.path)-1

if __name__ == '__main__':
    part1_tails(test_input)