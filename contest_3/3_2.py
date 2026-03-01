from typing import Generator


def get_binary(length: int) -> Generator[list[int], None, None]:
    if length == 0:
        yield []
    else:
        for last_comp in get_binary(length - 1):
            yield last_comp + [0]
            yield last_comp + [1]


def main() -> None:
    n = int(input())
    for sequence in get_binary(n):
        if n == 1:
            print(str(tuple(sequence)).replace(",", ""))
        else:
            print(tuple(sequence))


if __name__ == "__main__":
    main()
