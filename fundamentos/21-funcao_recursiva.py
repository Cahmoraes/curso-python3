"""
  Fatorial de um número:
  1 -> 1 * 1
  2 -> 2 * 1
  3 -> 3 * 2 * 1
"""

# 1 - Fatorial de um número
def fatorial(num: int) -> int:
  if num == 1: return 1
  return (num * fatorial(num - 1))

number = int(input("Digite o número para o fatorial:\n"))
print(f"O fatorial de {number} é {fatorial(number)}")

def total_sum(num):
  if num == 1: return 1
  return (num + total_sum(num - 1))