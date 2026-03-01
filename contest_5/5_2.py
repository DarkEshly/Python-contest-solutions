import sys
from abc import ABC, abstractmethod


class NormalForm(ABC):
    def __init__(self) -> None:
        self.clauses: list[list[int]] = []

    def add_clause(self, clause: list[int]) -> None:
        for element in clause:
            if element == 0:
                raise ValueError("Variable number is 0")
        self.clauses.append(clause)

    @staticmethod
    def check_values(values: dict[int, int]) -> None:
        for key, value in values.items():
            if key < 1:
                raise ValueError("Key is less than 1")
            if value not in [0, 1]:
                raise ValueError("Value should be 0 or 1")

    @abstractmethod
    def __call__(self, values: dict[int, int]) -> int:
        pass


class DNF(NormalForm):
    def __init__(self):
        super().__init__()

    def __call__(self, values: dict[int, int]) -> int:
        self.check_values(values)
        for clause in self.clauses:
            result = 1
            for var in clause:
                var_num = abs(var)
                if var_num not in values:
                    raise ValueError(f"Variable {var_num} is not found")
                literal_value = values[var_num] if var > 0 else 1 - values[var_num]
                result &= literal_value
                if result == 0:
                    break
            if result == 1:
                return 1
        return 0


class CNF(NormalForm):
    def __init__(self):
        super().__init__()

    def __call__(self, values: dict[int, int]) -> int:
        self.check_values(values)
        for clause in self.clauses:
            result = 0
            for var in clause:
                var_num = abs(var)
                if var_num not in values:
                    raise ValueError(f"Variable {var_num} is not found")
                literal_value = values[var_num] if var > 0 else 1 - values[var_num]
                result |= literal_value
                if result == 1:
                    break
            if result == 0:
                return 0
        return 1


def main():
    exec(sys.stdin.read())


if __name__ == "__main__":
    main()
