# Lista de filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - Iterando valores de uma lista de filmes usando o while
index = 0
while index < len(moviesList):
  print(moviesList[index])
  index += 1
  
# 2 - Quando a condição for atendida o loop será encerrado
print("="*30)
index = 0
while index < len(moviesList):
  if moviesList[index] == "Inception":
    break
  print(moviesList[index])
  index += 1
  
  
# 2 - Quando a condição for atendida o loop vai para a próxima iteração
print("="*30)
index = 0
while index < len(moviesList):
  if moviesList[index] == "Inception":
    index += 1
    continue
  print(moviesList[index])
  index += 1
  
# 4 - Avaliação do filme com While
print("="*30)
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))
total = 0
count = 0
average = 0

while count < movieRating:
  note = float(input("Digite a nota para o filme:\n"))
  total += note
  count += 1
  
if movieRating >= 0:
  average = total / movieRating

print(f"A média de avaliação do filme {movieName} é: {average:.2f}")

