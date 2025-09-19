from typing import TypedDict


class Course(TypedDict):
    language: str
    category: str


cursos: list[Course] = []

with open("./dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        cursos.append({"language": language, "category": category})


print("Language:")
for curso in sorted(cursos, key=lambda course: course["category"]):
    print(f"{curso['language']}-{curso['category']}")

print("-" * 50)

for curso in sorted(cursos, key=lambda course: course["language"]):
    print(f"{curso['language']}-{curso['category']}")
