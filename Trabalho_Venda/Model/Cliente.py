class Cliente:

    def __init__(self, id=0, nome="", endereco="", cidade="", uf="", cep=""):
        self._id = id
        self._nome = nome
        self._endereco = endereco
        self._cidade = cidade
        self._uf = uf
        self._cep = cep

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
        return self._cidade

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
        return (f"\nCódigo Cliente: {self.id} "
                f"\nNome: {self.nome} "
                f"\nEndereco: {self.endereco} "
                f"\nCidade: {self.cidade} "
                f"\nUF: {self.uf} "
                f"\nCEP: {self.cep}")