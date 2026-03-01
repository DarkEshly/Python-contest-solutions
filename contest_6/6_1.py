import sys
from typing import Literal

BooleanVector = list[Literal[0, 1]]


class BooleanFunction:
    def __init__(self, truth_table: BooleanVector):
        table_len = len(truth_table)
        if not ((table_len & (table_len - 1) == 0) and table_len != 0):
            raise ValueError("Truth table length is not a power of two")
        self.truth_table = truth_table.copy()
        self.function_length = 0
        while (1 << self.function_length) != table_len:
            self.function_length += 1

    def __str__(self) -> str:
        variables = ", ".join(f"x{i + 1}" for i in range(self.function_length))
        values = ", ".join(map(str, self.truth_table))
        return f"f({variables}) = ({values})"

    def __call__(self, values: BooleanVector) -> Literal[0, 1]:
        if len(values) != self.function_length:
            raise ValueError("Arity mismatch")
        return self.truth_table[int("".join(map(str, values)), 2)]

    def __add__(self, other: "BooleanFunction") -> "BooleanFunction":
        if self.function_length != other.function_length:
            raise ValueError("Arity mismatch")
        new_table: BooleanVector = []
        for a, b in zip(self.truth_table, other.truth_table):
            if a ^ b:
                new_table.append(1)
            else:
                new_table.append(0)
        return BooleanFunction(new_table)

    def __mul__(self, other: "BooleanFunction") -> "BooleanFunction":
        if self.function_length != other.function_length:
            raise ValueError("Arity mismatch")
        new_table: BooleanVector = []
        for a, b in zip(self.truth_table, other.truth_table):
            if a & b:
                new_table.append(1)
            else:
                new_table.append(0)
        return BooleanFunction(new_table)


def main():
    exec(sys.stdin.read())


if __name__ == "__main__":
    main()
