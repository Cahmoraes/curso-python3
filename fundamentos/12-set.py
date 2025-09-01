filmeSet = {
  "Inception", "The Shawshank Redemption", 
  "The Dark Knight", "Pulp Fiction", "Interstellar"
}

print(type(filmeSet))

# 1 - Buscar o tamanho do Set
print(len(filmeSet))

# 2  - True e 1 são considerados o mesmo valor
exampleSet = {"Interstellar", True, 1, 8.7}
print(exampleSet)

# 3 - Adicionar item de outro set
filmeSet.update(exampleSet)
print(filmeSet)

# 4 - Remover um item no Set
filmeSet.remove(True)
filmeSet.remove(8.7)
print(filmeSet)

