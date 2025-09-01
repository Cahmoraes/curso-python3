movieName = "Top Gun"
movieDescription = """
Top Gun Maverick, é um filme de aviação e aventura,
Muito consagrado na indústria
"""

print(movieName.upper())
print(movieName.lower())
print(movieName.capitalize())
print(movieName.title()) # Primeira letra de cada palavra em minúscula
print(movieName.center(10, "-")) # Retorna string centralizada com caractere de preenchimento
print(movieName.find("u")) # Retorna posição/índice do caracteres
print(movieName.count("o")) # Conta caracteres
print(movieName.replace("Top", "Matrix"))
print(movieDescription.split(","))