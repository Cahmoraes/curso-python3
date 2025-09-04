from modelos.itens.item_biblioteca import Item_Biblioteca


class Livro(Item_Biblioteca):
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco)
        self.isbn = isbn

    def aplicar_desconto(self):
        self._preco -= self._preco * 0.1  # 10% de desconto
