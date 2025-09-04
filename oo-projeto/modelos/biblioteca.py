from modelos.avaliacao import Avaliacao
from modelos.itens.item_biblioteca import Item_Biblioteca


class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacoes = []
        self._items = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome

    @classmethod
    def listar_bibliotecas(cls):
        print(
            f"{'Nome da biblioteca'.ljust(25)} | {'Nota média'.ljust(25)} | {'Status'}"
        )
        for biblioteca in Biblioteca.bibliotecas:
            print(
                f"{biblioteca.nome.ljust(25)} | {str(biblioteca.media_avaliacoes).ljust(25)} | {biblioteca._ativo}"
            )

    def alterna_estado(self):
        self._ativo = not self._ativo

    @staticmethod
    def sum(n1, n2):
        return n1 + n2

    @property
    def ativo(self):
        return "ativado" if self._ativo else "desativado"

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return "-"
        soma = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        media = round(soma / len(self._avaliacoes), 1)
        return media

    def adicionar_item(self, item):
        if isinstance(item, Item_Biblioteca):
            self._items.append(item)

    def exibir_itens(self):
        print(f"Itens da biblioteca {self.nome}\n")
        for i, item in enumerate(self._items, start=1):
            if hasattr(item, "isbn"):
                msg_livro = f"{i}. (Livro) -> Título: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | ISBN: {item.isbn}"
                print(msg_livro)
                continue
            msg_revista = f"{i}. (Revista) -> Título: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | Edição: {item.edicao}"
            print(msg_revista)
