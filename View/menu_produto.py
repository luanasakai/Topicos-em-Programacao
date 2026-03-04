from Controller.ProdutoController import ProdutoController

def menu_produto(controller):

    while True:
        print(f"\n=============== [MENU PRODUTO] ===============")
        print(f"[OPERAÇÕES BÁSICAS]: ")
        print(f"  [1] - Cadastrar Produto.")
        print(f"  [2] - Atualizar Produto.")
        print(f"  [3] - Excluir Produto.")
        print(f"  [4] - Buscar Produto.")
        print(f"  [5] - Listar Produtos.")

        print(f"\n[ARQUIVO TEXTO]: ")
        print(f"  [6] - Gravar Lista de Produtos.")
        print(f"  [7] - Carregar Lista de Produtos.")

        print(f"  [0] - SAIR.")
        print(f"============================================== ")

        try:
            op = int(input(' A seguir, insira uma opção: '))
        except ValueError:
            print("Opção inválida!")
            continue

        if op == 0:
            print("Saindo do Programa...")
            break
        elif op == 1:
            resp = controller.cadastrar_produto()

            if resp:
                print("\n Produto Cadastrado!")
            else:
                print("\n ERRO, Produto já existe!")

        elif op == 2:
            produto = controller.buscar_produto(controller.ler_id())

            if produto:
                resp = controller.atualizar_produto(controller.ler_atualizacao(produto))
                if resp:
                    print("\n Produto Atualizado!")
                else:
                    print("\n ERRO, Produto não existe!")
            else:
                print("\n ERRO, Produto não existe!")

        elif op == 3:
            resp = controller.excluir_produto(controller.ler_id())

            if resp:
                print("\n Produto Excluido!")
            else:
                print("\n ERRO, Produto não Existe!")

        elif op == 4:
            produto = controller.buscar_produto(controller.ler_id())

            if produto:
                print(produto)
            else:
                print("\n ERRO, Produto não Existe!")

        elif op == 5:
            lista = controller.listar_produto()

            if not lista:
                print("\n Lista Vazia! Cadastre um Produto ou Carregue um Arquivo.")
            else:
                for p in lista:
                    print(p)

        elif op == 6:
            controller.gravar_lista_arquivo()
            print("\n Lista de Produtos Gravada com Sucesso!")

        elif op == 7:
            controller.carregar_lista_arquivo()
            print("\n Lista de Produtos Carregada com Sucesso!")

if __name__ == "__main__":
    menu_produto()