from typing import TypedDict


class Curso(TypedDict):
    language: str
    category: str


cursos: list[Curso] = []

with open("./dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        cursos.append({"language": language, "category": category})

for curso in cursos[1:]:
    print(f"{curso['language']}-{curso['category']}")
