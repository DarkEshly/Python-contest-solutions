import sys


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main() -> None:
    for line in sys.stdin:
        number = int(line)
        if is_prime(int(line)):
            print(f"{number} is prime")
        else:
            print(f"{number} is not prime")


if __name__ == "__main__":
    main()
