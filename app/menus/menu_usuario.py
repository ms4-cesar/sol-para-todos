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
        print("3 - Excluir minha conta")
        print("0 - Sair da conta")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visualizar_perfil(usuario_logado["id_usuario"])

        elif opcao == "2":
            editar_perfil(usuario_logado["id_usuario"])

        elif opcao == "3":
            conta_excluida = deletar_conta(usuario_logado["id_usuario"])

            if conta_excluida:
                break

        elif opcao == "0":
            print("Saindo da conta.")
            break

        else:
            print("Opção inválida.")
