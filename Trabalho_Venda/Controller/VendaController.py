from Model.Venda import Venda
from Model.ItemVenda import ItemVenda
from Model.Produto import Produto
from Controller.ClienteController import ClienteController
from Controller.ProdutoController import ProdutoController

class VendaController:
    def __init__(self, cliente_controller, produto_controller):
        self.lista_venda = []
        self.cc = cliente_controller
        self.pv = produto_controller

    def ler_id(self):
        id = int(input('\n A seguir, preencha o Código de Venda: '))

        return id

    def ler_venda(self):
        v = Venda()

        print("\nCadastro de Venda")

        v.id = int(input("Código: "))
        v.data = input("Data: ")

        c = self.cc.buscar_cliente(self.cc.ler_id())
        if not c:
            print("Cliente não cadastrado!")
            return None

        v.cliente = c
        v.itens = self.criar_carrinho()
        v.valor_total = sum(item.subtotal for item in v.itens)

        print(f"\nTotal da venda: R$ {v.valor_total:.2f}")

        return v

    def criar_carrinho(self):
        itens = []

        while True:
            print("\n===== CARRINHO =====")
            print("1 - Adicionar produto")
            print("2 - Alterar quantidade")
            print("3 - Finalizar carrinho")

            total = sum(item.subtotal for item in itens)
            print(f"\nTotal parcial: R$ {total:.2f}")

            op = input("Escolha: ")

            if op == "1":
                produtos = self.pv.listar_produto()

                if not produtos:
                    print("Nenhum produto cadastrado!")
                    continue

                for p in produtos:
                    print(p)

                produto = self.pv.buscar_produto(self.pv.ler_id())

                if produto:
                    qtde = int(input("Quantidade: "))

                    item = ItemVenda()
                    item.produto = produto
                    item.quantidade = qtde
                    item.subtotal = produto.preco * qtde

                    itens.append(item)
                    print(" Produto adicionado!")

            elif op == "2":
                itens = self.alterar_quantidade_item(itens)

            elif op == "3":
                if not itens:
                    print("\n❌ Não é possível finalizar um carrinho vazio!")
                    continue
                break

            else:
                print("Opção inválida!")

        return itens

    def remover_item_carrinho(self, itens):
        if not itens:
            print("\nCarrinho vazio!")
            return itens

        print("\nItens no carrinho:")

        for i, item in enumerate(itens, start=1):
            print(f"{i} - {item.produto.nome} | "
                  f"Qtd: {item.quantidade} | "
                  f"Subtotal: R$ {item.subtotal:.2f}")

        try:
            op = int(input("\nDigite o número do item para remover (0 cancelar): "))

            if op == 0:
                return itens

            if 1 <= op <= len(itens):
                removido = itens.pop(op - 1)
                print(f"✅ {removido.produto.nome} removido do carrinho!")
            else:
                print("Opção inválida!")

        except ValueError:
            print("Entrada inválida!")

        return itens

    def alterar_quantidade_item(self, itens):
        if not itens:
            print("\nCarrinho vazio!")
            return itens

        print("\nItens no carrinho:")
        for i, item in enumerate(itens, start=1):
            print(f"{i} - {item.produto.nome} | "
                  f"Qtd: {item.quantidade} | "
                  f"Subtotal: R$ {item.subtotal:.2f}")

        try:
            op = int(input("\nEscolha o item para alterar (0 cancelar): "))

            if op == 0:
                return itens

            if 1 <= op <= len(itens):
                nova_qtde = int(input("Nova quantidade (0 remove item): "))

                item = itens[op - 1]

                if nova_qtde == 0:
                    itens.pop(op - 1)
                    print("Item removido do carrinho!")
                else:
                    item.quantidade = nova_qtde
                    item.subtotal = item.produto.preco * nova_qtde
                    print("Quantidade atualizada!")

            else:
                print("Opção inválida!")

        except ValueError:
            print("Entrada inválida!")

        return itens

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
                    f"{venda.id},{venda.data},{venda.valor_total},{venda.cliente.id},{venda.itens}\n")

    def carregar_lista_arquivo(self):
        self.lista_venda = []
        with open("venda.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                id_venda = int(dados[0])
                data = dados[1]
                valor = float(dados[2])
                id_cliente = int(dados[3])

                cliente = self.cc.buscar_cliente(id_cliente)

                venda = Venda(
                    id_venda,
                    data,
                    valor,
                    cliente,
                    []
                )

                self.lista_venda.append(venda)