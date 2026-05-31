from db import get_connection
from sql.lead_sql import (
INSERT_LEAD,
SELECT_LEADS_POR_PARCEIRO,
SELECT_LEADS_POR_CLIENTE,
UPDATE_STATUS_LEAD,
DELETE_LEAD
)


def criar_lead(id_cliente, id_parceiro):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        INSERT_LEAD,
        (id_cliente, id_parceiro, "Em contato")
    )

    id_lead = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return id_lead


def listar_leads_parceiro(id_parceiro):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        SELECT_LEADS_POR_PARCEIRO,
        (id_parceiro,)
    )

    leads = cursor.fetchall()

    cursor.close()
    conn.close()

    return leads


def listar_leads_cliente(id_cliente):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        SELECT_LEADS_POR_CLIENTE,
        (id_cliente,)
    )

    leads = cursor.fetchall()

    cursor.close()
    conn.close()

    return leads


def atualizar_status_lead(id_lead, novo_status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        UPDATE_STATUS_LEAD,
        (novo_status, id_lead)
    )

    conn.commit()

    cursor.close()
    conn.close()


def deletar_lead(id_lead):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        DELETE_LEAD,
        (id_lead,)
    )

    conn.commit()

    cursor.close()
    conn.close()