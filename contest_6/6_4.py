import json
import sys
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class StudentDepartment:
    student: str
    department: str


@dataclass
class StudentGrade:
    student: str
    grade: float


class Stats:
    def __init__(self) -> None:
        self._grades: list[float] = []

    def add(self, value: float) -> None:
        self._grades.append(value)

    @property
    def average(self) -> float:
        if len(self._grades) == 0:
            return 0
        return sum(self._grades) / len(self._grades)


def main():
    departments_list: list[StudentDepartment] = []
    grades_list: list[StudentGrade] = []
    for line in sys.stdin:
        if "{" not in line:
            continue
        data = json.loads(line)
        if "department" in data:
            departments_list.append(StudentDepartment(**data))
        if "grade" in data:
            grades_list.append(StudentGrade(**data))
    student_to_department = {elem.student: elem.department for elem in departments_list}
    departments_to_grades: defaultdict[str, Stats] = defaultdict(Stats)
    for grade in grades_list:
        department = student_to_department.get(grade.student)
        if department:
            departments_to_grades[department].add(grade.grade)
    result = sorted(departments_to_grades.keys())
    for department in result:
        print(departments_to_grades[department].average)


if __name__ == "__main__":
    main()
