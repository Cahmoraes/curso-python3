from modelos.itens.item_biblioteca import Item_Biblioteca


class Revista(Item_Biblioteca):
    def __init__(self, titulo, autor, preco, edicao):
        super().__init__(titulo, autor, preco)
        self.edicao = edicao

    def aplicar_desconto(self):
        self._preco -= self._preco * 0.05
