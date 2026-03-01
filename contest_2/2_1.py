from typing import Dict


def main() -> None:
    n, m = map(int, input().split())
    dns_server: Dict[str, str] = dict()
    for _ in range(n):
        domen, ip = input().split()
        dns_server[domen] = ip
    for _ in range(m):
        print(dns_server.get(input(), "PUSTO"))


if __name__ == "__main__":
    main()
