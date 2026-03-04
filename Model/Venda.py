from Model.Cliente import Cliente

class Venda:

    def __init__(self, id=0, data="", valor_total=0.00, cliente=None, itens=None):
        self._id = id
        self._data = data
        self._valor_total = valor_total
        self._cliente = cliente
        self.itens = itens if itens is not None else []

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

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def itens(self):
        return self._itens

    @itens.setter
    def itens(self, itens):
        self._itens = itens

    def __str__(self):
        itens_str = "\n".join(
            f"  Produto: {item.produto.nome} | "
            f"Qtd: {item.quantidade} | "
            f"Subtotal: R$ {item.subtotal:.2f}"
            for item in self._itens
        )

        cliente_nome = self._cliente.nome if self._cliente else "Sem cliente"
        return (
            f"\nCódigo Venda: {self.id}"
            f"\nData: {self.data}"
            f"\nValor Total: R$ {self.valor_total:.2f}"
            f"\nCliente: {cliente_nome}"
            f"\nItens:\n{itens_str if itens_str else '  Nenhum item'}"
        )
