cursos = []

with open("./dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.rstrip().split(",")
        cursos.append(f"{linguagem}-{categoria}")

print("-" * 50)

for curso in sorted(cursos):
    print(curso)
