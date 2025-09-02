from collections import Counter, deque, namedtuple
from operator import itemgetter

# 1 - Lista de Frutas (Contagem)
fruits = [
    "Maçã",
    "Banana",
    "Uva",
    "Pêra",
    "Banana",
    "Uva",
    "Maçã",
    "Laranja",
    "Banana",
    "Abacaxi",
    "Tangerina",
    "Uva",
    "Pêra",
    "Banana",
]

print(Counter(fruits))

# 3 - Utilizando tupla nomeada
game = namedtuple("game", ["name", "price", "note"])
g1 = game("Fifa 23", 90.50, 8.5)
g2 = game("Resident Evil 4 Remake", 300, 10.0)
print(g1)
print(g2)
print(g2.note)

# 4 - Ordenando dicionários
students = {"Thomas": 24, "Igor": 20, "Caique": 31, "Isabella": 26}

students_sorted = sorted(students.items(), key=itemgetter(0))
print(students_sorted)

# 4 - Utilizando uma fila em ambas as extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
