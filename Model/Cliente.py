class Cliente:

    def __init__(self):
        self._id= 0
        self._nome = ""
        self._endereco = ""
        self._cidade = ""
        self._uf = ""
        self._cep = ""

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
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def cidade(self):
        return self._qtde

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, uf):
        self._uf = uf

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, cep):
        self._cep = cep

    def __str__(self):
        return (f"Código Cliente: {self.id}, "
                f"Nome: {self.nome}, "
                f"Endereco: {self.endereco}, "
                f"Cidade: {self.cidade}, "
                f"UF: {self.uf}, "
                f"CEP: {self.cep}")