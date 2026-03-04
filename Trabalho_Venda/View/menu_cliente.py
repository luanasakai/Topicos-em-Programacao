from Controller.ClienteController import ClienteController

def menu_cliente(controller):

    while True:
        print(f"\n=============== [MENU CLIENTE] ===============")
        print(f"[OPERAÇÕES BÁSICAS]: ")
        print(f"  [1] - Cadastrar Cliente.")
        print(f"  [2] - Atualizar Cliente.")
        print(f"  [3] - Excluir Cliente.")
        print(f"  [4] - Buscar Cliente.")
        print(f"  [5] - Listar Clientes.")

        print(f"\n[ARQUIVO TEXTO]: ")
        print(f"  [6] - Gravar Lista de Clientes.")
        print(f"  [7] - Carregar Lista de Clientes.")

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
            resp = controller.cadastrar_cliente(controller.ler_cliente())

            if resp:
                print("\n Cliente Cadastrado!")
            else:
                print("\n ERRO, Cliente já existe!")

        elif op == 2:
            cliente = controller.buscar_cliente(controller.ler_id())

            if cliente:
                resp = controller.atualizar_cliente(controller.ler_atualizacao(cliente))
                if resp:
                    print("\n Cliente Atualizado!")
                else:
                    print("\n ERRO, Cliente não existe!")
            else:
                print("\n ERRO, Cliente não existe!")

        elif op == 3:
            resp = controller.excluir_cliente(controller.ler_id())

            if resp:
                print("\n Cliente Excluido!")
            else:
                print("\n ERRO, Cliente não Existe!")

        elif op == 4:
            cliente = controller.buscar_cliente(controller.ler_id())

            if cliente:
                print(cliente)
            else:
                print("\n ERRO, Cliente não Existe!")

        elif op == 5:
            lista = controller.listar_clientes()

            if not lista:
                print("\n Lista Vazia! Cadastre um Cliente ou Carregue um Arquivo.")
            else:
                for c in lista:
                    print(c)

        elif op == 6:
            controller.gravar_lista_arquivo()
            print("\n Lista de Clientes Gravada com Sucesso!")

        elif op == 7:
            controller.carregar_lista_arquivo()
            print("\n Lista de Clientes Carregada com Sucesso!")

if __name__ == "__main__":
    menu_cliente()