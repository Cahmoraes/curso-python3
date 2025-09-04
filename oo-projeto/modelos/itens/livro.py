from modelos.itens.item_biblioteca import Item_Biblioteca


class Livro(Item_Biblioteca):
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco)
        self.isbn = isbn
