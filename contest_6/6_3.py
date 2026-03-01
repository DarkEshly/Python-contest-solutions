import sys
from typing import Any, Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def decorator_lozhkin(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print("Так сказать")
        return func(*args, **kwargs)

    return wrapper


class FindLozhkin(type):
    def __new__(cls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]) -> type:
        if "lozhkin" not in namespace:
            raise TypeError("Очень плохой класс, в нём нет Ложкина")
        lozhkin_attribute = namespace["lozhkin"]
        if callable(lozhkin_attribute):
            namespace["lozhkin"] = decorator_lozhkin(lozhkin_attribute)
        elif isinstance(lozhkin_attribute, int):
            if lozhkin_attribute < 10**9:
                namespace["lozhkin"] = 10**9
        elif isinstance(lozhkin_attribute, str):
            namespace["lozhkin"] = f"Так сказать, {lozhkin_attribute}"
        new_lozhkin = super().__new__(cls, name, bases, namespace)
        return new_lozhkin


def main():
    exec(sys.stdin.read())


if __name__ == "__main__":
    main()
