from Controller.VendaController import VendaController

def menu_venda(controller):

    while True:
        print("\n=============== [MENU VENDA] ===============")
        print("[CARRINHO]")
        print("  [1] - Criar Nova Venda (Carrinho)")
        print("  [2] - Excluir Venda")
        print("  [3] - Buscar Venda")
        print("  [4] - Listar Vendas")

        print("\n[ARQUIVO TEXTO]")
        print("  [5] - Gravar Lista de Vendas")
        print("  [6] - Carregar Lista de Vendas")

        print("\n  [0] - SAIR")
        print("============================================")

        try:
            op = int(input("\nA seguir, insira uma opção: "))
        except ValueError:
            print("Opção inválida!")
            continue

        if op == 0:
            print("Saindo do programa...")
            break

        elif op == 1:
            venda = controller.ler_venda()

            if venda:
                if controller.cadastrar_venda(venda):
                    print("\nVenda cadastrada com sucesso!")
                else:
                    print("\n❌ Venda já existe!")

        elif op == 2:
            resp = controller.excluir_venda(controller.ler_id())

            if resp:
                print("\nVenda excluída!")
            else:
                print("\n❌ Venda não encontrada!")

        elif op == 3:
            venda = controller.buscar_venda(controller.ler_id())

            if venda:
                print("\nVenda encontrada:")
                print(venda)
            else:
                print("\n❌ Venda não encontrada!")

        elif op == 4:
            lista = controller.listar_venda()

            if not lista:
                print("\nLista vazia!")
            else:
                print("\n===== VENDAS =====")
                for v in lista:
                    print(v)

        elif op == 5:
            controller.gravar_lista_arquivo()
            print("\n✅ Lista gravada com sucesso!")

        elif op == 6:
            controller.carregar_lista_arquivo()
            print("\n✅ Lista carregada com sucesso!")

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_venda()