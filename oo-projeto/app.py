from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_cidade = Biblioteca(nome="Biblioteca da Cidade")
biblioteca_shopping = Biblioteca(nome="Biblioteca do Shopping")

livro1 = Livro("1984", "George Orwell", 30.0, "084-3245")
livro2 = Livro("Brave New World", "Aldous Huxley", 25.0, "084-3188")

revista1 = Revista("National Geographic", "John Doe", 15.0, "Quinta")

# biblioteca_cidade.alterna_estado()
# biblioteca_cidade.receber_avaliacao("Caique", 10)
# biblioteca_cidade.receber_avaliacao("Thomas", 9.5)

biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(revista1)
biblioteca_cidade.adicionar_item(livro2)


def main():
    # Biblioteca.listar_bibliotecas()
    print(vars(livro1))
    print(vars(revista1))
    biblioteca_cidade.exibir_itens()


if __name__ == "__main__":
    main()
