from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return f""" 
Item: {self._nome} 
R${self._preco:.2f}
Descrição: {self._descricao}"""
    
    def aplicar_desconto(self, percentual):
        desconto = self._preco * (percentual / 100)
        self._preco -= desconto