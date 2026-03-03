from Model.Produto import Produto

class ProdutoController:
    def __init__(self):
        self.lista_produto = []

    def ler_id(self):
        id = int(input('\n A seguir, preencha o Código do Produto: '))

        return id

    def ler_produto(self):
        p = Produto()
        print(f"\n A seguir, preencha as informações para Cadastrar um Produto: ")
        p.id = int(input(' Código: '))
        p.nome = input(' Nome: ')
        p.preco = float(input(' Preço: '))
        p.qtde = int(input(' Quantidade: '))

        return p

    def ler_atualizacao(self, p: Produto):

        print(f"\n A seguir, preencha as informações para Atualizar um Produto: ")
        p.nome = input(' Nome: ')
        p.preco = float(input(' Preço: '))
        p.qtde = int(input(' Quantidade: '))

        return p

    def cadastrar_produto(self):
        produto = self.ler_produto()
        if self.buscar_produto(produto.id) is not None:
            return False
        self.lista_produto.append(produto)
        return True

    def listar_produto(self):
        return self.lista_produto

    def buscar_produto(self, id):
        for produto in self.lista_produto:
            if produto.id == id:
                return produto
        return None

    def atualizar_produto(self, produto: Produto):
        for i, produto_db in enumerate(self.lista_produto):
            if produto_db.id == produto.id:
                produto_db.nome = produto.nome
                produto_db.preco = produto.preco
                produto_db.qtde = produto.qtde
                self.lista_produto[i] = produto_db
                return True
        return False

    def excluir_produto(self, id):
        for i, produto in enumerate(self.lista_produto):
            if produto.id == id:
                del self.lista_produto[i]
                return True
        return False

    def gravar_lista_arquivo(self):
        with open("produtos.txt", "w") as arquivo:
            for produto in self.lista_produto:
                arquivo.write(
                    f"{produto.id},{produto.nome},{produto.preco},{produto.qtde}\n")

    def carregar_lista_arquivo(self):
        self.lista_produto = []
        with open("produtos.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                produto = Produto(dados[0], dados[1], dados[2], dados[3])
                self.lista_produto.append(produto)