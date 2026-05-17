from app.services.simulacao_service import (
    criar_simulacao,
    listar_simulacoes_usuario,
    excluir_simulacao
)

from app.services.usuario_service import (
    buscar_usuario_por_id,
    atualizar_usuario,
    excluir_usuario
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
    nova_renda = input("Nova renda (pressione Enter para manter): ")

    print(f"Tipo de moradia atual: {usuario[6]}")
    novo_tipo_moradia = input(
        "Novo tipo de moradia (Casa, Apartamento, Área rural, Outro) ou Enter para manter: "
    )

    nome = novo_nome if novo_nome.strip() else usuario[1]
    sobrenome = novo_sobrenome if novo_sobrenome.strip() else usuario[2]
    renda = float(nova_renda) if nova_renda.strip() else usuario[5]
    tipo_moradia = novo_tipo_moradia if novo_tipo_moradia.strip() else usuario[6]

    try:
        atualizar_usuario(
            id_usuario,
            nome,
            sobrenome,
            renda,
            tipo_moradia
        )
        print("Perfil atualizado com sucesso.")

    except Exception as erro:
        print("Erro ao atualizar perfil:")
        print(erro)


def deletar_conta(id_usuario):
    confirmacao = input("Tem certeza que deseja excluir sua conta? (s/n): ")

    if confirmacao.lower() != "s":
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
        print("6 - Excluir minha conta")
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
            conta_excluida = deletar_conta(usuario_logado["id_usuario"])

            if conta_excluida:
                break

        elif opcao == "0":
            print("Saindo da conta.")
            break

        else:
            print("Opção inválida.")


def fazer_simulacao(id_usuario):
    print("\n===== FAZER SIMULAÇÃO =====")

    try:
        consumo_mensal = float(input("Informe seu consumo mensal em kWh: "))
        valor_fatura = float(input("Informe o valor médio da sua conta de luz: R$ "))

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
        print(f"Economia estimada geral: R$ {simulacao[3]}")
        print(f"Data: {simulacao[4]}")


def deletar_simulacao(id_usuario):
    print("\n===== EXCLUIR SIMULAÇÃO =====")

    visualizar_simulacoes(id_usuario)

    try:
        id_simulacao = int(input("\nInforme o ID da simulação que deseja excluir: "))

        confirmacao = input("Tem certeza que deseja excluir esta simulação? (s/n): ")

        if confirmacao.lower() != "s":
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
