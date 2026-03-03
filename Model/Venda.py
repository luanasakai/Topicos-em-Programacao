from Model import Cliente

class Venda:

    def __init__(self):
        self._id = 0
        self._data = ""
        self._valor_total = 0.0
        self._cliente = Cliente()
        self.itens = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def valor_total(self, valor_total):
        self._valor_total = valor_total

    def __str__(self):
        return (f"Código Produto: {self.id}, "
                f"Nome: {self.nome}, "
                f"Valor Total: {self.valor_total}, "
                f"Cliente: {self._cliente.nome}, ")