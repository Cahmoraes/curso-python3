# 1 Funções para imprimir um nome completo

def full_name(first_name: str = "", last_name: str ="Moraes") -> str:
  print(f"O nome completo é: {first_name} {last_name}")
  
# full_name("moraes", "caique")

# HOC
def with_first_name(first_name: str):
  return lambda las_name:  f"Nome completo é: {first_name} {las_name}"

with_caique = with_first_name("Caique")
# print(with_caique("Moraes"))

# Decorator
def with_first_name_decorator(first_name: str):
    def hoc(func):
      return lambda *args, **kwargs: f"Nome completo é {first_name} {func(*args, **kwargs)}"
    return hoc
  
@with_first_name_decorator("Caique")
def get_lastname():
  return "Moraes"

# print(get_lastname())

# *args e **kwargs
def do_the_job(*args, **kwargs):
  print(type(args))
  print(*args)
  print(type(kwargs))
  print(kwargs)

do_the_job("Caique", "Moraes", user="cahmoraes")