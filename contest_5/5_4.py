from abc import ABC, abstractmethod
from math import sqrt


class MetricBase(ABC):
    @abstractmethod
    def calculate(self, first_vector: list[float], second_vector: list[float]) -> float:
        pass

    @staticmethod
    def create(name: str) -> "MetricBase":
        if name == "euclidean":
            return EuclideanMetric()
        elif name == "manhattan":
            return ManhattanMetric()
        else:
            raise ValueError("Задана неизвестная метрика.")


class EuclideanMetric(MetricBase):
    def calculate(self, first_vector: list[float], second_vector: list[float]) -> float:
        return sqrt(sum((x - y) ** 2 for x, y in zip(first_vector, second_vector)))


class ManhattanMetric(MetricBase):
    def calculate(self, first_vector: list[float], second_vector: list[float]) -> float:
        return sum(abs(x - y) for x, y in zip(first_vector, second_vector))


def read_vector() -> list[float]:
    return list(map(float, input().split()))


def main() -> None:
    metric_name: str = input()
    first_vecor: list[float] = read_vector()
    second_vector: list[float] = read_vector()
    metric_class: MetricBase = MetricBase.create(metric_name)
    print(metric_class.calculate(first_vecor, second_vector))


if __name__ == "__main__":
    main()
