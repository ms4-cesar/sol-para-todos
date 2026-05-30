import bcrypt
from services.usuario_service import buscar_usuario_por_email

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
        "id_usuario": usuario[0],
        "nome": usuario[1],
        "sobrenome": usuario[2],
        "email": usuario[3]
    }
