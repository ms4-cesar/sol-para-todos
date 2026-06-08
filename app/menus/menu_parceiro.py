from services.parceiro_service import (
    buscar_parceiro_por_id,
    listar_enderecos_parceiro,
    listar_telefones_parceiro,
    atualizar_parceiro,
    excluir_parceiro
)

from services.lead_service import (
    listar_leads_parceiro,
    atualizar_status_lead,
    cancelar_lead_parceiro
)

from menus.opcoes import escolher_tipo_servico
from menus.ui import cabecalho, separador


def visualizar_perfil_parceiro(id_parceiro):
    parceiro = buscar_parceiro_por_id(id_parceiro)

    if parceiro is None:
        print("\n❌ Parceiro não encontrado.")
        return

    cabecalho("PERFIL DO PARCEIRO", "🏢")

    print(f"Empresa: {parceiro[1]}")
    print(f"E-mail: {parceiro[2]}")
    print(f"CNPJ: {parceiro[3]}")
    print(f"Tipo de serviço: {parceiro[4]}")

    enderecos = listar_enderecos_parceiro(id_parceiro)

    cabecalho("ENDEREÇOS", "📍")

    if not enderecos:
        print("Nenhum endereço cadastrado.")
    else:
        for endereco in enderecos:
            separador()
            print(f"Rua: {endereco[1]}, {endereco[2]}")
            print(f"Complemento: {endereco[3]}")
            print(f"CEP: {endereco[4]}")
            print(f"Bairro: {endereco[5]}")
            print(f"Cidade/UF: {endereco[6]} - {endereco[7]}")

    telefones = listar_telefones_parceiro(id_parceiro)

    cabecalho("TELEFONES", "📞")

    if not telefones:
        print("Nenhum telefone cadastrado.")
    else:
        for telefone in telefones:
            print(f"({telefone[1]}) {telefone[2]}")


def editar_perfil_parceiro(id_parceiro):
    parceiro = buscar_parceiro_por_id(id_parceiro)

    if parceiro is None:
        print("\n❌ Parceiro não encontrado.")
        return

    cabecalho("EDITAR PERFIL DO PARCEIRO", "✏️")

    print(f"Nome atual da empresa: {parceiro[1]}")
    novo_nome = input("Novo nome da empresa (pressione Enter para manter): ")

    print(f"\nTipo de serviço atual: {parceiro[4]}")
    alterar_servico = input("Deseja alterar o tipo de serviço? (s/n): ")

    if alterar_servico.strip().lower() == "s":
        novo_tipo_servico = escolher_tipo_servico()
    else:
        novo_tipo_servico = ""

    nome_empresa = novo_nome if novo_nome.strip() else parceiro[1]
    tipo_servico = novo_tipo_servico if novo_tipo_servico.strip() else parceiro[4]

    try:
        atualizar_parceiro(
            id_parceiro,
            nome_empresa,
            tipo_servico
        )

        print("\n✅ Perfil do parceiro atualizado com sucesso.")

    except Exception as erro:
        print("\n❌ Erro ao atualizar parceiro:")
        print(erro)


def deletar_perfil_parceiro(id_parceiro):
    cabecalho("EXCLUIR PERFIL DO PARCEIRO", "⚠️")

    confirmacao = input("Tem certeza que deseja excluir o perfil da empresa? (s/n): ")

    if confirmacao.strip().lower() != "s":
        print("\nOperação cancelada.")
        return False

    try:
        excluir_parceiro(id_parceiro)
        print("\n✅ Perfil do parceiro excluído com sucesso.")
        return True

    except Exception as erro:
        print("\n❌ Erro ao excluir parceiro:")
        print(erro)
        return False


def visualizar_leads_recebidos(id_parceiro):
    leads = listar_leads_parceiro(id_parceiro)

    cabecalho("LEADS RECEBIDOS", "🤝")

    if not leads:
        print("Nenhum lead recebido.")
        return

    for lead in leads:
        separador()
        print(f"ID do lead: {lead[0]}")
        print(f"Cliente: {lead[1]} {lead[2]}")
        print(f"E-mail do cliente: {lead[3]}")
        print(f"Solução: {lead[4]}")
        print(f"Status: {lead[5]}")
        print(f"Data: {lead[6]}")


