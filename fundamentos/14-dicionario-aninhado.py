import json

filmesDict = {
  "Inception": {
    "yearRelease": 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Thriller"],
  },
  "Interstellar": {
    "yearRelease": 2014,
    "imdbRating": 8.6,
    "genre": ["Sci-fi", "Drama"],
  },
  "The Dark Knight": {
    "yearRelease": 2008,
    "imdbRating": 9.0,
    "genre": ["Action", "Drama", "Crime"],
  }
}

# result = json.dumps(filmesDict, indent=4)
# print(result)

# 1 - Buscar informação dentro de um dicionário aninhado
print(filmesDict["Interstellar"]["genre"])

# 2 - Adicionar novo item
filmesDict["Inception"]["Director"] = "Christopher Nolan"
print(filmesDict["Inception"])

# 3 - Excluir um dicionário
del filmesDict["The Dark Knight"]
print(json.dumps(filmesDict, indent=4))