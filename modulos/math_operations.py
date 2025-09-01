# Módulo de operações matemáticas

def sum(x, y):
  return y + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y != 0:
    return x / y
  raise ValueError("Não é divido por zero")
  
