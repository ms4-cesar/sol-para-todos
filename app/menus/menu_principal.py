<<<<<<< HEAD
from auth import autenticar_usuario
from services.usuario_service import criar_usuario
from menus.menu_usuario import menu_usuario
from menus.opcoes import escolher_tipo_moradia
from auth import autenticar_login
from services.parceiro_service import criar_parceiro
from menus.menu_parceiro import menu_parceiro
from menus.opcoes import escolher_tipo_moradia, escolher_tipo_servico
from menus.validacoes import (
=======
from app.menus.ui import cabecalho_sistema, cabecalho
from app.auth import autenticar_login
from app.services.usuario_service import criar_usuario
from app.services.parceiro_service import criar_parceiro
from app.menus.menu_usuario import menu_usuario
from app.menus.menu_parceiro import menu_parceiro
from app.menus.opcoes import escolher_tipo_moradia, escolher_tipo_servico
from app.menus.validacoes import (
>>>>>>> origin/main
    solicitar_texto_obrigatorio,
    solicitar_email,
    solicitar_senha,
    solicitar_cpf,
    solicitar_renda,
    solicitar_cnpj,
    solicitar_ddd,
    solicitar_telefone,
    solicitar_cep,
    solicitar_uf,
    solicitar_texto_opcional
)


def cadastrar_usuario():
    cabecalho("CADASTRO DE USUÁRIO", "👤")

    nome = solicitar_texto_obrigatorio("Nome: ", tamanho_maximo=100)
    sobrenome = solicitar_texto_obrigatorio("Sobrenome: ", tamanho_maximo=100)
    email = solicitar_email()
    senha = solicitar_senha()
    cpf = solicitar_cpf()
    renda = solicitar_renda()
    tipo_moradia = escolher_tipo_moradia()

    cabecalho("ENDEREÇO DO USUÁRIO", "📍")

    rua = solicitar_texto_obrigatorio("Rua: ", tamanho_maximo=150)
    numero = solicitar_texto_obrigatorio("Número: ", tamanho_maximo=10)

    complemento = solicitar_texto_opcional(
        "Complemento (pressione Enter se não houver): ",
        tamanho_maximo=150
    )

    cep = solicitar_cep()
    bairro = solicitar_texto_obrigatorio("Bairro: ", tamanho_maximo=100)
    cidade = solicitar_texto_obrigatorio("Cidade: ", tamanho_maximo=100)
    uf = solicitar_uf()

    cabecalho("TELEFONE DO USUÁRIO", "📞")

    ddd = solicitar_ddd()
    telefone = solicitar_telefone()

    try:
        id_usuario = criar_usuario(
            nome,
            sobrenome,
            email,
            senha,
            cpf,
            renda,
            tipo_moradia,
            rua,
            numero,
            complemento,
            cep,
            bairro,
            cidade,
            uf,
            ddd,
            telefone
        )

        print(f"\n✅ Usuário cadastrado com sucesso. ID: {id_usuario}")

    except Exception as erro:
        print("\n❌ Erro ao cadastrar usuário:")
        print(erro)


def cadastrar_parceiro():
    cabecalho("CADASTRO DE PARCEIRO", "🏢")

    nome_empresa = solicitar_texto_obrigatorio(
        "Nome da empresa: ",
        tamanho_maximo=150
    )

    email = solicitar_email()
    senha = solicitar_senha()
    cnpj = solicitar_cnpj()

    tipo_servico = escolher_tipo_servico()

    cabecalho("ENDEREÇO DO PARCEIRO", "📍")

    rua = solicitar_texto_obrigatorio(
        "Rua: ",
        tamanho_maximo=150
    )

    numero = solicitar_texto_obrigatorio(
        "Número: ",
        tamanho_maximo=10
    )

    complemento = solicitar_texto_opcional(
        "Complemento (pressione Enter se não houver): ",
        tamanho_maximo=150
    )

    cep = solicitar_cep()

    bairro = solicitar_texto_obrigatorio(
        "Bairro: ",
        tamanho_maximo=100
    )

    cidade = solicitar_texto_obrigatorio(
        "Cidade: ",
        tamanho_maximo=100
    )

    uf = solicitar_uf()

    cabecalho("TELEFONE DO PARCEIRO", "📞")

    ddd = solicitar_ddd()
    telefone = solicitar_telefone()

    try:
        id_parceiro = criar_parceiro(
            nome_empresa,
            email,
            senha,
            cnpj,
            tipo_servico,
            rua,
            numero,
            complemento,
            cep,
            bairro,
            cidade,
            uf,
            ddd,
            telefone
        )

        print(f"\n✅ Parceiro cadastrado com sucesso. ID: {id_parceiro}")

    except Exception as erro:
        print("\n❌ Erro ao cadastrar parceiro:")
        print(erro)


def login():
    cabecalho("LOGIN", "🔐")

    email = input("E-mail: ")
    senha = input("Senha: ")

    conta = autenticar_login(email, senha)

    if conta is None:
        print("\n❌ E-mail ou senha inválidos.")
        return

    if conta["tipo"] == "usuario":
        print(f"\n✅ Login realizado com sucesso. Bem-vindo(a), {conta['nome']}!")
        menu_usuario(conta)

    elif conta["tipo"] == "parceiro":
        print(f"\n✅ Login realizado com sucesso. Bem-vindo(a), {conta['nome_empresa']}!")
        menu_parceiro(conta)


def menu_principal():
    while True:
        cabecalho_sistema()

        print("1 - Login")
        print("2 - Cadastrar-se como usuário")
        print("3 - Cadastrar-se como parceiro")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            login()

        elif opcao == "2":
            cadastrar_usuario()

        elif opcao == "3":
            cadastrar_parceiro()

        elif opcao == "0":
            print("\nEncerrando o sistema.")
            break

        else:
            print("\n❌ Opção inválida.")