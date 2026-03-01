import re
import sys


def refactor_code(code: str) -> str:
    pattern = re.compile(
        r"CalcDistance(\s*\(\s*)([\w.]+)(\s*,\s*)([\w.]+)(\s*,\s*)([\w.]+)(\s*,\s*)([\w.]+)(\s*\))", re.MULTILINE
    )
    replacement = r"GeoDistance\1\2\3\6\5\4\7\8\9"
    return pattern.sub(replacement, code)


def main() -> None:
    print(refactor_code(sys.stdin.read()))


if __name__ == "__main__":
    main()
