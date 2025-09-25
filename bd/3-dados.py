import sqlite3

# 1 - Conectando no banco
conexao = sqlite3.connect("./titulo.db")

# 2 - Criando cursor
cursor = conexao.cursor()
cursor.execute(
    """
      INSERT INTO filmes(nome, ano, nota) 
      values ('Sonic', 2020, 8.0)
    """
)

conexao.commit()
conexao.close()
print("Dados inseridos na tabela")
