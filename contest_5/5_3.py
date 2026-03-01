from enum import Enum


class Cell(Enum):
    UNKNOWN = "."
    EMPTY = "X"
    TREASURE = "$"

    def __str__(self):
        return self.value


class Model:
    def __init__(self):
        self.map: list[list[Cell]] = []
        self.treasures: set[tuple[int, int]] = set()

    def initialize(self, n: int, m: int):
        self.map = [[Cell.UNKNOWN for _ in range(m)] for _ in range(n)]

    def add_treasure(self, x: int, y: int):
        self.treasures.add((x, y))

    def examine(self, x: int, y: int):
        if (x, y) in self.treasures:
            self.map[x][y] = Cell.TREASURE
        else:
            self.map[x][y] = Cell.EMPTY


class View:
    @staticmethod
    def print(map: list[list[Cell]]):
        for row in map:
            print("".join(str(cell) for cell in row))
        print("")


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def read_map(self):
        n, m = map(int, input().split())
        self.model.initialize(n, m)
        t = int(input())
        for _ in range(t):
            x, y = map(int, input().split())
            self.model.add_treasure(x, y)

    def do_examinations(self):
        e = int(input())
        for _ in range(e):
            x, y = map(int, input().split())
            self.model.examine(x, y)
            self.view.print(self.model.map)


def main():
    controller = Controller()
    controller.read_map()
    controller.do_examinations()


if __name__ == "__main__":
    main()
