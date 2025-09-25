from conexao_postgres import conn

cursor_obj = conn.cursor()

games = [("The Last of US II", 2020, 9.5), ("Spiderman 2", 2023, 10.0)]

for game in games:
    cursor_obj.execute(
        """
          INSERT INTO db_games.games(name, year, score)
          values (%s, %s, %s)
        """,
        game,
    )
conn.commit()
print("Dados inseridos com sucesso!")
conn.close()
