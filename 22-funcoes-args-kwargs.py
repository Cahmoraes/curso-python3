"""
  *args - utilizamos ele quando não temos certeza de quantos argumentos queremos ter em uma função - Os argumentos são passados como uma tupla
  
  **kwargs - Além dos valores, podemos passar as respectivas chaves para cada argumento.
  Os argumentos são passados como um dicionário
"""

# 1 - Soma de números
def sum(*num: tuple[int]):
  total = 0
  for num in num:
    total += num
  return total
    
print(sum(1,2,3))
print(sum(1))

# 2 - Apresentação de cursos
def presentation(**data):
  for key, value in data.items():
    print(f"{key} - {value}")

presentation(name="Python", category="Backend", level="Iniciante")
