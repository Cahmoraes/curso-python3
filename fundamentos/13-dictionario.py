filmeInception = {
  "title": "Inception",
  "yearRelease": 2010,
  "imdbRating": 8.8,
  "genre": ["Sci-fi", "Action", "Thriller"],
}

print(filmeInception)
print(len(filmeInception))
print(type(filmeInception))

# 1 - Recuperar um elemento do dicionário
print(filmeInception["title"])
print(filmeInception.get("genre"))

# 2 - Buscar apenas as chaves do dicionário
print(filmeInception.keys())

# 3 - Apenas os valores do dicionário
print(filmeInception.values())

# 4 - Buscar filmes do dicionário com chaves e valor
print(filmeInception.items())

# 5 - Adicionar itens no dicionário
filmeInception["director"] = "Christopher Nolan"
print(filmeInception)

# 6 - Adicionar itens no dicionário
filmeInception.update({
  "imdbRate": 8.7,
})
print(filmeInception)

# 7 - Remover filme do dicionário
print(filmeInception.pop("director"))
print(filmeInception)