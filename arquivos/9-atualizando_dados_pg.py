from conexao_postgres import conn

cursor_obj = conn.cursor()

sql = """
  UPDATE db_games.games
  SET NAME = %s
  WHERE ID = %s 
"""

cursor_obj.execute(sql, ("Fifa 23", 3))
conn.commit()
print("Dados atualizados com sucesso")
conn.close()
