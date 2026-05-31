from services.lead_service import listar_leads_parceiro
from services.simulacao_service import(listar_simulacoes)

def visualizar_leads():
    try:
        leads = listar_leads_parceiro()

        if not leads:
            print("Nenhum lead encontrado.")
            return

        for lead in leads:
            print(lead)

    except Exception as erro:
        print(f"Erro ao listar leads: {erro}")

def visualizar_simulacoes():
    simulacoes = listar_simulacoes()

    print("\n===== MINHAS SIMULAÇÕES =====")

    if not simulacoes:
        print("Nenhuma simulação encontrada.")
        return

    for simulacao in simulacoes:
        print("\n------------------------------")
        print(f"ID da simulação: {simulacao[0]}")
        print(f"Consumo mensal: {simulacao[1]} kWh")
        print(f"Valor da fatura: R$ {simulacao[2]}")
        print(f"Economia estimada geral: R$ {simulacao[3]}")
        print(f"Data: {simulacao[4]}")

def menu_lead():
    while True:
        print("\n==============================")
        print("        MENU DE LEADS")
        print("==============================")
        print("1 - Registrar interesse (Lead)")
        print("2 - Visualizar meus leads")
        print("3 - Atualizar status do lead")
        print("4 - Cancelar lead")
        print("5 - visualizar simulaçoes")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("Registrar novo lead")

        elif opcao == "2":
           visualizar_leads() 

        elif opcao == "3":
            print("Atualizar status do lead") 

        elif opcao == "4":
            print("Cancelar lead")

        elif opcao == "5":
            visualizar_simulacoes()

        elif opcao == "0":
            print("Retornando ao menu principal...")
            break

        else:
            print("Opção inválida! Tente novamente.")