import json
import string


def get_tokens(current_string: str) -> list[str]:
    answer: list[str] = []
    current_token = ""
    for letter in current_string:
        if letter.isalnum():
            current_token += letter
        elif letter in string.punctuation or letter.isspace():
            if current_token != "":
                answer.append(current_token)
            current_token = ""
            if letter in string.punctuation:
                answer.append(letter)
    if current_token != "":
        answer.append(current_token)
    return sorted(list(set(answer)))


def main() -> None:
    print(json.dumps(get_tokens(input())))


if __name__ == "__main__":
    main()
