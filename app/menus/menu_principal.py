from auth import autenticar_usuario
from services.usuario_service import criar_usuario
from menus.menu_usuario import menu_usuario

def cadastrar_usuario():
    print("\n===== CADASTRO DE USUÁRIO =====")

    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    cpf = input("CPF (somente números): ")
    renda = float(input("Renda: "))
    tipo_moradia = input("Tipo de moradia (Casa, Apartamento, Área rural, Outro): ")

    try:
        id_usuario = criar_usuario(
            nome,
            sobrenome,
            email,
            senha,
            cpf,
            renda,
            tipo_moradia
        )

        print(f"Usuário cadastrado com sucesso. ID: {id_usuario}")

    except Exception as erro:
        print("Erro ao cadastrar usuário:")
        print(erro)


def login():
    print("\n===== LOGIN =====")

    email = input("E-mail: ")
    senha = input("Senha: ")

    usuario = autenticar_usuario(email, senha)

    if usuario is None:
        print("E-mail ou senha inválidos.")
        return

    print(f"Login realizado com sucesso. Bem-vindo(a), {usuario['nome']}!")
    menu_usuario(usuario)


def menu_principal():
    while True:
        print("\n==============================")
        print("        SOL PARA TODOS")
        print("==============================")
        print("1 - Login")
        print("2 - Cadastrar-se")
        print("3 - Cadastrar-se como parceiro")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            login()

        elif opcao == "2":
            cadastrar_usuario()

        elif opcao == "3":
            print("Cadastro de parceiro ainda será implementado.")

        elif opcao == "0":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida.")
