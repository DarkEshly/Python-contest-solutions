from typing import List, Tuple

COORDS_NUM = 3


def get_square(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> float:
    answer = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) / 2
    return answer


def main() -> None:
    coords: List[Tuple[float, ...]] = []
    for _ in range(COORDS_NUM):
        data = input().split()
        coords.append((float(data[0]), float(data[1])))
    answer = get_square(coords[0][0], coords[0][1], coords[1][0], coords[1][1], coords[2][0], coords[2][1])
    print("The area of the triangle is", answer)


if __name__ == "__main__":
    main()
