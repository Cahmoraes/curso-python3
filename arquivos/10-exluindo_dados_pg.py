from conexao_postgres import conn

cursor = conn.cursor()

sql = """
  DELETE FROM db_games.games
  WHERE id = %s
"""

cursor.execute(sql, (5,))

conn.commit()
print("Dados excluídos com sucesso")
