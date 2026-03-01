import math
import sys


def get_lcm(first_number: int, second_number: int) -> int:
    answer = first_number * second_number
    while first_number * second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return answer // (first_number + second_number)


def calc(*args: int, **kwargs: int | float) -> int | float:
    current_lcm = 1
    for new_number in args:
        current_lcm = get_lcm(current_lcm, new_number)
    if "log" in kwargs:
        log_base = kwargs["log"]
        return math.log(current_lcm, log_base)
    return current_lcm


def main() -> None:
    exec(sys.stdin.read())


if __name__ == "__main__":
    main()
