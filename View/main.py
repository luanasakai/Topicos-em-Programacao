from Controller.ClienteController import ClienteController
from Controller.ProdutoController import ProdutoController
from Controller.VendaController import VendaController

from View.menu_cliente import menu_cliente
from View.menu_produto import menu_produto
from View.menu_venda import menu_venda


def menu_principal():
    cliente_controller = ClienteController()
    produto_controller = ProdutoController()

    cliente_controller.carregar_lista_arquivo()
    produto_controller.carregar_lista_arquivo()

    venda_controller = VendaController(
        cliente_controller,
        produto_controller
    )

    while True:
        print("\n====== [SISTEMA DE VENDAS] ========")
        print("[1] - Clientes")
        print("[2] - Produtos")
        print("[3] - Vendas")
        print("[0] - Sair")
        print("\n===================================")
        op = input(" Escolha uma Opção: ")

        if op == "1":
            menu_cliente(cliente_controller)

        elif op == "2":
            menu_produto(produto_controller)

        elif op == "3":
            menu_venda(venda_controller)

        elif op == "0":
            break


if __name__ == "__main__":
    menu_principal()