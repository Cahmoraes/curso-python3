filmesTupla = ("Inception", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction", "Interstellar")

print(type(filmesTupla))

# 1 - Os dois primeiros itens da Tupla
print(filmesTupla[:2])

# 2 - último item da tupla
print(filmesTupla[-1])

# 2.2 - tamanho da tupla
print(len(filmesTupla))

# 3 - filmes até uma determinada posição
print(filmesTupla[1:4])

# 4 - Buscar filmes de uma posição em diante
print(filmesTupla[2:])

# 5 - Recuperar um item da tupla pelo nome
print(filmesTupla.index("Pulp Fiction"))