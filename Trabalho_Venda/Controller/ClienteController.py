from Model.Cliente import Cliente
from util.persistir_pasta_dados import caminho_arquivo
import os

class ClienteController:
    def __init__(self):
        self.lista_clientes = []

    def ler_id(self):
        id = int(input('\n A seguir, preencha o Código do Cliente: '))

        return id

    def ler_cliente(self):
        c = Cliente()
        print(f"\n A seguir, preencha as informações para Cadastrar um Cliente: ")
        c.id = int(input(' Código: '))
        c.nome = input(' Nome: ')
        c.endereco = input(' Endereço: ')
        c.cidade = input(' Cidade: ')
        c.uf = input(' UF: ')
        c.cep = input(' CEP: ')

        return c

    def ler_atualizacao(self, c: Cliente):

        print(f"\n A seguir, preencha as informações para Atualizar um Cliente: ")
        c.nome = input(' Nome: ')
        c.cidade = input(' Cidade: ')
        c.uf = input(' UF: ')
        c.cep = input(' CEP: ')

        return c

    def cadastrar_cliente(self, cliente: Cliente):
        if self.buscar_cliente(cliente.id) is not None:
            return False
        self.lista_clientes.append(cliente)
        return True

    def listar_clientes(self):
        return self.lista_clientes

    def buscar_cliente(self, id):
        for cliente in self.lista_clientes:
            if cliente.id == id:
                return cliente
        return None

    def atualizar_cliente(self, cliente: Cliente):
        for i, cliente_db in enumerate(self.lista_clientes):
            if cliente_db.id == cliente.id:
                cliente_db.nome = cliente.nome
                cliente_db.endereco = cliente.endereco
                cliente_db.cidade = cliente.cidade
                cliente_db.uf = cliente.uf
                cliente_db.cep = cliente.cep
                self.lista_clientes[i] = cliente_db
                return True
        return False

    def excluir_cliente(self, id):
        for i, cliente in enumerate(self.lista_clientes):
            if cliente.id == id:
                del self.lista_clientes[i]
                return True
        return False

    def gravar_lista_arquivo(self):
        with open(caminho_arquivo("clientes.txt"), "w") as arquivo:
            for cliente in self.lista_clientes:
                arquivo.write(
                    f"{cliente.id},{cliente.nome},{cliente.endereco},{cliente.cidade},{cliente.uf},{cliente.cep}\n")

    def carregar_lista_arquivo(self):
        self.lista_clientes = []

        caminho = caminho_arquivo("clientes.txt")

        if not os.path.exists(caminho):
            print("Arquivo não encontrado!")
            return

        with open(caminho, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                cliente = Cliente(
                    int(dados[0]),
                    dados[1],
                    dados[2],
                    dados[3],
                    dados[4],
                    dados[5]
                )
                self.lista_clientes.append(cliente)