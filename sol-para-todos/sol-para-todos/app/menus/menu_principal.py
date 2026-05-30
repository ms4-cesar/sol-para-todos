from auth import autenticar_usuario
from services.usuario_service import criar_usuario
from menus.menu_usuario import menu_usuario
from menus.menu_parceiro import menu_parceiro
from services.parceiro_service import (
    autenticar_parceiro,
    criar_parceiro
)

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

def cadastrar_parceiro():
    print("\n===== CADASTRO DE EMPRESA PARCEIRA =====")

    nome_empresa = input("Nome da empresa: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cnpj = input("CNPJ (somente números): ")
    tipo_servico = input("Tipo de serviço prestado: ")
    
    try:
        id_parceiro = criar_parceiro(
            nome_empresa,
            email,
            senha,
            cnpj,
            tipo_servico
        )

        print(f"Empresa parceira cadastrada com sucesso. ID: {id_parceiro}")

    except Exception as erro:
        print("Erro ao cadastrar parceiro:")
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

def login_parceiro():
    print("\n===== LOGIN DE EMPRESA PARCEIRA =====")

    email = input("E-mail: ")
    senha = input("Senha: ")

    parceiro = autenticar_parceiro(email, senha)

    if parceiro is None:
        print("E-mail ou senha inválidos.")
        return

    print(f"Login realizado com sucesso. Bem-vindo(a), {parceiro['nome_empresa']}!")
    menu_parceiro(parceiro)


def menu_principal():
    while True:
        print("\n==============================")
        print("        SOL PARA TODOS")
        print("==============================")
        print("1 - Login")
        print("2 - Cadastrar-se")
        print("3 - Cadastrar-se como parceiro")
        print("4 - Login de parceiro")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            login()

        elif opcao == "2":
            cadastrar_usuario()

        elif opcao == "3":
            cadastrar_parceiro()

        elif opcao == "4":
            login_parceiro()

        elif opcao == "0":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida.")
