from services.solucao_service import (
    criar_solucao,
    listar_todas_solucoes,
    buscar_solucao_por_id,
    atualizar_solucao,
    excluir_solucao
)

def cadastrar_nova_solucao():
    print("\n===== CADASTRAR NOVA SOLUÇÃO =====")
    tipo = input("Tipo de Solução (ex: Cooperativa Solar): ")
    descricao = input("Descrição da Solução: ")
    requisitos = input("Requisitos de Elegibilidade: ")

    try:
        id_solucao = criar_solucao(tipo, descricao, requisitos)
        print(f"\n[SUCESSO] Solução cadastrada com sucesso! ID Gerado: {id_solucao}")
    except Exception as erro:
        print(f"\n[ERRO] Não foi possível cadastrar a solução: {erro}")


def exibir_todas_solucoes():
    print("\n===== PORTFÓLIO DE SOLUÇÕES ENERGÉTICAS =====")
    try:
        solucoes = listar_todas_solucoes()
        
        if not solucoes:
            print("Nenhuma solução ativa no catálogo atual.")
            return

        for sol in solucoes:
            print("\n--------------------------------------------------")
            print(f"ID da Solução: {sol[0]}")
            print(f"Tipo:          {sol[1]}")
            print(f"Descrição:     {sol[2]}")
            print(f"Requisitos:    {sol[3]}")
        print("\n--------------------------------------------------")
    except Exception as erro:
        print(f"\n[ERRO] Falha ao listar soluções: {erro}")


def editar_solucao_existente():
    print("\n===== ATUALIZAR INFORMAÇÕES DA SOLUÇÃO =====")
    try:
        id_solucao = int(input("Informe o ID da solução que deseja alterar: "))
        solucao_atual = buscar_solucao_por_id(id_solucao)

        if not solucao_atual:
            print("\n[AVISO] Nenhuma solução encontrada com o ID informado.")
            return

        print(f"\nTipo atual: {solucao_atual[1]}")
        novo_tipo = input("Novo tipo (Pressione Enter para manter): ") or solucao_atual[1]

        print(f"\nDescrição atual: {solucao_atual[2]}")
        nova_descricao = input("Nova descrição (Pressione Enter para manter): ") or solucao_atual[2]

        print(f"\nRequisitos atuais: {solucao_atual[3]}")
        novos_requisitos = input("Novos requisitos (Pressione Enter para manter): ") or solucao_atual[3]

        atualizar_solucao(id_solucao, novo_tipo, nova_descricao, novos_requisitos)
        print("\n[SUCESSO] Solução atualizada com sucesso no banco de dados!")

    except ValueError:
        print("\n[ERRO] Por favor, informe um número de ID válido.")
    except Exception as erro:
        print(f"\n[ERRO] Falha ao atualizar dados: {erro}")


def remover_solucao_catalogo():
    print("\n===== REMOVER SOLUÇÃO PERMANENTEMENTE =====")
    try:
        id_solucao = int(input("Informe o ID da solução a ser excluída: "))
        solucao = buscar_solucao_por_id(id_solucao)

        if not solucao:
            print("\n[AVISO] Solução não encontrada.")
            return

        print(f"\n⚠️ ATENÇÃO: Você está prestes a deletar a solução: '{solucao[1]}'.")
        print("Isso apagará permanentemente todos os leads e vínculos vinculados a ela!")
        confirmacao = input("Deseja prosseguir com a exclusão? (s/n): ")

        if confirmacao.lower() == 's':
            excluir_solucao(id_solucao)
            print("\n[SUCESSO] Solução expurgada do sistema.")
        else:
            print("\nOperação cancelada pelo operador.")

    except ValueError:
        print("\n[ERRO] ID inválido.")
    except Exception as erro:
        print(f"\n[ERRO] Não foi possível remover o registro: {erro}")


def menu_gerenciar_solucoes():
    while True:
        print("\n==============================")
        print("    PAINEL DE SOLUÇÕES (CRUD)")
        print("==============================")
        print("1 - Cadastrar Nova Solução")
        print("2 - Listar Todas as Soluções")
        print("3 - Atualizar uma Solução")
        print("4 - Remover uma Solução")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_nova_solucao()
        elif opcao == "2":
            exibir_todas_solucoes()
        elif opcao == "3":
            editar_solucao_existente()
        elif opcao == "4":
            remover_solucao_catalogo()
        elif opcao == "0":
            print("Retornando ao menu anterior...")
            break
        else:
            print("Opção inválida. Tente novamente.")