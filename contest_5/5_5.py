from abc import ABC, abstractmethod
from typing import Optional


class Object:
    def __init__(self, cost: int, income: int, square: int):
        self.cost = cost
        self.income = income
        self.square = square

    def __repr__(self) -> str:
        return f"({self.cost}, {self.income}, {self.square})"


class StrategyBase(ABC):
    @abstractmethod
    def compare(self, first: Object, second: Object) -> bool:
        pass

    def select(self, objects: list[Object], money: int) -> Optional[Object]:
        can_build = [object for object in objects if object.cost <= money]
        if len(can_build) == 0:
            return None
        best_object = can_build[0]
        for object in can_build[1:]:
            if self.compare(object, best_object):
                best_object = object
        return best_object


class StrategyIncome(StrategyBase):
    def compare(self, first: Object, second: Object) -> bool:
        first_value = first.income / first.cost
        second_value = second.income / second.cost
        if first_value == second_value:
            first_square_value = first.square / first.cost
            second_square_value = second.square / second.cost
            if first_square_value == second_square_value:
                return first.income > second.income
            return first_square_value > second_square_value
        return first_value > second_value


class StrategySquare(StrategyBase):
    def compare(self, first: Object, second: Object) -> bool:
        first_value = first.square / first.cost
        second_value = second.square / second.cost
        if first_value == second_value:
            first_income_value = first.income / first.cost
            second_income_value = second.income / second.cost
            if first_income_value == second_income_value:
                return first.income > second.income
            return first_income_value > second_income_value
        return first_value > second_value


class Context:
    def __init__(self, strategy: StrategyBase):
        self.strategy = strategy
        self.objects: list[Object] = []
        self.money: int = 0
        self.global_income: int = 0
        self.global_square: int = 0

    def set_strategy(self, strategy: StrategyBase):
        self.strategy = strategy

    def build(self, available_objects: list[Object]) -> bool:
        selected_object = self.strategy.select(available_objects, self.money)
        if not selected_object:
            return False
        self.money -= selected_object.cost
        self.global_income += selected_object.income
        self.global_square += selected_object.square
        self.money += self.global_income
        print(
            f"Selected: {selected_object}, Money: {self.money}, Income: {self.global_income}, Square: {self.global_square}"
        )
        available_objects.remove(selected_object)
        return True


def main():
    m, n = map(int, input().split())
    objects: list[Object] = []
    for _ in range(n):
        cost, income, square = map(int, input().split())
        objects.append(Object(cost, income, square))
    first_strategy_count, second_strategy_count = map(int, input().split())
    context = Context(StrategyIncome())
    context.money = m
    for _ in range(first_strategy_count):
        if not context.build(objects):
            break
    context.set_strategy(StrategySquare())
    for _ in range(second_strategy_count):
        if not context.build(objects):
            break


if __name__ == "__main__":
    main()
