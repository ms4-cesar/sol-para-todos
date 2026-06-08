from app.menus.ui import cabecalho


def escolher_tipo_moradia():
    while True:
        cabecalho("TIPO DE MORADIA", "🏠")

        print("1 - Casa")
        print("2 - Apartamento")
        print("3 - Área rural")
        print("4 - Outro")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            return "Casa"
        elif opcao == "2":
            return "Apartamento"
        elif opcao == "3":
            return "Área rural"
        elif opcao == "4":
            return "Outro"
        else:
            print("\n❌ Opção inválida. Escolha uma opção de 1 a 4.")


def escolher_tipo_servico():
    while True:
        cabecalho("TIPO DE SERVIÇO", "💡")

        print("1 - Cooperativa Solar")
        print("2 - Energia Solar Compartilhada")
        print("3 - Financiamento Solar")
        print("4 - Programa Público ou Social")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            return "Cooperativa Solar"
        elif opcao == "2":
            return "Energia Solar Compartilhada"
        elif opcao == "3":
            return "Financiamento Solar"
        elif opcao == "4":
            return "Programa Público ou Social"
        else:
            print("\n❌ Opção inválida. Escolha uma opção de 1 a 4.")