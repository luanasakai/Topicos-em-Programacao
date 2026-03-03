from Model import Venda

class VendaController:
    def __init__(self):
        self.lista_venda = []

    def cadastrar_venda(self, venda: Venda):
        if self.buscar_venda(venda.id) is not None:
            return False
        self.lista_venda.append(venda)
        return True

    def listar_venda(self):
        return self.lista_venda

    def buscar_venda(self, id):
        for venda in self.lista_venda:
            if venda.id == id:
                return venda
        return None

    def atualizar_venda(self, venda: Venda):
        for i, venda_db in enumerate(self.lista_venda):
            if venda_db.id == venda.id:
                venda_db.data = venda.data
                venda_db.valor_total = venda.valor_total
                venda_db.itens = venda.itens
                self.lista_venda[i] = venda_db
                return True
        return False

    def excluir_venda(self, id):
        for i, venda in enumerate(self.lista_venda):
            if venda.id == id:
                del self.lista_venda[i]
                return True
        return False

    def gravar_lista_arquivo(self):
        with open("venda.txt", "w") as arquivo:
            for venda in self.lista_venda:
                arquivo.write(
                    f"{venda.id},{venda.data},{venda.valor_total},{venda.cliente},{venda.itens}\n")

    def carregar_lista_arquivo(self):
        self.lista_venda = []
        with open("venda.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                venda = Venda(dados[0], dados[1], dados[2], dados[3], dados[4])
                self.lista_venda.append(venda)