class Produto:

    def __init__(self):
        self._id = 0
        self._nome = ""
        self._preco = 0.0
        self._qtde = 0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def qtde(self):
        return self._qtde

    @qtde.setter
    def qtde(self, qtde):
        self._qtde = qtde

    def __str__(self):
        return (f"Código Produto: {self.id}, "
                f"Nome: {self.nome}, "
                f"Preço: {self.endereco}, "
                f"Quantidade: {self.cidade}")