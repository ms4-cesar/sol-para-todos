import bcrypt
from db import get_connection
from sql.usuario_sql import (
    INSERT_USUARIO,
    SELECT_USUARIO_POR_EMAIL,
    SELECT_USUARIO_POR_ID,
    UPDATE_USUARIO,
    DELETE_USUARIO
)

def criar_usuario(nome, sobrenome, email, senha, cpf, renda, tipo_moradia):
    senha_hash = bcrypt.hashpw(
        senha.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            INSERT_USUARIO,
            (nome, sobrenome, email, senha_hash, cpf, renda, tipo_moradia)
        )

        id_usuario = cursor.fetchone()[0]
        conn.commit()

        return id_usuario

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()


def buscar_usuario_por_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_USUARIO_POR_EMAIL, (email,))
        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()


def buscar_usuario_por_id(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_USUARIO_POR_ID, (id_usuario,))
        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()


def atualizar_usuario(id_usuario, nome, sobrenome, renda, tipo_moradia):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            UPDATE_USUARIO,
            (nome, sobrenome, renda, tipo_moradia, id_usuario)
        )

        conn.commit()

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()


def excluir_usuario(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(DELETE_USUARIO, (id_usuario,))
        conn.commit()

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()
