from app.menus.opcoes import escolher_tipo_moradia
from app.menus.validacoes import solicitar_renda_opcional
from app.services.lead_service import (
    criar_lead,
    listar_leads_usuario,
    cancelar_lead_usuario
)

from app.services.simulacao_service import (
    criar_simulacao,
    listar_simulacoes_usuario,
    excluir_simulacao
)

from app.services.usuario_service import (
    buscar_usuario_por_id,
    atualizar_usuario,
    excluir_usuario,
    buscar_endereco_usuario,
    listar_telefones_usuario
)

from app.services.solucao_service import (
    listar_solucoes,
    buscar_solucao_por_id,
    listar_parceiros_por_solucao_e_usuario
)

def visualizar_perfil(id_usuario):
    usuario = buscar_usuario_por_id(id_usuario)

    if usuario is None:
        print("Usuário não encontrado.")
        return

    print("\n===== MEU PERFIL =====")
    print(f"Nome: {usuario[1]} {usuario[2]}")
    print(f"E-mail: {usuario[3]}")
    print(f"CPF: {usuario[4]}")
    print(f"Renda: R$ {usuario[5]}")
    print(f"Tipo de moradia: {usuario[6]}")

    endereco = buscar_endereco_usuario(id_usuario)

    print("\nEndereço:")
    if endereco is None:
        print("Nenhum endereço cadastrado.")
    else:
        print(f"Rua: {endereco[0]}, {endereco[1]}")
        print(f"Complemento: {endereco[2]}")
        print(f"CEP: {endereco[3]}")
        print(f"Bairro: {endereco[4]}")
        print(f"Cidade/UF: {endereco[5]} - {endereco[6]}")

    telefones = listar_telefones_usuario(id_usuario)

    print("\nTelefones:")
    if not telefones:
        print("Nenhum telefone cadastrado.")
    else:
        for telefone in telefones:
            print(f"({telefone[0]}) {telefone[1]}")


def editar_perfil(id_usuario):
    usuario = buscar_usuario_por_id(id_usuario)

    if usuario is None:
        print("Usuário não encontrado.")
        return

    print("\n===== EDITAR PERFIL =====")

    print(f"Nome atual: {usuario[1]}")
    novo_nome = input("Novo nome (pressione Enter para manter): ")

    print(f"Sobrenome atual: {usuario[2]}")
    novo_sobrenome = input("Novo sobrenome (pressione Enter para manter): ")

    print(f"Renda atual: R$ {usuario[5]}")
    nova_renda = solicitar_renda_opcional("Nova renda (pressione Enter para manter): ")

    print(f"Tipo de moradia atual: {usuario[6]}")
    alterar_moradia = input("Deseja alterar o tipo de moradia? (s/n): ")

    if alterar_moradia.strip().lower() == "s":
        novo_tipo_moradia = escolher_tipo_moradia()
    else:
        novo_tipo_moradia = ""

    try:
        nome = novo_nome if novo_nome.strip() else usuario[1]
        sobrenome = novo_sobrenome if novo_sobrenome.strip() else usuario[2]

        renda = nova_renda if nova_renda is not None else usuario[5]

        tipo_moradia = novo_tipo_moradia if novo_tipo_moradia.strip() else usuario[6]

        atualizar_usuario(
            id_usuario,
            nome,
            sobrenome,
            renda,
            tipo_moradia
        )

        print("Perfil atualizado com sucesso.")

    except ValueError:
        print("Erro: informe um valor numérico válido para a renda.")

    except Exception as erro:
        print("Erro ao atualizar perfil:")
        print(erro)


def deletar_conta(id_usuario):
    confirmacao = input("Tem certeza que deseja excluir sua conta? (s/n): ")

    if confirmacao.strip().lower() != "s":
        print("Operação cancelada.")
        return False

    try:
        excluir_usuario(id_usuario)
        print("Conta excluída com sucesso.")
        return True

    except Exception as erro:
        print("Erro ao excluir conta:")
        print(erro)
        return False


