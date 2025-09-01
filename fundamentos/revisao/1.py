"""
1- Escreva uma programa que lê dois nomes e retorne uma string
   formatada no formato "ÚltimoNome, PrimeiroNome".
"""
# primeiro_nome = input("Informe o primeiro nome:\n")
# segundo_nome = input("Informe o segundo nome:\n")
# print(f"{segundo_nome}, {primeiro_nome}")

"""
2- Inverta a ordem das palavras em uma string fornecida.
"""
# original_string = "caique moraes"
# string_separada = original_string.split()[::-1]
# string_invertida = " ".join(string_separada)
# print(string_invertida)


"""
3- Verifique se uma string fornecida é um palíndromo —
   (pode ser lida da mesma forma de trás para frente).
"""

palavra = input("Digite uma palavra para verificar se é palíndromo:\n")
eh_palindromo = palavra.strip().lower() == palavra[::-1].strip().lower()
print(eh_palindromo)