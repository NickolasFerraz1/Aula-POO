class Bebida():
    def __init__(self, nome: str, preco: float, tamanho: int):
        self._nome = nome
        self._preco = preco
        self._tamanho = tamanho

    def __str__(self):
        return f"{self._nome} - R${self._preco:.2f} ({self._tamanho}ml)"