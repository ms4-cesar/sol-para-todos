def escolher_tipo_moradia():
    while True:
        print("\nTipo de moradia:")
        print("1 - Casa")
        print("2 - Apartamento")
        print("3 - Área rural")
        print("4 - Outro")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            return "Casa"
        elif opcao == "2":
            return "Apartamento"
        elif opcao == "3":
            return "Área rural"
        elif opcao == "4":
            return "Outro"
        else:
            print("Opção inválida. Escolha uma opção de 1 a 4.")


def escolher_tipo_servico():
    while True:
        print("\nTipo de serviço:")
        print("1 - Cooperativa Solar")
        print("2 - Energia Solar Compartilhada")
        print("3 - Financiamento Solar")
        print("4 - Programa Público")
        print("5 - Instalação Solar")
        print("6 - Consultoria Energética")
        print("7 - Outro")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            return "Cooperativa Solar"
        elif opcao == "2":
            return "Energia Solar Compartilhada"
        elif opcao == "3":
            return "Financiamento Solar"
        elif opcao == "4":
            return "Programa Público"
        elif opcao == "5":
            return "Instalação Solar"
        elif opcao == "6":
            return "Consultoria Energética"
        elif opcao == "7":
            return "Outro"
        else:
            print("Opção inválida. Escolha uma opção de 1 a 7.")
