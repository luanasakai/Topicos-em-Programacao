from Model.Venda import Venda
from Model.Produto import Produto

class ItemVenda:

    def __init__(self, id=0, qtde=0, valor_total=0.00, venda=Venda(), produto=Produto()):
        self._id = id
        self._qtde = qtde
        self._valor_total = valor_total
        self._venda = venda
        self._produto = produto

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