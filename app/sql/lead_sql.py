INSERT_LEAD = """
INSERT INTO Lead (
    id_parceiro,
    id_usuario,
    id_solucao,
    status
)
VALUES (%s, %s, %s, 'Novo')
RETURNING id_lead;
"""

SELECT_LEADS_POR_USUARIO = """
SELECT
    l.id_lead,
    s.tipo_solucao,
    p.nome_empresa,
    p.email,
    l.status,
    l.data_registro
FROM Lead l
JOIN Solucao s
    ON l.id_solucao = s.id_solucao
JOIN Parceiro p
    ON l.id_parceiro = p.id_parceiro
WHERE l.id_usuario = %s
ORDER BY l.data_registro DESC;
"""

SELECT_LEADS_POR_PARCEIRO = """
SELECT
    l.id_lead,
    u.nome,
    u.sobrenome,
    u.email,
    s.tipo_solucao,
    l.status,
    l.data_registro
FROM Lead l
JOIN Usuario u
    ON l.id_usuario = u.id_usuario
JOIN Solucao s
    ON l.id_solucao = s.id_solucao
WHERE l.id_parceiro = %s
ORDER BY l.data_registro DESC;
"""

UPDATE_STATUS_LEAD = """
UPDATE Lead
SET status = %s
WHERE id_lead = %s
AND id_parceiro = %s;
"""

CANCELAR_LEAD_USUARIO = """
UPDATE Lead
SET status = 'Cancelado'
WHERE id_lead = %s
AND id_usuario = %s;
"""

CANCELAR_LEAD_PARCEIRO = """
UPDATE Lead
SET status = 'Cancelado'
WHERE id_lead = %s
AND id_parceiro = %s;
"""

SELECT_LEAD_EXISTENTE = """
SELECT id_lead
FROM Lead
WHERE id_usuario = %s
AND id_parceiro = %s
AND id_solucao = %s
AND status <> 'Cancelado';
"""