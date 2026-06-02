import bcrypt
from app.services.usuario_service import buscar_usuario_por_email
from app.services.parceiro_service import buscar_parceiro_por_email


def autenticar_usuario(email, senha):
    usuario = buscar_usuario_por_email(email)

    if usuario is None:
        return None

    senha_hash = usuario[4]

    senha_valida = bcrypt.checkpw(
        senha.encode("utf-8"),
        senha_hash.encode("utf-8")
    )

    if not senha_valida:
        return None

    return {
        "tipo": "usuario",
        "id_usuario": usuario[0],
        "nome": usuario[1],
        "sobrenome": usuario[2],
        "email": usuario[3]
    }


def autenticar_parceiro(email, senha):
    parceiro = buscar_parceiro_por_email(email)

    if parceiro is None:
        return None

    senha_hash = parceiro[3]

    senha_valida = bcrypt.checkpw(
        senha.encode("utf-8"),
        senha_hash.encode("utf-8")
    )

    if not senha_valida:
        return None

    return {
        "tipo": "parceiro",
        "id_parceiro": parceiro[0],
        "nome_empresa": parceiro[1],
        "email": parceiro[2]
    }


def autenticar_login(email, senha):
    usuario = autenticar_usuario(email, senha)

    if usuario is not None:
        return usuario

    parceiro = autenticar_parceiro(email, senha)

    if parceiro is not None:
        return parceiro

    return None