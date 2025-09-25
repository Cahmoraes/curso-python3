from sqlalchemy import create_engine, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column

engine = create_engine("sqlite:///banco.db", echo=True)
Base = declarative_base()


class Filme(Base):
    __tablename__ = "filmes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    ano: Mapped[int] = mapped_column(Integer, nullable=False)
    nota: Mapped[float] = mapped_column(Float, nullable=False)


Base.metadata.create_all(engine)


# Inserir Dados
def adiciona_filme(nome: str, ano: int, nota: float):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = Filme(nome=nome, ano=ano, nota=nota)
    session.add(filme)
    session.commit()
    session.close()


# adiciona_filme("Mario", 2022, 9.5)
# adiciona_filme("Sonic", 2019, 8.5)


def atualiza_filme(id: int, nome: str | None, ano: int | None, nota: float | None):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        session.commit()
    session.close()


def excluir_filme(id: int):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        session.delete(filme)
    session.commit()
    session.close()


atualiza_filme(1, "Homem Aranha", 2016, 9.0)
