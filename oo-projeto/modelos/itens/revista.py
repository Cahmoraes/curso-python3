from modelos.itens.item_biblioteca import Item_Biblioteca


class Revista(Item_Biblioteca):
    def __init__(self, titulo, autor, preco, edicao):
        super().__init__(titulo, autor, preco)
        self.edicao = edicao
