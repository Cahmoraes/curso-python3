from modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca(nome="Biblioteca da Cidade")
biblioteca_shopping = Biblioteca(nome="Biblioteca do Shopping")

biblioteca_cidade.alterna_estado()
biblioteca_cidade.receber_avaliacao("Caique", 10)
biblioteca_cidade.receber_avaliacao("Thomas", 9.5)


def main():
    Biblioteca.listar_bibliotecas()


print(__name__)
if __name__ == "__main__":
    main()
