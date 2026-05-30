import bcrypt
from db import get_connection
from sql.parceiro_sql import (
    INSERT_PARCEIRO,
    SELECT_PARCEIRO_POR_EMAIL,
    SELECT_PARCEIRO_POR_ID,
    UPDATE_PARCEIRO,
    DELETE_PARCEIRO
)

def criar_parceiro(nome_empresa, email, senha, cnpj, tipo_servico):
    senha_hash = bcrypt.hashpw(
        senha.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            INSERT_PARCEIRO,
            (nome_empresa, email, senha_hash, cnpj, tipo_servico)
        )

        id_parceiro = cursor.fetchone()[0]
        conn.commit()

        return id_parceiro

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()

def buscar_parceiro_por_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_PARCEIRO_POR_EMAIL, (email,))
        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()

def buscar_parceiro_por_id(id_parceiro):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_PARCEIRO_POR_ID, (id_parceiro,))
        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()

def atualizar_parceiro(id_parceiro, nome_empresa, email, tipo_servico):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            UPDATE_PARCEIRO,
            (nome_empresa, email, tipo_servico, id_parceiro)
        )

        conn.commit()

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()

def excluir_parceiro(id_parceiro):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(DELETE_PARCEIRO, (id_parceiro,))
        conn.commit()

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()

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
        "id_parceiro": parceiro[0],
        "nome_empresa": parceiro[1],
        "email": parceiro[2],
        "cnpj": parceiro[4],
        "tipo_servico": parceiro[5]
    }
