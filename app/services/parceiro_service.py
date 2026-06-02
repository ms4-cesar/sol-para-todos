import bcrypt
from app.db import get_connection
from app.sql.parceiro_sql import (
    INSERT_PARCEIRO,
    INSERT_ENDERECO_PARCEIRO,
    INSERT_TELEFONE_PARCEIRO,
    SELECT_PARCEIRO_POR_EMAIL,
    SELECT_PARCEIRO_POR_ID,
    SELECT_ENDERECOS_PARCEIRO,
    SELECT_TELEFONES_PARCEIRO,
    UPDATE_PARCEIRO,
    DELETE_PARCEIRO,
    SELECT_SOLUCAO_POR_TIPO,
    INSERT_PARCEIRO_SOLUCAO
)


def criar_parceiro(
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
):
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

        cursor.execute(
            INSERT_ENDERECO_PARCEIRO,
            (
                id_parceiro,
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
            INSERT_TELEFONE_PARCEIRO,
            (id_parceiro, ddd, telefone)
        )

        cursor.execute(SELECT_SOLUCAO_POR_TIPO, (tipo_servico,))
        solucao = cursor.fetchone()

        if solucao is not None:
            id_solucao = solucao[0]

            cursor.execute(
                INSERT_PARCEIRO_SOLUCAO,
                (id_parceiro, id_solucao)
            )

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


def listar_enderecos_parceiro(id_parceiro):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_ENDERECOS_PARCEIRO, (id_parceiro,))
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def listar_telefones_parceiro(id_parceiro):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_TELEFONES_PARCEIRO, (id_parceiro,))
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def atualizar_parceiro(id_parceiro, nome_empresa, tipo_servico):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            UPDATE_PARCEIRO,
            (nome_empresa, tipo_servico, id_parceiro)
        )

        cursor.execute(SELECT_SOLUCAO_POR_TIPO, (tipo_servico,))
        solucao = cursor.fetchone()

        if solucao is not None:
            id_solucao = solucao[0]

            cursor.execute(
                INSERT_PARCEIRO_SOLUCAO,
                (id_parceiro, id_solucao)
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