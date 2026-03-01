import copy
import json
import sys
from typing import Any, Dict


def get_new_dict(new_dict: Dict[str, Any], path: str, number: int) -> Dict[str, Any]:
    current_path = path.split("/")
    current_dict = new_dict
    for i in range(len(current_path) - 1):
        if current_path[i] not in current_dict:
            current_dict[current_path[i]] = {}
        if isinstance(current_dict[current_path[i]], dict):
            current_dict = current_dict[current_path[i]]
        else:
            current_dict[current_path[i]] = {}
            current_dict = current_dict[current_path[i]]
    current_dict[current_path[-1]] = number
    return new_dict


def main() -> None:
    current_dict: Dict[str, Any] = json.loads(input())
    data = sys.stdin.readlines()
    for line in data:
        path, number = line.split()[0], int(line.split()[1])
        new_dict: Dict[str, Any] = copy.deepcopy(current_dict)
        new_dict = get_new_dict(new_dict, path, number)
        print(json.dumps(new_dict))


if __name__ == "__main__":
    main()
