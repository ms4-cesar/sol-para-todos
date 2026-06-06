from app.db import get_connection
from app.sql.lead_sql import (
    INSERT_LEAD,
    SELECT_LEADS_POR_USUARIO,
    SELECT_LEADS_POR_PARCEIRO,
    UPDATE_STATUS_LEAD,
    CANCELAR_LEAD_USUARIO,
    CANCELAR_LEAD_PARCEIRO,
    SELECT_LEAD_EXISTENTE
)


def criar_lead(id_usuario, id_parceiro, id_solucao):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            SELECT_LEAD_EXISTENTE,
            (id_usuario, id_parceiro, id_solucao)
        )

        lead_existente = cursor.fetchone()

        if lead_existente is not None:
            return None

        cursor.execute(
            INSERT_LEAD,
            (id_parceiro, id_usuario, id_solucao)
        )

        id_lead = cursor.fetchone()[0]
        conn.commit()

        return id_lead

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()


def listar_leads_usuario(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_LEADS_POR_USUARIO, (id_usuario,))
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def listar_leads_parceiro(id_parceiro):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_LEADS_POR_PARCEIRO, (id_parceiro,))
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def atualizar_status_lead(id_lead, id_parceiro, novo_status):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            UPDATE_STATUS_LEAD,
            (novo_status, id_lead, id_parceiro)
        )

        conn.commit()

        return cursor.rowcount > 0

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()


def cancelar_lead_usuario(id_lead, id_usuario):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            CANCELAR_LEAD_USUARIO,
            (id_lead, id_usuario)
        )

        conn.commit()

        return cursor.rowcount > 0

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()


def cancelar_lead_parceiro(id_lead, id_parceiro):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            CANCELAR_LEAD_PARCEIRO,
            (id_lead, id_parceiro)
        )

        conn.commit()

        return cursor.rowcount > 0

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()