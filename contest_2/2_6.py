import json
from typing import Dict, List


def list_to_dict(current_list: List[str]) -> Dict[str, str]:
    answer = {elem: str(int(elem) ** 2) for elem in current_list if elem.isdigit()}
    return answer


def main() -> None:
    current_list: List[str] = json.loads(input())
    answer: Dict[str, str] = list_to_dict(current_list)
    print(json.dumps(answer))


if __name__ == "__main__":
    main()
