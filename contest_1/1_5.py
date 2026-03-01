import os


def get_path(root_path: str, first_directory: str, second_directory: str) -> str:
    answer = os.path.join(root_path, first_directory, second_directory)
    return answer


def main() -> None:
    print(get_path(input(), input(), input()))


if __name__ == "__main__":
    main()
