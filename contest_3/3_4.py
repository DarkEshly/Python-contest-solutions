import sys
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def decorator(decorator_arg: str) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def decorator_sub(current_func: Callable[P, T]) -> Callable[P, T]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            for index, new_argument in enumerate(args):
                print(f"{index}: {new_argument}")
            answer = current_func(*args, **kwargs)
            print(f"{decorator_arg}: {answer}")
            return answer

        return wrapper

    return decorator_sub


def main() -> None:
    exec(sys.stdin.read())


if __name__ == "__main__":
    main()
