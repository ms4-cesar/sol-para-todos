INSERT_LEAD = """
INSERT INTO Lead (
    id_usuario,
    id_parceiro,
    id_solucao,
    status
)
VALUES (%s, %s, %s, %s)
RETURNING id_lead;
"""
SELECT_PARCEIRO_SOLUCAO = """
SELECT * FROM parceiro_solucao
WHERE id_solucao = %s
"""

SELECT_LEADS_POR_PARCEIRO = """
SELECT
    id_lead,
    id_usuario,
    id_parceiro,
    status,
    data_registro
FROM Lead
WHERE id_parceiro = %s
ORDER BY data_registro DESC;
"""

SELECT_LEADS_POR_CLIENTE = """
SELECT
    id_lead,
    id_usuario,
    id_parceiro,
    status,
    data_registro
FROM Lead
WHERE id_usuario = %s
ORDER BY data_registro DESC;
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