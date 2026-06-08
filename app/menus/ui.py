def linha():
    print("=" * 50)


def separador():
    print("-" * 50)


def cabecalho_sistema():
    print(r"""
        \   |   /
          .-*-.
       -- ( ☀ ) --     SOL PARA TODOS
          `-*-'
        /   |   \      Energia solar acessível
    """)
    print("=" * 50)


def cabecalho(titulo, icone=""):
    print("\n" + "=" * 50)

    if icone:
        print(f"{icone}  {titulo}")
    else:
        print(titulo)

    print("=" * 50)


def mensagem_sucesso(mensagem):
    print(f"\n✅ {mensagem}")


def mensagem_erro(mensagem):
    print(f"\n❌ {mensagem}")


def mensagem_alerta(mensagem):
    print(f"\n⚠️  {mensagem}")


def mensagem_info(mensagem):
    print(f"\nℹ️  {mensagem}")