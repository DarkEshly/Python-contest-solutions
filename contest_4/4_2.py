import random
import sys
from typing import TypedDict

DECK_SIZE = 42
COLORS = ("red", "green", "blue", "yellow")
CARDS_PER_PLAYER = {2: 8, 3: 7, 4: 6}
RANGES_OF_COST = ((10, 25), (25, 50), (50, 100), (100, 200))


class PlayerDict(TypedDict):
    color: str
    cards: list[int]


class GameDict(TypedDict):
    players: list[PlayerDict]
    costs: list[int]
    card_deck: list[int]


def generate(number: int) -> GameDict:
    colors = random.sample(COLORS, number)
    current_deck = [i for i in range(1, DECK_SIZE + 1)]
    random.shuffle(current_deck)
    costs = [random.randint(RANGES_OF_COST[i][0], RANGES_OF_COST[i][1]) for i in range(number)]
    cards_per_player = CARDS_PER_PLAYER[number]
    players: list[PlayerDict] = []
    for i in range(number):
        players.append({"color": colors[i], "cards": current_deck[i * cards_per_player : cards_per_player * (i + 1)]})
    return {"players": players, "costs": costs, "card_deck": current_deck[number * cards_per_player :]}


def main():
    exec(sys.stdin.read())


if __name__ == "__main__":
    main()
