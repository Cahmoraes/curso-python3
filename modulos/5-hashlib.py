import hashlib

# 1 - Verificar os algoritmos disponíveis
print(hashlib.algorithms_available, len(hashlib.algorithms_available))

# 2 -Verificar algoritmos de acordo com o SO
print(hashlib.algorithms_guaranteed, len(hashlib.algorithms_guaranteed))

# 3 - Utilizando o sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é criá-lo".encode()
print(message)
algorithm.update(message)
print(algorithm.hexdigest())

# 4 - Utilizando o MD5
# para comprovar a integridade de dados
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())