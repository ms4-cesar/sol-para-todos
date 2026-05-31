INSERT_LEAD = """
INSERT INTO Lead (
    id_cliente,
    id_parceiro,
    status
)
VALUES (%s, %s, %s)
RETURNING id_lead;
"""

SELECT_LEADS_POR_PARCEIRO = """
SELECT
    id_lead,
    id_cliente,
    id_parceiro,
    status,
    data_criacao
FROM Lead
WHERE id_parceiro = %s
ORDER BY data_criacao DESC;
"""

SELECT_LEADS_POR_CLIENTE = """
SELECT
    id_lead,
    id_cliente,
    id_parceiro,
    status,
    data_criacao
FROM Lead
WHERE id_cliente = %s
ORDER BY data_criacao DESC;
"""

UPDATE_STATUS_LEAD = """
UPDATE Lead
SET status = %s
WHERE id_lead = %s;
"""

DELETE_LEAD = """
DELETE FROM Lead
WHERE id_lead = %s
AND status <> 'Projeto instalado';
"""