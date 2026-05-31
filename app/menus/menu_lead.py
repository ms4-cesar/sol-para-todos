from services.lead_service import (listar_leads_parceiro,atualizar_status_lead)

def visualizar_leads(id_parceiro):
    try:
        leads = listar_leads_parceiro(id_parceiro)

        print("\n===== MEUS LEADS =====")

        if not leads:
            print("Nenhuma Lead encontrada.")
            return

        for lead in leads:
            print("\n------------------------------")
            print(f"ID do lead: {lead["id_lead"]}")
            print(f"Nome do lead: {lead["nome_usuario"]}")
            print(f"Status: {lead["status"]}")
            print(f"Data: {lead["created_at"]}")

        return leads

    except Exception as erro:
        print(f"Erro ao listar leads: {erro}")

def atualizar_lead(id_parceiro):

    print("\n===== ATUALIZAR LEAD =====")

    visualizar_leads(id_parceiro)
    print("0 -  voltar")

    opcao = int(input("Qual Lead você deseja atualizar ?"))
    status = ""
    if opcao != 0 :
        print("Para qual opção voçê gostaria de atualizar o lead")
        print(" 1 - Em andamento")
        print(" 2 - Fechado")
        print(" 3- Cancelado")
        print(" 0 -Voltar")
        opcao_status = int(input())
        if opcao_status == 1:
            status = "Em andamento"
        elif opcao_status == 2:
            status = "Fechado"
        elif opcao_status == 3:
            status ="Cancelado"
        else:
            return
    else:
        return

    try:
        atualizar_status_lead(
            opcao,
            status
        )
        print("Lead atualizado com sucesso.")

    except Exception as erro:
        print("Erro ao atualizar perfil:")
        print(erro)

def menu_lead(id_parceiro):
    while True:
        print("\n==============================")
        print("        MENU DE LEADS")
        print("==============================")
        print("1 - Visualizar meus leads")
        print("2 - Atualizar status do lead")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
           visualizar_leads(id_parceiro) 

        elif opcao == "2":
            atualizar_lead(id_parceiro)

        elif opcao == "0":
            print("Retornando ao menu principal...")
            break

        else:
            print("Opção inválida! Tente novamente.")

