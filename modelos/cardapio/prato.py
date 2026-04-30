class Prato:
    def __init__(self, nome: str, preco: float, descricao: str):
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    def __str__(self):
        return f"{self._nome} - R${self._preco:.2f}\n{self._descricao}"