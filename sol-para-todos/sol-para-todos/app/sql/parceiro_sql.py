INSERT_PARCEIRO = """
INSERT INTO Parceiro (
    nome_empresa,
    email,
    senha,
    cnpj,
    tipo_servico
)
VALUES (%s, %s, %s, %s, %s)
RETURNING id_parceiro;
"""

SELECT_PARCEIRO_POR_EMAIL = """
SELECT
    id_parceiro,
    nome_empresa,
    email,
    senha,
    cnpj,
    tipo_servico
FROM Parceiro
WHERE email = %s;
"""

SELECT_PARCEIRO_POR_ID = """
SELECT
    id_parceiro,
    nome_empresa,
    email,
    senha,
    cnpj,
    tipo_servico
FROM Parceiro
WHERE id_parceiro = %s;
"""

UPDATE_PARCEIRO = """
UPDATE Parceiro
SET
    nome_empresa = %s,
    email = %s,
    tipo_servico = %s
WHERE id_parceiro = %s;
"""

DELETE_PARCEIRO = """
DELETE FROM Parceiro
WHERE id_parceiro = %s;
"""