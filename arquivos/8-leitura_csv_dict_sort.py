from typing import TypedDict


class Course(TypedDict):
    language: str
    category: str


cursos: list[Course] = []

with open("./dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        cursos.append({"language": language, "category": category})


def get_language(course: Course) -> str:
    return course["language"]


def get_category(course: Course) -> str:
    return course["category"]


print("Language:")
for curso in sorted(cursos, key=get_language):
    print(f"{curso['language']}-{curso['category']}")

print("-" * 50)

for curso in sorted(cursos, key=get_category):
    print(f"{curso['language']}-{curso['category']}")