def fazer_simulacao(id_usuario):
    print("\n===== FAZER SIMULAÇÃO =====")

    try:
        consumo_mensal = float(input("Informe seu consumo mensal em kWh: "))
        valor_fatura = float(input("Informe o valor médio da sua conta de luz: R$ "))

        if consumo_mensal < 0 or valor_fatura < 0:
            print("Erro: consumo e valor da fatura não podem ser negativos.")
            return

        simulacao = criar_simulacao(
            id_usuario,
            consumo_mensal,
            valor_fatura
        )

        print("\nSimulação realizada com sucesso.")
        print(f"Consumo mensal informado: {simulacao['consumo_mensal']} kWh")
        print(f"Valor atual da fatura: R$ {simulacao['valor_fatura']:.2f}")

        print("\n===== COMPARAÇÃO DE SOLUÇÕES =====")
        print(
            f"{'Opção':<30} "
            f"{'Custo estimado':<18} "
            f"{'Economia':<15} "
            f"{'Prazo':<15}"
        )
        print("-" * 85)

        for item in simulacao["comparacao"]:
            print(
                f"{item['solucao']:<30} "
                f"R$ {item['custo_estimado']:<15.2f} "
                f"R$ {item['economia']:<12.2f} "
                f"{item['prazo']:<15}"
            )

        print("\nObservações:")
        for item in simulacao["comparacao"]:
            print(f"- {item['solucao']}: {item['observacao']}")

    except ValueError:
        print("Erro: informe valores numéricos válidos.")

    except Exception as erro:
        print("Erro ao realizar simulação:")
        print(erro)


def visualizar_simulacoes(id_usuario):
    simulacoes = listar_simulacoes_usuario(id_usuario)

    print("\n===== MINHAS SIMULAÇÕES =====")

    if not simulacoes:
        print("Nenhuma simulação encontrada.")
        return

    for simulacao in simulacoes:
        print("\n------------------------------")
        print(f"ID da simulação: {simulacao[0]}")
        print(f"Consumo mensal: {simulacao[1]} kWh")
        print(f"Valor da fatura: R$ {simulacao[2]}")
        print(f"Economia base estimada: R$ {simulacao[3]}")
        print(f"Data: {simulacao[4]}")


def deletar_simulacao(id_usuario):
    print("\n===== EXCLUIR SIMULAÇÃO =====")

    simulacoes = listar_simulacoes_usuario(id_usuario)

    if not simulacoes:
        print("Nenhuma simulação encontrada para excluir.")
        return

    visualizar_simulacoes(id_usuario)

    try:
        id_simulacao = int(input("\nInforme o ID da simulação que deseja excluir: "))

        confirmacao = input("Tem certeza que deseja excluir esta simulação? (s/n): ")

        if confirmacao.strip().lower() != "s":
            print("Operação cancelada.")
            return

        sucesso = excluir_simulacao(id_simulacao, id_usuario)

        if sucesso:
            print("Simulação excluída com sucesso.")
        else:
            print("Simulação não encontrada para este usuário.")

    except ValueError:
        print("Erro: informe um ID válido.")

    except Exception as erro:
        print("Erro ao excluir simulação:")
        print(erro)


def menu_usuario(usuario_logado):
    while True:
        print("\n==============================")
        print("        MENU DO USUÁRIO")
        print("==============================")
        print("1 - Visualizar meu perfil")
        print("2 - Atualizar meu perfil")
        print("3 - Fazer simulação")
        print("4 - Visualizar minhas simulações")
        print("5 - Excluir simulação")
        print("6 - Visualizar soluções disponíveis")
        print("7 - Visualizar meus interesses")
        print("8 - Cancelar interesse")
        print("9 - Excluir minha conta")
        print("0 - Sair da conta")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visualizar_perfil(usuario_logado["id_usuario"])

        elif opcao == "2":
            editar_perfil(usuario_logado["id_usuario"])

        elif opcao == "3":
            fazer_simulacao(usuario_logado["id_usuario"])

        elif opcao == "4":
            visualizar_simulacoes(usuario_logado["id_usuario"])

        elif opcao == "5":
            deletar_simulacao(usuario_logado["id_usuario"])

        elif opcao == "6":
            visualizar_solucoes_disponiveis(usuario_logado["id_usuario"])

        elif opcao == "7":
            visualizar_meus_interesses(usuario_logado["id_usuario"])

        elif opcao == "8":
            cancelar_interesse(usuario_logado["id_usuario"])

        elif opcao == "9":
            conta_excluida = deletar_conta(usuario_logado["id_usuario"])

            if conta_excluida:
                break

        elif opcao == "0":
            print("Saindo da conta.")
            break

        else:
            print("Opção inválida.")

