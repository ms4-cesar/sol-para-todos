import bcrypt
from app.db import get_connection
from app.sql.usuario_sql import (
    INSERT_USUARIO,
    SELECT_USUARIO_POR_EMAIL,
    SELECT_USUARIO_POR_ID,
    UPDATE_USUARIO,
    DELETE_USUARIO,
    INSERT_ENDERECO_USUARIO,
    INSERT_TELEFONE_USUARIO,
    SELECT_ENDERECO_USUARIO,
    SELECT_TELEFONES_USUARIO
)

def criar_usuario(
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
):
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

        cursor.execute(
            INSERT_ENDERECO_USUARIO,
            (
                id_usuario,
                rua,
                numero,
                complemento,
                cep,
                bairro,
                cidade,
                uf
            )
        )

        cursor.execute(
            INSERT_TELEFONE_USUARIO,
            (
                id_usuario,
                ddd,
                telefone
            )
        )

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


def buscar_endereco_usuario(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_ENDERECO_USUARIO, (id_usuario,))
        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()


def listar_telefones_usuario(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_TELEFONES_USUARIO, (id_usuario,))
        return cursor.fetchall()

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
