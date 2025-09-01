# função de potência de um número
power = lambda num: num ** 2
print(power(2))

is_even = lambda num: num % 2 == 0

print(is_even(2))
print(is_even(1))

# Função que divide um número pelo outro
div_num = lambda num1, num2: num1 / num2
print(div_num(2,6))

# Reverte uma string
revert_string = lambda aString: aString[::-1]
print(revert_string("caique"))

# Funcionalidades com filmes

movies_list = ["Titanic", "The GodFather", "Inception"]

ratings: dict = {
  "Titanic": [8.5, 9.0, 7.5],
  "The GodFather": [9.5, 9.8, 8.0],
  "Inception": [8.0, 7.0, 8.5],
}

# Função para calcular a média de avaliações dos filmes

calculate_average_for = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])
print(f"A média de avaliação do filme: Titanic é: {calculate_average_for('Titanic')}")

# Verificar se um filme está na lista
check_movie = lambda movie_name: movie_name in movies_list
print(check_movie("Titanic"))

recommend_movie = lambda movie_name: f"Recomendo o filme {movie_name} que está na média {calculate_average_for(movie_name):.2f}"

print(recommend_movie("Inception"))