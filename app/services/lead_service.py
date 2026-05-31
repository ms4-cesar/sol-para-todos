from db import get_connection
from sql.lead_sql import (
INSERT_LEAD,
SELECT_LEADS_POR_PARCEIRO,
SELECT_LEADS_POR_CLIENTE,
SELECT_PARCEIRO_SOLUCAO,
UPDATE_STATUS_LEAD,
DELETE_LEAD
)

from services.usuario_service import buscar_usuario_por_id

def criar_lead(id_usuario, id_solucao):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        SELECT_PARCEIRO_SOLUCAO,
        (id_solucao,)
    )

    id_parceiro = cursor.fetchone()[0]

    cursor.execute(
        INSERT_LEAD,
        (id_usuario, id_parceiro, id_solucao, "Novo")
    )

    conn.commit()
    cursor.close()
    conn.close()

def listar_leads_parceiro(id_parceiro):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        SELECT_LEADS_POR_PARCEIRO,
        (id_parceiro,)
    )

    leads_raws = cursor.fetchall()

    leads = []

    for lead in leads_raws:
        usuario = buscar_usuario_por_id(lead[2])
        lead_dict = {
            "id_lead": lead[0],
            "nome_usuario": usuario[1],
            "status": lead[3],
            "created_at": lead[4],
        }
        leads.append(lead_dict)

    cursor.close()
    conn.close()

    return leads

def listar_leads_cliente(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        SELECT_LEADS_POR_CLIENTE,
        (id_usuario,)
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