def escolher_status_lead():
    while True:
        cabecalho("NOVO STATUS DO LEAD", "📌")

        print("1 - Novo")
        print("2 - Em andamento")
        print("3 - Fechado")
        print("4 - Cancelado")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            return "Novo"
        elif opcao == "2":
            return "Em andamento"
        elif opcao == "3":
            return "Fechado"
        elif opcao == "4":
            return "Cancelado"
        else:
            print("\n❌ Opção inválida. Escolha uma opção de 1 a 4.")


def atualizar_status_lead_parceiro(id_parceiro):
    cabecalho("ATUALIZAR STATUS DO LEAD", "🔄")

    leads = listar_leads_parceiro(id_parceiro)

    if not leads:
        print("Nenhum lead recebido para atualizar.")
        return

    visualizar_leads_recebidos(id_parceiro)

    try:
        id_lead = int(input("\nDigite o ID do lead que deseja atualizar: "))

        ids_leads_disponiveis = [lead[0] for lead in leads]

        if id_lead not in ids_leads_disponiveis:
            print("\n❌ Lead inválido. Escolha apenas um lead listado.")
            return

        novo_status = escolher_status_lead()

        sucesso = atualizar_status_lead(
            id_lead,
            id_parceiro,
            novo_status
        )

        if sucesso:
            print("\n✅ Status do lead atualizado com sucesso.")
        else:
            print("\n❌ Lead não encontrado para este parceiro.")

    except ValueError:
        print("\n❌ Erro: informe um ID válido.")

    except Exception as erro:
        print("\n❌ Erro ao atualizar status do lead:")
        print(erro)


def cancelar_lead_do_parceiro(id_parceiro):
    cabecalho("CANCELAR LEAD", "⚠️")

    leads = listar_leads_parceiro(id_parceiro)

    if not leads:
        print("Nenhum lead recebido para cancelar.")
        return

    visualizar_leads_recebidos(id_parceiro)

    try:
        id_lead = int(input("\nDigite o ID do lead que deseja cancelar: "))

        ids_leads_disponiveis = [lead[0] for lead in leads]

        if id_lead not in ids_leads_disponiveis:
            print("\n❌ Lead inválido. Escolha apenas um lead listado.")
            return

        confirmacao = input("Tem certeza que deseja cancelar este lead? (s/n): ")

        if confirmacao.strip().lower() != "s":
            print("\nOperação cancelada.")
            return

        sucesso = cancelar_lead_parceiro(id_lead, id_parceiro)

        if sucesso:
            print("\n✅ Lead cancelado com sucesso.")
        else:
            print("\n❌ Lead não encontrado para este parceiro.")

    except ValueError:
        print("\n❌ Erro: informe um ID válido.")

    except Exception as erro:
        print("\n❌ Erro ao cancelar lead:")
        print(erro)


def menu_parceiro(parceiro_logado):
    while True:
        cabecalho("MENU DO PARCEIRO", "🏢")

        print("1 - Visualizar perfil da empresa")
        print("2 - Atualizar perfil da empresa")
        print("3 - Visualizar leads recebidos")
        print("4 - Atualizar status de um lead")
        print("5 - Cancelar lead")
        print("6 - Excluir perfil da empresa")
        print("0 - Sair da conta")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            visualizar_perfil_parceiro(parceiro_logado["id_parceiro"])

        elif opcao == "2":
            editar_perfil_parceiro(parceiro_logado["id_parceiro"])

        elif opcao == "3":
            visualizar_leads_recebidos(parceiro_logado["id_parceiro"])

        elif opcao == "4":
            atualizar_status_lead_parceiro(parceiro_logado["id_parceiro"])

        elif opcao == "5":
            cancelar_lead_do_parceiro(parceiro_logado["id_parceiro"])

        elif opcao == "6":
            perfil_excluido = deletar_perfil_parceiro(parceiro_logado["id_parceiro"])

            if perfil_excluido:
                break

        elif opcao == "0":
            print("\nSaindo da conta.")
            break

        else:
            print("\n❌ Opção inválida.")