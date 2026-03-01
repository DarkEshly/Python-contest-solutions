import calendar
import datetime
import sys


def correct_date(day: int, month: int, year: int) -> tuple[int, int]:
    if month == 2 and day == 29 and not calendar.isleap(year):
        return 1, 3
    return day, month


def days_until_next_birthday(current_date: str, birthdays: list[str]) -> int:
    today = datetime.datetime.strptime(current_date, "%d.%m.%Y").date()
    min_delta = -1
    for new_birthday in birthdays:
        data = new_birthday.split(".")
        day, month = correct_date(int(data[0]), int(data[1]), today.year)
        birthday_date = datetime.date(today.year, month, day)
        if birthday_date < today:
            day, month = correct_date(int(data[0]), int(data[1]), today.year + 1)
            birthday_date = datetime.date(today.year + 1, month, day)
        if min_delta == -1:
            min_delta = (birthday_date - today).days
        else:
            min_delta = min(min_delta, (birthday_date - today).days)
    return min_delta


def main() -> None:
    data = sys.stdin.readlines()
    current_date = data[0].split()[2].rstrip()
    birthdays = data[1:]
    print(days_until_next_birthday(current_date, birthdays))


if __name__ == "__main__":
    main()
