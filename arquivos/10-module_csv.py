from typing import TypedDict
import csv


class Course(TypedDict):
    language: str
    category: str


courses: list[Course] = []

with open("./dados/cursos.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print(reader)
    for row in reader:
        courses.append({"category": row["category"], "language": row["language"]})

print(courses)
