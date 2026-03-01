import random
import string
import sys


def generate_password(
    length: int, digits: bool = False, uppercase_letters: bool = False, special_symbols: bool = False
) -> str:
    necessary_length = 1
    password: list[str] = []
    password.append(random.choice(string.ascii_lowercase))
    all_letters = string.ascii_lowercase
    if digits:
        necessary_length += 1
        password.append(random.choice(string.digits))
        all_letters += string.digits
    if uppercase_letters:
        necessary_length += 1
        password.append(random.choice(string.ascii_uppercase))
        all_letters += string.ascii_uppercase
    if special_symbols:
        necessary_length += 1
        password.append(random.choice(string.punctuation))
        all_letters += string.punctuation
    if length < necessary_length:
        raise ValueError("Not enough length")
    password.extend(random.choices(all_letters, k=length - len(password)))
    random.shuffle(password)
    return "".join(password)


def main():
    exec(sys.stdin.read())


if __name__ == "__main__":
    main()
