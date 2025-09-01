# Operadores

num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

# Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
multi = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print("# Aritméticos")
print(f"Soma: {sum}")
print(f"Substração: {sub}")
print(f"Módulo: {mod}")
print(f"Potência: {exp}")
print(f"Divisão: {div}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"Os números {num1} e {num2} são iguais? {equal}")
print(f"O número {num1} é maior ou igual a {num2}? {bigger_equal}")

# Atribuição
# num1 = num1 + 1
num1 = 1
num1 -= 1
