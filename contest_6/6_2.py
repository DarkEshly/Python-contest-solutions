import sys
from typing import Iterator


class CovidSimulator:
    def __init__(self, days: int, step: float) -> None:
        self.days = days
        self.step = round(step, 1)
        self.tempt = 36.6
        self.current_day = 1

    def __iter__(self) -> Iterator[float]:
        old_tempt = self.tempt
        for i in range(self.days):
            yield old_tempt
            self.tempt += (
                self.step * [1, -1][i >= self.days // 2] * (not (self.days % 2 == 0 and i == self.days // 2 - 1))
            )
            if round(self.tempt, 1) <= 40:
                old_tempt = self.tempt
            self.current_day += 1


def main():
    exec(sys.stdin.read())


if __name__ == "__main__":
    main()
