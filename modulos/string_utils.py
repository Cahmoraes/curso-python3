# Módulo de operações com strings

def capitalize(string: str) -> str:
  return f"{string[0].upper()}{string[1:]}"

def reverse_string(string: str) -> str:
  return string[::-1]

def count(string: str) -> str:
  return len(string)