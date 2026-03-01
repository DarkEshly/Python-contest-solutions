import sys


class Student:
    def __init__(self, name: str, age: int, course: int) -> None:
        self.name = name
        self.age = age
        self.course = course


class University:
    def __init__(self) -> None:
        self._students: dict[str, Student] = {}

    def enroll_student(self, name: str, age: int, course: int) -> None:
        if name in self._students:
            raise RuntimeError(f"Student with name {name} is already enrolled")
        self._students[name] = Student(name, age, course)

    def expell_student(self, name: str) -> None:
        if name not in self._students:
            raise KeyError(f"Student with name {name} is not enrolled")
        self._students.pop(name)

    def get_students(self) -> list[Student]:
        return sorted(self._students.values(), key=lambda student: student.name)

    @staticmethod
    def print_students(students: list[Student]) -> None:
        for student in students:
            print(f"Name: {student.name}, age: {student.age}, course: {student.course}")

    @staticmethod
    def average_age(students: list[Student]) -> float:
        if len(students) == 0:
            return 0
        return sum(student.age for student in students) / len(students)


def main():
    exec(sys.stdin.read())


if __name__ == "__main__":
    main()
