SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def get_time(seconds: int) -> str:
    hours = seconds // SECONDS_IN_HOUR
    minutes = (seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    left_seconds = seconds % SECONDS_IN_MINUTE
    answer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, left_seconds)
    return answer


def main() -> None:
    print(get_time(int(input())))


if __name__ == "__main__":
    main()
