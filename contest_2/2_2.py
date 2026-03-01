import json
from typing import List, TypeAlias, Union

RecursiveList: TypeAlias = List[Union[int, "RecursiveList"]]


def expand(current_list: RecursiveList) -> List[int]:
    answer: List[int] = []
    for elem in current_list:
        if isinstance(elem, list):
            answer.extend(expand(elem))
        else:
            answer.append(elem)
    return answer


def main() -> None:
    print(expand(json.loads(input())))


if __name__ == "__main__":
    main()
