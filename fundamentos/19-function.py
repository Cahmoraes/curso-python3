# 1 - Função para imprimir uma mensagem
def welcome():
  print("Bem vindo ao sistema de filmes!")

welcome()

# função para calcular a média de notas

# def calculate_average():
#   average = 0
#   total = 0
#   num_ratings = int(input("Digite quantas avaliações deseja fazer para o filme:\n"))
#   for _ in range(num_ratings):
#     note = float(input("Digite a nota para o filme:\n"))
#     total += note
#   if num_ratings > 0:
#     average = total / num_ratings
#   else:
#     average = 0
#   return average

# print(f"A média de avaliações é: {calculate_average():.2f}")

# função para cadastrar um filme
def create_movie():
  name = input("Digite o nome do filme:\n")
  yearLaunch = int(input("Digite o ano de lançamento:\n"))
  moviePrice = float(input("Digite o preço do filme:\n"))
  rating = float(input("Digite a nota do filme: \n"))
  print(f"{name} ({yearLaunch}) - R$ {moviePrice:.2f}")
  
create_movie()
create_movie()