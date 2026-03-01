from collections import Counter


def main() -> None:
    print(" ".join(sorted(elem for elem, num in Counter(input().lower().split()).items() if num == 2)))


if __name__ == "__main__":
    main()
