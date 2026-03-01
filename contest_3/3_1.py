import sys
from functools import lru_cache

RECURSION_LIMIT = 5000

sys.setrecursionlimit(RECURSION_LIMIT)


@lru_cache(maxsize=None)
def get_binomial_coefficients(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1
    elif k > n or k < 0:
        return 0
    return get_binomial_coefficients(n - 1, k) + get_binomial_coefficients(n - 1, k - 1)


def main() -> None:
    data = input().split()
    n, k = int(data[0]), int(data[1])
    print(get_binomial_coefficients(n, k))


if __name__ == "__main__":
    main()
