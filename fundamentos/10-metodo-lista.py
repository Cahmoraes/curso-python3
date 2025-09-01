filmesList = ["Inception", "The Shawshank Redemption", 
              "The Dark Knight", "Pulp Fiction", "Interstellar"
            ]

# 1 - Tamanho da lista
print(len(filmesList))

# 2 - Recuperar um item da Lista pelo nome
print(filmesList.index("Interstellar"))

# 3 - Adicionar um item no final da Lista
filmesList.append("The Lord of the Rings")
print(filmesList)

# 4 - Ordena a lista
filmesList.sort()
print(filmesList)

# 5 - Copia os itens de uma lista para outra
filmesCopy = filmesList.copy()
filmesCopy.remove("Pulp Fiction")
print(filmesCopy, filmesList)

# 6 - Remove todos os itens da lista
filmesList.clear()
print(filmesList)