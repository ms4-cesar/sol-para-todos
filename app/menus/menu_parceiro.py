from services.parceiro_service import (
    buscar_parceiro_por_id,
    atualizar_parceiro,
    excluir_parceiro
)
from menus.menu_lead import menu_lead


def visualizar_perfil(id_parceiro):
    parceiro = buscar_parceiro_por_id(id_parceiro)

    if parceiro is None:
        print("Empresa não encontrada.")
        return

    print("\n===== MEU PERFIL =====")
    print(f"Nome da empresa: {parceiro[1]}")
    print(f"E-mail: {parceiro[2]}")
    print(f"CNPJ: {parceiro[4]}")
    print(f"Tipo de serviço: R$ {parceiro[5]}")

def editar_perfil(id_parceiro):
    parceiro = buscar_parceiro_por_id(id_parceiro)

    if parceiro is None:
        print("Parceiro não encontrado.")
        return

    print("\n===== EDITAR PERFIL =====")

    print(f"Nome atual da empresa: {parceiro[1]}")
    novo_nome = input("Novo nome (pressione Enter para manter): ")

    print(f"Email atual: {parceiro[2]}")
    novo_email = input("Novo email (pressione Enter para manter): ")

    print(f"Tipo de serviço atual: R$ {parceiro[5]}")
    novo_tipo_de_servico = input("Novo tipo de serviço (pressione Enter para manter): ")


    nome_empresa = novo_nome if novo_nome.strip() else parceiro[1]
    email = novo_email if novo_email.strip() else parceiro[2]
    tipo_servico = novo_tipo_de_servico if novo_tipo_de_servico.strip() else parceiro[5]

    try:
        atualizar_parceiro(
            id_parceiro,
            nome_empresa,
            email,
            tipo_servico
        )
        print("Perfil atualizado com sucesso.")

    except Exception as erro:
        print("Erro ao atualizar perfil:")
        print(erro)

def deletar_parceiro(id_parceiro):
    confirmacao = input("Tem certeza que deseja excluir sua conta? (s/n): ")

    if confirmacao.lower() != "s":
        print("Operação cancelada.")
        return False

    try:
        excluir_parceiro(id_parceiro)
        print("Conta excluída com sucesso.")
        return True

    except Exception as erro:
        print("Erro ao excluir conta:")
        print(erro)
        return False
    
def menu_parceiro(parceiro_logado):
    while True:
        print("\n==============================")
        print("        MENU DO PARCEIRO")
        print("==============================")
        print("1 - Visualizar meu perfil")
        print("2 - Atualizar meu perfil")
        print("3 - Excluir minha conta")
        print("4 - Gerenciar Leads")

        print("0 - Sair da conta")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visualizar_perfil(parceiro_logado["id_parceiro"])

        elif opcao == "2":
            editar_perfil(parceiro_logado["id_parceiro"])
        
        elif opcao == "3":
            parceiro_excluido = deletar_parceiro(parceiro_logado["id_parceiro"])

            if parceiro_excluido:
                break
        elif opcao == "4":
            menu_lead(parceiro_logado["id_parceiro"])

        elif opcao == "0":
            print("Saindo da conta.")
            break

        else:
            print("Opção inválida.")