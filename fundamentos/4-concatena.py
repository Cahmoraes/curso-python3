# Concatenar valores

name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digite o ano de lançamento:\n"))
noteMovie = float(input("Digite a nota do filme: \n"))

# Alternativa 1
print("Dados do Filme")
print("===============")
print("Nome do filme: ", name)
print("Ano de lançamento: ", yearLaunch)
print("Nota do filme: ", noteMovie)

# Alternativa 2
print("===============")
print("Nome do filme: ", name, "\nAno de lançamento: ", yearLaunch, "\nNota do Filme: ", noteMovie)

# Alternativa 3
print("===============")
print(
  f"Nome do filme: {name}\n"
  f"Ano de lançamento: {yearLaunch}\n"
  f"Nota do filme: {noteMovie}"
)