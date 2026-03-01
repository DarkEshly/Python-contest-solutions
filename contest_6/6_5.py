import sys


class BankDeposit:
    def __init__(self, balance: int, deposit_rate: int):
        self._balance = balance
        self._deposit_rate = deposit_rate

    @property
    def balance(self) -> int:
        return self._balance

    @property
    def deposit_rate(self) -> int:
        return self._deposit_rate

    @deposit_rate.setter
    def deposit_rate(self, value: int):
        if value < 0:
            raise ValueError("Deposit rate cannot be less than zero")
        self._deposit_rate = value

    def capitalization(self) -> None:
        self._balance += self._balance * self._deposit_rate // 100


def main():
    exec(sys.stdin.read())


if __name__ == "__main__":
    main()
