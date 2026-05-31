INSERT_SOLUCAO = """
INSERT INTO Solucao (
    tipo_solucao, 
    descricao_solucao, 
    requisitos
)
VALUES (%s, %s, %s)
RETURNING id_solucao;
"""

SELECT_TODAS_SOLUCOES = """
SELECT 
    id_solucao, 
    tipo_solucao, 
    descricao_solucao, 
    requisitos
FROM Solucao
ORDER BY id_solucao ASC;
"""

SELECT_SOLUCAO_POR_ID = """
SELECT 
    id_solucao, 
    tipo_solucao, 
    descricao_solucao, 
    requisitos
FROM Solucao
WHERE id_solucao = %s;
"""

UPDATE_SOLUCAO = """
UPDATE Solucao
SET tipo_solucao = %s,
    descricao_solucao = %s,
    requisitos = %s
WHERE id_solucao = %s;
"""

DELETE_SOLUCAO = """
DELETE FROM Solucao
WHERE id_solucao = %s;
"""