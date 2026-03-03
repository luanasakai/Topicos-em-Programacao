from Model import Produto, Venda

class ItemVenda:

    def __init__(self):
        self._id = 0
        self._qtde = 0
        self._valor_total = 0.0
        self._venda = Venda()
        self._produto = Produto()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def qtde(self):
        return self._qtde

    @qtde.setter
    def qtde(self, qtde):
        self._qtde = qtde

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def valor_total(self, valor_total):
        self._valor_total = valor_total

    def __str__(self):
        return (f"Código ItemVenda: {self.id}, "
                f"Quantidade: {self._qtde}, "
                f"Valor: {self.valor_total}, "
                f"Produto: {self._produto.nome}, "
                f"Venda: {self._venda}")