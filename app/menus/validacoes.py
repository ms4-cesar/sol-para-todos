def solicitar_texto_obrigatorio(mensagem, tamanho_maximo=None):
    while True:
        valor = input(mensagem).strip()

        if not valor:
            print("\n❌ Erro: este campo é obrigatório.")
            continue

        if tamanho_maximo is not None and len(valor) > tamanho_maximo:
            print(f"\n❌ Erro: este campo deve ter no máximo {tamanho_maximo} caracteres.")
            continue

        return valor


def solicitar_texto_opcional(mensagem, tamanho_maximo=None):
    while True:
        valor = input(mensagem).strip()

        if not valor:
            return None

        if tamanho_maximo is not None and len(valor) > tamanho_maximo:
            print(f"\n❌ Erro: este campo deve ter no máximo {tamanho_maximo} caracteres.")
            continue

        return valor


def solicitar_email(mensagem="E-mail: "):
    while True:
        email = input(mensagem).strip()

        if not email:
            print("\n❌ Erro: o e-mail é obrigatório.")
            continue

        if len(email) > 150:
            print("\n❌ Erro: o e-mail deve ter no máximo 150 caracteres.")
            continue

        if "@" not in email or "." not in email:
            print("\n❌ Erro: informe um e-mail válido.")
            continue

        return email


def solicitar_senha(mensagem="Senha: "):
    while True:
        senha = input(mensagem).strip()

        if not senha:
            print("\n❌ Erro: a senha é obrigatória.")
            continue

        if len(senha) > 255:
            print("\n❌ Erro: a senha deve ter no máximo 255 caracteres.")
            continue

        if len(senha) < 6:
            print("\n❌ Erro: a senha deve ter pelo menos 6 caracteres.")
            continue

        return senha


def solicitar_cpf(mensagem="CPF (somente números): "):
    while True:
        cpf = input(mensagem).strip()

        if not cpf.isdigit():
            print("\n❌ Erro: o CPF deve conter apenas números.")
            continue

        if len(cpf) != 11:
            print("\n❌ Erro: o CPF deve conter exatamente 11 dígitos.")
            continue

        return cpf


def solicitar_cnpj(mensagem="CNPJ (somente números): "):
    while True:
        cnpj = input(mensagem).strip()

        if not cnpj.isdigit():
            print("\n❌ Erro: o CNPJ deve conter apenas números.")
            continue

        if len(cnpj) != 14:
            print("\n❌ Erro: o CNPJ deve conter exatamente 14 dígitos.")
            continue

        return cnpj


def solicitar_renda(mensagem="Renda: "):
    while True:
        valor = input(mensagem).strip()

        if not valor:
            print("\n❌ Erro: a renda é obrigatória.")
            continue

        try:
            renda = float(valor)

            if renda < 0:
                print("\n❌ Erro: a renda não pode ser negativa.")
                continue

            return renda

        except ValueError:
            print("\n❌ Erro: informe um valor numérico válido para a renda.")


def solicitar_renda_opcional(mensagem="Nova renda (pressione Enter para manter): "):
    while True:
        valor = input(mensagem).strip()

        if not valor:
            return None

        try:
            renda = float(valor)

            if renda < 0:
                print("\n❌ Erro: a renda não pode ser negativa.")
                continue

            return renda

        except ValueError:
            print("\n❌ Erro: informe um valor numérico válido para a renda.")


def solicitar_ddd(mensagem="DDD: "):
    while True:
        ddd = input(mensagem).strip()

        if not ddd.isdigit():
            print("\n❌ Erro: o DDD deve conter apenas números.")
            continue

        if len(ddd) != 2:
            print("\n❌ Erro: o DDD deve conter exatamente 2 dígitos. Exemplo: 81.")
            continue

        return ddd


def solicitar_telefone(mensagem="Telefone: "):
    while True:
        telefone = input(mensagem).strip()

        if not telefone.isdigit():
            print("\n❌ Erro: o telefone deve conter apenas números.")
            continue

        if len(telefone) not in [8, 9]:
            print("\n❌ Erro: o telefone deve conter 8 ou 9 dígitos.")
            continue

        return telefone


def solicitar_cep(mensagem="CEP (somente números): "):
    while True:
        cep = input(mensagem).strip()

        if not cep.isdigit():
            print("\n❌ Erro: o CEP deve conter apenas números.")
            continue

        if len(cep) != 8:
            print("\n❌ Erro: o CEP deve conter exatamente 8 dígitos.")
            continue

        return cep


def solicitar_uf(mensagem="UF: "):
    while True:
        uf = input(mensagem).strip().upper()

        if not uf.isalpha():
            print("\n❌ Erro: a UF deve conter apenas letras.")
            continue

        if len(uf) != 2:
            print("\n❌ Erro: a UF deve conter exatamente 2 letras. Exemplo: PE.")
            continue

        return uf