def visualizar_solucoes_disponiveis(id_usuario):
    solucoes = listar_solucoes()

    print("\n===== SOLUÇÕES DISPONÍVEIS =====")

    if not solucoes:
        print("Nenhuma solução cadastrada.")
        return

    for solucao in solucoes:
        print(f"{solucao[0]} - {solucao[1]}")

    try:
        id_solucao = int(input("\nDigite o ID da solução para ver detalhes ou 0 para voltar: "))

        if id_solucao == 0:
            return

        solucao = buscar_solucao_por_id(id_solucao)

        if solucao is None:
            print("Solução não encontrada.")
            return

        print("\n===== DETALHES DA SOLUÇÃO =====")
        print(f"Tipo: {solucao[1]}")
        print(f"Descrição: {solucao[2]}")
        print(f"Requisitos: {solucao[3]}")

        parceiros = listar_parceiros_por_solucao_e_usuario(id_solucao, id_usuario)

        print("\n===== PARCEIROS COMPATÍVEIS =====")

        if parceiros is None:
            print("Não foi possível buscar parceiros porque o usuário não possui endereço cadastrado.")
            return

        if not parceiros:
            print("Nenhum parceiro encontrado para essa solução na sua região.")
            return

        for parceiro in parceiros:
            print("\n------------------------------")
            print(f"ID do parceiro: {parceiro[0]}")
            print(f"Empresa: {parceiro[1]}")
            print(f"E-mail: {parceiro[2]}")
            print(f"Tipo de serviço: {parceiro[3]}")
            print(f"Localização: {parceiro[4]} - {parceiro[5]}")

        demonstrar_interesse = input(
            "\nDeseja demonstrar interesse em algum parceiro? (s/n): "
        )

        if demonstrar_interesse.strip().lower() != "s":
            print("Nenhum interesse foi registrado.")
            return

        id_parceiro = int(input("Digite o ID do parceiro desejado: "))

        ids_parceiros_disponiveis = [parceiro[0] for parceiro in parceiros]

        if id_parceiro not in ids_parceiros_disponiveis:
            print("Parceiro inválido. Escolha apenas um parceiro listado.")
            return

        confirmacao = input("Confirmar interesse nesta solução/parceiro? (s/n): ")

        if confirmacao.strip().lower() != "s":
            print("Operação cancelada.")
            return

        id_lead = criar_lead(
            id_usuario,
            id_parceiro,
            id_solucao
        )

        if id_lead is None:
            print("Já existe um interesse ativo para esse parceiro e essa solução.")
            return

        print(f"Interesse registrado com sucesso. Código do lead: {id_lead}")

    except ValueError:
        print("Erro: informe um ID válido.")

    except Exception as erro:
        print("Erro ao visualizar soluções:")
        print(erro)

def visualizar_meus_interesses(id_usuario):
    leads = listar_leads_usuario(id_usuario)

    print("\n===== MEUS INTERESSES =====")

    if not leads:
        print("Nenhum interesse registrado.")
        return

    for lead in leads:
        print("\n------------------------------")
        print(f"ID do lead: {lead[0]}")
        print(f"Solução: {lead[1]}")
        print(f"Parceiro: {lead[2]}")
        print(f"E-mail do parceiro: {lead[3]}")
        print(f"Status: {lead[4]}")
        print(f"Data: {lead[5]}")


def cancelar_interesse(id_usuario):
    print("\n===== CANCELAR INTERESSE =====")

    leads = listar_leads_usuario(id_usuario)

    if not leads:
        print("Nenhum interesse encontrado para cancelar.")
        return

    visualizar_meus_interesses(id_usuario)

    try:
        id_lead = int(input("\nDigite o ID do lead que deseja cancelar: "))

        confirmacao = input("Tem certeza que deseja cancelar este interesse? (s/n): ")

        if confirmacao.strip().lower() != "s":
            print("Operação cancelada.")
            return

        sucesso = cancelar_lead_usuario(id_lead, id_usuario)

        if sucesso:
            print("Interesse cancelado com sucesso.")
        else:
            print("Lead não encontrado para este usuário.")

    except ValueError:
        print("Erro: informe um ID válido.")

    except Exception as erro:
        print("Erro ao cancelar interesse:")
        print(erro)