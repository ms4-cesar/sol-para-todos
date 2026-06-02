from app.db import get_connection
from app.sql.solucao_sql import (
    SELECT_SOLUCOES,
    SELECT_SOLUCAO_POR_ID,
    SELECT_ENDERECO_USUARIO,
    SELECT_PARCEIROS_POR_SOLUCAO_E_LOCALIZACAO
)


def listar_solucoes():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_SOLUCOES)
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def buscar_solucao_por_id(id_solucao):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_SOLUCAO_POR_ID, (id_solucao,))
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


def listar_parceiros_por_solucao_e_usuario(id_solucao, id_usuario):
    endereco_usuario = buscar_endereco_usuario(id_usuario)

    if endereco_usuario is None:
        return None

    cidade_usuario = endereco_usuario[0]
    uf_usuario = endereco_usuario[1]

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            SELECT_PARCEIROS_POR_SOLUCAO_E_LOCALIZACAO,
            (id_solucao, uf_usuario, cidade_usuario)
        )

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()