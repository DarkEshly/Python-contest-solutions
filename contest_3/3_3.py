import sys
from typing import Generator


def generate_string() -> Generator[str, str, None]:
    current_string = ""
    count = 1
    while True:
        new_string = yield current_string
        current_string = new_string * count
        count += 1


def main() -> None:
    current_generator = generate_string()
    next(current_generator)
    for line in sys.stdin:
        print(current_generator.send(line.rstrip()))


if __name__ == "__main__":
    main()
