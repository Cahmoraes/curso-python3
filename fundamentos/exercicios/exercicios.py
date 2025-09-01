"""
1- Escreva uma programa que lê dois nomes e retorne uma string
   formatada no formato "ÚltimoNome, PrimeiroNome".
"""
# primeiro_nome = input("Forneça o primeiro nome:\n")
# ultimo_nome = input("Forneça o último nome:\n")
# print(f"{ultimo_nome.title()}, {primeiro_nome.title()}")

"""
2- Inverta a ordem das palavras em uma string fornecida.
"""
# string_original = input("Insira uma string para ser invertida:\n")
# string_invertida = string_original[::-1]
# print(string_invertida)

# texto = "Python é muito interessante"
# palavras = texto.split()
# textoInvertido = " ".join(palavras[::-1])
# print(textoInvertido)

"""
3- Verifique se uma string fornecida é um palíndromo —
   (pode ser lida da mesma forma de trás para frente).
"""
string_original = input("Insira uma string para ser invertida:\n")
string_formatada = string_original.lower().replace("", "")
string_invertida = string_formatada[::-1]
eh_palindromo = string_formatada == string_invertida
print(eh_palindromo)
