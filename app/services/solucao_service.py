from db import get_connection
from sql.solucao_sql import (
    INSERT_SOLUCAO,
    SELECT_TODAS_SOLUCOES,
    SELECT_SOLUCAO_POR_ID,
    UPDATE_SOLUCAO,
    DELETE_SOLUCAO
)

def criar_solucao(tipo_solucao, descricao_solucao, requisitos):
    """
    Regra de Negócio: Valida se os campos obrigatórios não estão vazios
    ou preenchidos apenas com espaços antes de submeter à base de dados.
    """
    if not tipo_solucao or not tipo_solucao.strip():
        raise ValueError("O tipo de solução não pode estar vazio.")
    if not descricao_solucao or not descricao_solucao.strip():
        raise ValueError("A descrição da solução não pode estar vazia.")
    if not requisitos or not requisitos.strip():
        raise ValueError("Os requisitos da solução não podem estar vazios.")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            INSERT_SOLUCAO,
            (tipo_solucao.strip(), descricao_solucao.strip(), requisitos.strip())
        )
        id_solucao = cursor.fetchone()[0]
        conn.commit()
        return id_solucao

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()


def listar_todas_solucoes():
    """
    Retorna a lista completa de soluções registadas no catálogo.
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_TODAS_SOLUCOES)
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def buscar_solucao_por_id(id_solucao):
    """
    Procura e retorna uma solução específica com base no seu ID único.
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_SOLUCAO_POR_ID, (id_solucao,))
        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()


def atualizar_solucao(id_solucao, tipo_solucao, descricao_solucao, requisitos):
    """
    Modifica os dados de uma solução existente com validação de consistência.
    """
    if not tipo_solucao or not tipo_solucao.strip():
        raise ValueError("O tipo de solução modificado não pode estar vazio.")
    if not descricao_solucao or not descricao_solucao.strip():
        raise ValueError("A descrição modificada não pode estar vazia.")
    if not requisitos or not requisitos.strip():
        raise ValueError("Os requisitos modificados não podem estar vazios.")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            UPDATE_SOLUCAO,
            (tipo_solucao.strip(), descricao_solucao.strip(), requisitos.strip(), id_solucao)
        )
        conn.commit()

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()


def excluir_solucao(id_solucao):
    """
    Remove uma solução do catálogo. 
    Atenção: Irá disparar o ON DELETE CASCADE nas tabelas dependentes.
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(DELETE_SOLUCAO, (id_solucao,))
        conn.commit()
        return True

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()