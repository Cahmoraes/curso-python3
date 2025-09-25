import sqlite3


# 1 - Conectar banco de dados
def conecta_db() -> sqlite3.Connection:
    conexao = sqlite3.connect("./titulo.db")
    return conexao


def insere_dados(nome: str, ano: int, nota: float) -> None:
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(
        """
          INSERT INTO filmes(nome, ano, nota)
          values (?, ?, ?)
        """,
        (nome, ano, nota),
    )
    conexao.commit()
    conexao.close()


def obter_dados():
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    return dados
